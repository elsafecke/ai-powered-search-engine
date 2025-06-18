from azure.search.documents import SearchClient
from azure.search.documents.models import VectorizedQuery
from azure.core.credentials import AzureKeyCredential
from openai import AzureOpenAI
from langchain_openai import AzureOpenAIEmbeddings
from dotenv import load_dotenv
import os

load_dotenv()

# Azure Search configuration
ai_search_endpoint = os.environ["AZURE_SEARCH_ENDPOINT"]
ai_search_key = os.environ["AZURE_SEARCH_KEY"]
ai_search_index = os.environ["AZURE_SEARCH_INDEX"]

# Azure OpenAI configuration
aoai_deployment = "o3-mini"  # Updated for o3-mini
aoai_key = os.getenv("AZURE_OPENAI_API_KEY")
aoai_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")

# Initialize clients
search_client = SearchClient(ai_search_endpoint, ai_search_index, AzureKeyCredential(ai_search_key))

# Initialize Azure OpenAI client for o3-mini
openai_client = AzureOpenAI(
    api_version="2024-12-01-preview",
    azure_endpoint=aoai_endpoint,
    api_key=aoai_key,
)

embeddings_model = AzureOpenAIEmbeddings(
    azure_deployment="text-embedding-3-large",
    api_key=aoai_key,
    azure_endpoint=aoai_endpoint
)

# Configuration
NUM_SEARCH_RESULTS = 15
K_NEAREST_NEIGHBORS = 30

def run_search(search_query: str):
    """
    Perform a search using Azure Cognitive Search with both semantic and vector queries.
    Searches across KeyFacts, DocumentText, and Commentary vector fields.
    """
    # Generate vector embedding for the query
    query_vector = embeddings_model.embed_query(search_query)
    
    # Create vector queries for all three vector fields
    vector_queries = [
        VectorizedQuery(
            vector=query_vector,
            k_nearest_neighbors=K_NEAREST_NEIGHBORS,
            fields="KeyFactsVector"
        ),
        VectorizedQuery(
            vector=query_vector,
            k_nearest_neighbors=K_NEAREST_NEIGHBORS,
            fields="DocumentTextVector"
        ),
        VectorizedQuery(
            vector=query_vector,
            k_nearest_neighbors=K_NEAREST_NEIGHBORS,
            fields="CommentaryVector"
        )
    ]
    
    # Perform the search with all vector fields and corresponding text fields
    results = search_client.search(
        search_text=search_query,
        vector_queries=vector_queries,
        select=["ID", "BrowserFile", "Title", "KeyFacts", "DocumentText", "Commentary", 
                "DateIssued", "Published", "DocumentTypes", "NumberOfViolations", 
                "SettlementAmount", "SanctionPrograms", "Industries"],
        top=NUM_SEARCH_RESULTS
    )
    
    search_results = []
    for result in results:
        # Combine all text content for the LLM with clear delineation
        content_parts = []
        
        # Always include title at the top
        if result.get("Title"):
            content_parts.append(f"=== TITLE ===\n{result['Title']}\n=== END TITLE ===")
        
        if result.get("KeyFacts"):
            content_parts.append(f"=== KEY FACTS ===\n{result['KeyFacts']}\n=== END KEY FACTS ===")
        
        if result.get("DocumentText"):
            content_parts.append(f"=== DOCUMENT TEXT ===\n{result['DocumentText']}\n=== END DOCUMENT TEXT ===")
        
        if result.get("Commentary"):
            content_parts.append(f"=== COMMENTARY ===\n{result['Commentary']}\n=== END COMMENTARY ===")
        
        combined_content = "\n\n".join(content_parts)
        
        search_result = {
            "id": result["ID"],
            "content": combined_content,
            "title": result.get("Title", ""),
            "browser_file": result.get("BrowserFile", ""),
            "date_issued": result.get("DateIssued", ""),
            "document_types": result.get("DocumentTypes", ""),
            "settlement_amount": result.get("SettlementAmount", ""),
            "sanction_programs": result.get("SanctionPrograms", ""),
            "industries": result.get("Industries", ""),
            "score": result["@search.score"]
        }
        search_results.append(search_result)
    
    return search_results

