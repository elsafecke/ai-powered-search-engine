import os
import pyodbc
import csv
import sys
import struct
import unicodedata
from azure.identity import DefaultAzureCredential

# Load environment variables from .env file
from dotenv import load_dotenv
load_dotenv()

# Azure SQL connection settings
conn_str_base = os.getenv('AZURE_SQL_CONNECTION_STRING')

# CSV file path
CSV_FILE = 'SRCExport.csv'
table_name = 'EnforcementActionsFull2'

def get_azure_sql_token():
    """Get Azure AD access token for SQL Database"""
    try:
        credential = DefaultAzureCredential()
        # The scope for Azure SQL Database
        token = credential.get_token("https://database.windows.net/.default")
        return token.token
    except Exception as e:
        print(f"ERROR getting Azure AD token: {e}")
        return None

def create_connection_string_with_token():
    """Create connection string using Azure AD token"""
    if not conn_str_base:
        print("ERROR: AZURE_SQL_CONNECTION_STRING environment variable not set")
        return None
        
    token = get_azure_sql_token()
    if not token:
        return None
    
    # Convert token to the format pyodbc expects
    token_bytes = token.encode('utf-16-le')
    token_struct = struct.pack(f'<I{len(token_bytes)}s', len(token_bytes), token_bytes)
    
    return conn_str_base, token_struct

def validate_csv_file():
    """Check if CSV file exists and is readable"""
    if not os.path.exists(CSV_FILE):
        print(f"ERROR: CSV file '{CSV_FILE}' not found in current directory")
        return False
    
    try:
        with open(CSV_FILE, 'r', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            headers = next(reader)
            # Strip BOM from first header if present
            if headers and headers[0].startswith('\ufeff'):
                headers[0] = headers[0].replace('\ufeff', '')
            if not headers:
                print("ERROR: CSV file appears to be empty")
                return False
        print(f"✓ CSV file validated: {len(headers)} columns found")
        return True
    except Exception as e:
        print(f"ERROR reading CSV file: {e}")
        return False

def validate_sql_connection():
    """Test SQL Server connection using Azure AD"""
    try:
        conn_info = create_connection_string_with_token()
        if not conn_info:
            return False
        
        conn_str, token_struct = conn_info
        
        # Connect using the token
        conn = pyodbc.connect(conn_str, attrs_before={1256: token_struct})
        cursor = conn.cursor()
        cursor.execute("SELECT 1")
        conn.close()
        
        print("✓ SQL Server connection successful (Azure AD)")
        return True
    except Exception as e:
        print(f"ERROR connecting to SQL Server with Azure AD: {e}")
        print("Make sure you're logged in with 'az login' or have proper Azure credentials configured")
        return False

def create_or_truncate_table(cursor):
    """Create table if not exists, otherwise truncate existing table"""
    # Check if table exists
    cursor.execute(f"""
        SELECT COUNT(*) FROM INFORMATION_SCHEMA.TABLES 
        WHERE TABLE_NAME = '{table_name}'
    """)
    table_exists = cursor.fetchone()[0] > 0
    
    if table_exists:
        print(f"Table '{table_name}' exists. Truncating...")
        cursor.execute(f"TRUNCATE TABLE {table_name}")
    else:
        print(f"Creating table '{table_name}'...")
        cursor.execute(f'''
            CREATE TABLE {table_name} (
                ID INT PRIMARY KEY,
                Title NVARCHAR(MAX),
                BrowserFile NVARCHAR(MAX),
                Ordinal FLOAT NULL,
                DateIssued DATETIME,
                Published BIT,
                DocumentTypes NVARCHAR(MAX),
                KeyFacts NVARCHAR(MAX),
                DocumentText NVARCHAR(MAX),
                Commentary NVARCHAR(MAX),
                NumberOfViolations INT NULL,
                SettlementAmount FLOAT NULL,
                OfacPenalty NVARCHAR(MAX) NULL,
                AggregatePenalty NVARCHAR(MAX) NULL,
                BasePenalty NVARCHAR(MAX) NULL,
                StatutoryMaximum NVARCHAR(MAX) NULL,
                VSD NVARCHAR(MAX) NULL,
                Egregious NVARCHAR(MAX) NULL,
                WillfulOrReckless NVARCHAR(MAX) NULL,
                Criminal NVARCHAR(MAX) NULL,
                RegulatoryProvisions NVARCHAR(MAX) NULL,
                LegalIssues NVARCHAR(MAX) NULL,
                SanctionPrograms NVARCHAR(MAX) NULL,
                EnforcementCharacterizations NVARCHAR(MAX) NULL,
                Industries NVARCHAR(MAX) NULL,
                AggravatingFactors NVARCHAR(MAX) NULL,
                MitigatingFactors NVARCHAR(MAX) NULL
            )
        ''')

def deep_sanitize_string(val):
    if not isinstance(val, str):
        return val
    # Remove all non-printable and control characters
    val = ''.join(ch for ch in val if ch.isprintable() and not unicodedata.category(ch).startswith('C'))
    # Remove BOM, non-breaking space, zero-width space, etc.
    val = val.replace('\ufeff', '').replace('\xa0', '').replace('\u200b', '')
    return val.strip()

def prepare_batch_data(headers, rows):
    """Prepare data for batch insert, ensuring all values are correct type for SQL Server columns"""
    int_columns = {'ID', 'NumberOfViolations'}
    float_columns = {'Ordinal', 'SettlementAmount'}
    bit_columns = {'Published'}
    datetime_columns = {'DateIssued'}
    filtered_headers = [col for col in headers if col.strip()]
    header_indices = [i for i, col in enumerate(headers) if col.strip()]

    # Track invalid values for debug
    invalid_values = {col: [] for col in int_columns | float_columns | bit_columns}
    batch_rows = []
    for row_idx, row in enumerate(rows):
        filtered_row = []
        for idx, i in enumerate(header_indices):
            col = filtered_headers[idx]
            val = row[i]
            if isinstance(val, str):
                val = deep_sanitize_string(val)
            if val == '':
                filtered_row.append(None)
            elif col in int_columns:
                try:
                    # Only accept int-like values
                    if isinstance(val, int):
                        filtered_row.append(val)
                    elif isinstance(val, float) and val.is_integer():
                        filtered_row.append(int(val))
                    elif str(val).strip().isdigit():
                        filtered_row.append(int(val))
                    else:
                        raise ValueError
                except Exception:
                    if len(invalid_values[col]) < 5:
                        invalid_values[col].append((row_idx, val))
                    filtered_row.append(None)
            elif col in float_columns:
                try:
                    # Accept float-like values
                    float_val = float(str(val).replace(',', '').replace('$', ''))
                    filtered_row.append(float_val)
                except Exception:
                    if len(invalid_values[col]) < 5:
                        invalid_values[col].append((row_idx, val))
                    filtered_row.append(None)
            elif col in bit_columns:
                if val is None:
                    filtered_row.append(None)
                else:
                    sval = str(val).strip().upper()
                    if sval in ('1', 'TRUE', 'Y', 'YES'):
                        filtered_row.append(1)
                    elif sval in ('0', 'FALSE', 'N', 'NO'):
                        filtered_row.append(0)
                    else:
                        if len(invalid_values[col]) < 5:
                            invalid_values[col].append((row_idx, val))
                        filtered_row.append(None)
            elif col in datetime_columns:
                if val is None or val == '':
                    filtered_row.append(None)
                else:
                    filtered_row.append(str(val))
            else:
                filtered_row.append(str(val) if val is not None else None)
        # Check row length matches header length
        if len(filtered_row) != len(filtered_headers):
            print(f"[ERROR] Row {row_idx} length {len(filtered_row)} does not match headers {len(filtered_headers)}")
            print(f"Row: {filtered_row}")
        batch_rows.append(filtered_row)
    # Print summary of invalid values
    for col, vals in invalid_values.items():
        if vals:
            print(f"[WARN] First invalid values for column '{col}': {vals}")
    # Print repr() of first 3 processed rows for hidden/invisible char debugging
    print("[DEBUG] repr() of first 3 processed rows:")
    for i, row in enumerate(batch_rows[:3]):
        print(f"Row {i}: {[repr(x) for x in row]}")
    return filtered_headers, batch_rows

def print_unicode_debug(row):
    print("[UNICODE DEBUG] Code points for each value in row:")
    for idx, val in enumerate(row):
        if isinstance(val, str):
            codepoints = [f"U+{ord(c):04X}" for c in val]
            print(f"  Col {idx}: {repr(val)} -> {codepoints}")
        else:
            print(f"  Col {idx}: {repr(val)} (type: {type(val)})")

def batch_insert(cursor, headers, batch_rows):
    """Insert multiple rows in a single batch, with debug info on error"""
    if not batch_rows:
        return
    
    filtered_headers, processed_rows = prepare_batch_data(headers, batch_rows)
    
    placeholders = ','.join(['?'] * len(filtered_headers))
    columns = ','.join(f'[{col}]' for col in filtered_headers)
    sql = f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders})"
    
    cursor.fast_executemany = True  # Enable fast_executemany for much faster batch inserts
    try:
        cursor.executemany(sql, processed_rows)
    except Exception as e:
        print("\n--- BATCH INSERT ERROR DEBUG ---")
        print(f"Headers: {filtered_headers}")
        print(f"First row: {processed_rows[0] if processed_rows else 'EMPTY'}")
        print(f"Types: {[type(x) for x in processed_rows[0]] if processed_rows else 'EMPTY'}")
        print(f"repr() of first row: {[repr(x) for x in processed_rows[0]] if processed_rows else 'EMPTY'}")
        print(f"Batch size: {len(processed_rows)}")
        print(f"SQL: {sql}")
        print(f"Exception: {e}")
        if processed_rows:
            print_unicode_debug(processed_rows[0])
        print("--- END DEBUG ---\n")
        raise