def generate_answer(user_question: str, search_results: list):
    """
    Generate an answer using o3-mini and search results.
    """
    final_prompt = """Review the provided documents and commentary to answer the user's question.

    ###Guidance###

    1. From the list of provided documents, list out which are relevant to the user's question.
    2. For each relevant document, explain how it addresses the user's question. Make sure to cite the document title and put the title in brackets. Always refer to the documents by [title], not by number.
    3. Commentary may also be relevant to the user's question. If so, explain how it addresses the user's question. 
    4. If there is no relevant information in the documents or commentary, say that you couldn't find any relevant information to answer the question. Under no circumstances should you answer with anything outside of the context of the search results. This is a legal search engine AI, accuracy is paramount. Do not make assumptions or inferences.
    
    ###Output Format###

    - Always begin your answer stating 'Yes.', 'No.', 'It depends.', or 'It is unclear.', followed by identifying which documents you're referencing (e.g., "According to [Document Title]..."). 
    - When referencing information, clearly indicate which document it came from
    - Use the document titles provided in the TITLE sections to identify sources
    - If information comes from multiple documents, mention all relevant sources
    - Be specific about which document contains which information
    - Summarize the expert commentary at the end if relevant to the user's question.

    ###Examples###

    
    #### Example 1 ####
    User: Can Zarnian-origin commemorative stamps be imported into the U.S.?
    Assistant: According to [Title], the importation of Zarnian-origin commemorative stamps into the United States is subject to restrictions under the Zarnian Transactions and Sanctions Regulations (ZTSR). However, the permissibility depends on specific factors:

        - If the stamps are still valid for postage, their importation is prohibited unless specifically licensed by the Office of Foreign Assets Control (OFAC).
        - If the stamps are no longer valid and qualify as informational materials, their importation may be exempt from the prohibition.
    
    Additionally, [Title] explains that wholly domestic transactions involving such stamps may be authorized under ZTSR § 670.518, provided they are not blocked property.

    Expert commentary further clarifies that the same stamp may fall inside or outside the exemption depending on whether it retains postal value. This distinction is critical in determining whether OFAC authorization is required.

    
    #### Example 2 ####
    User: are transactions related to Information housed on a subscription database of legal information exempt under the informational materials exemption?
    Assistant: According to Case No. IA-2012-293259-1, transactions involving access to a subscription database of legal information—such as HeinOnline—are exempt under the informational materials exemption of the Iranian Transactions Regulations (ITR), provided certain conditions are met.

    OFAC determined that such access does not require a license under ITR § 560.210(c), as long as:

    - The content is fully created and in existence at the time of transmission, and
    - It is not created at the behest of an Iranian person.
    
    The exemption does not apply if the transaction involves alteration or enhancement of the materials, or the provision of marketing or consulting services.

    The commentary confirms that commercial access to web-based databases is exempt, even when login credentials or search functionality are involved. OFAC interprets “fully created and in existence” to mean at the time of transmission, ensuring that static, pre-existing content qualifies—so long as it is not tailored for a sanctioned party.
    
    #### Example 3 ####
    User: Is paying "landings fees and ground handling payments" to a blocked airport operator in connection with a charter flight exempt under the travel exemption?
    Assistant: According to Case No. Ukraine-EO13662-2018-353695-1, payments of landing fees and ground handling charges to blocked airport operators in connection with charter flights are not explicitly exempt under the travel exemption, and OFAC does not confirm that such payments fall within that exemption.

    In Case No. Ukraine-EO13662-2018-353695-1, Scandinavian Airlines System (SAS) sought guidance on operating charter flights to Russian airports managed by entities owned 50% or more by SDNs. OFAC concluded that the proposed payments—made in non-U.S. dollar funds and without U.S. person or financial system involvement—were not prohibited under the Ukraine-Related Sanctions Regulations (URSR). However, OFAC declined to opine on whether the transactions would be considered “significant” under secondary sanctions provisions in CAATSA.

    Notably, OFAC did not invoke the travel exemption as a basis for its conclusion. The commentary suggests that if OFAC believed the exemption applied, it likely would have said so. This implies that such payments are not categorically exempt under the travel exemption and may still raise sanctions concerns depending on the involvement of U.S. persons or the U.S. financial system.

    The commentary highlights that OFAC’s silence on the travel exemption is meaningful. While the travel exemption under IEEPA applies to the URSR (see FAQ 504), OFAC did not apply it here—possibly because the payments were made to SDN-owned entities. The analysis suggests that if the transaction had involved U.S. persons or U.S. dollars, it might have been prohibited, reinforcing that the exemption does not clearly cover such payments.
        """
    
    # Format search results for the LLM with clear document separation
    formatted_results = []
    for i, result in enumerate(search_results, 1):
        formatted_results.append(f"DOCUMENT {i}:\n{result['content']}")
    
    llm_input = f"""Create a comprehensive answer to the user's question using these search results.

                User Question: {user_question}

                Search Results:
                {chr(10).join(formatted_results)}

                Synthesize these results into a clear, complete answer. Remember to cite which documents contain the information you're referencing."""
    
    messages = [
        {"role": "system", "content": final_prompt},
        {"role": "user", "content": llm_input}
    ]
    
    response = openai_client.chat.completions.create(
        messages=messages,
        model=aoai_deployment,
        max_completion_tokens=2000
    )
    
    return response.choices[0].message.content

def process_question(question: str):
    """
    Main function that takes a user question, performs search, and generates answer.
    
    Args:
        question: The user's question
        
    Returns:
        dict: Contains the question, documents, and answer
    """
    # Step 1: User input (already provided)
    
    # Step 2 & 3: Convert to vector embedding and run search
    documents = run_search(question)
    
    # Step 4: Generate answer via LLM + search results
    answer = generate_answer(question, documents)
    
    return {
        "question": question,
        "documents": documents,
        "answer": answer
    }

if __name__ == "__main__":
    import json
    
    # Example usage
    user_question = input("Enter your question: ")
    result = process_question(user_question)
    
    print("\n" + "="*80)
    print("SEARCH AND ANSWER RESULT")
    print("="*80)
    
    print(f"\nQuestion: {result['question']}")
    
    print(f"\nDocuments Found ({len(result['documents'])}):")
    for i, doc in enumerate(result['documents'], 1):
        print(f"{i}. {doc['title']}")
    
    print(f"\nAnswer:")
    print(result['answer'])