def print_table_schema(cursor):
    """Print the actual SQL Server table schema"""
    print("\n--- SQL Server Table Schema ---")
    cursor.execute(f"""
        SELECT COLUMN_NAME, DATA_TYPE, CHARACTER_MAXIMUM_LENGTH
        FROM INFORMATION_SCHEMA.COLUMNS
        WHERE TABLE_NAME = '{table_name}'
    """)
    rows = cursor.fetchall()
    for row in rows:
        print(f"{row[0]:30} {row[1]:15} {row[2]}")
    print("--- END SCHEMA ---\n")

def main():
    print('Validating prerequisites...')
    
    # Validate CSV file
    if not validate_csv_file():
        sys.exit(1)
    
    # Validate SQL connection  
    if not validate_sql_connection():
        sys.exit(1)
    
    print('Validation passed. Starting truncate and reload...')
    
    # Get connection info with token
    conn_info = create_connection_string_with_token()
    if not conn_info:
        print("ERROR: Could not establish Azure AD connection")
        sys.exit(1)
    
    conn_str, token_struct = conn_info
    
    # Connect and import data
    conn = pyodbc.connect(conn_str, attrs_before={1256: token_struct})
    try:
        cursor = conn.cursor()
        create_or_truncate_table(cursor)
        conn.commit()
        print_table_schema(cursor)  # Print the actual table schema before inserting
        
        # Import data in batches
        batch_size = 1000  # Process 1000 rows at a time
        batch_rows = []
        total_rows = 0
        
        with open(CSV_FILE, encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            headers = next(reader)
            # Strip BOM from first header if present
            if headers and headers[0].startswith('\ufeff'):
                headers[0] = headers[0].replace('\ufeff', '')
            
            for row in reader:
                # Strip BOM from first value in each row if present
                if row and row[0].startswith('\ufeff'):
                    row[0] = row[0].replace('\ufeff', '')
                batch_rows.append(row)
                total_rows += 1
                
                # Process batch when it reaches batch_size
                if len(batch_rows) >= batch_size:
                    try:
                        batch_insert(cursor, headers, batch_rows)
                        conn.commit()
                        print(f"Processed {total_rows} rows...")
                        batch_rows = []  # Reset batch
                    except Exception as e:
                        print(f"Error inserting batch at row {total_rows}: {e}")
                        batch_rows = []  # Reset batch to continue
            
            # Process remaining rows in final batch
            if batch_rows:
                try:
                    batch_insert(cursor, headers, batch_rows)
                    conn.commit()
                    print(f"Processed final {len(batch_rows)} rows...")
                except Exception as e:
                    print(f"Error inserting final batch: {e}")
        
        print(f'Truncate and reload complete. Total rows loaded: {total_rows}')
    finally:
        conn.close()

if __name__ == '__main__':
    main()