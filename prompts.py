simple_search_prompt = """ You are given a user query. Historically, users had to manually write the specific search query syntax themselves and manaully select the filters they want to apply. Your job is to do this for them based on the query.

 

###Distinct Values for Filters###

 

<DocumentType>

 

Currently on OFAC's Website

Currently on OFAC's Website

Removed from OFAC's Website

Removed from OFAC's Website

Active

Active

Blocked Property-Related Licenses (Non-Real Estate)

Code of Federal Regulations

Current

Enforcement

Enforcement Releases

General Commercial

Interpretive Rulings

Notable U.S. Federal Court Opnions

OFAC FAQs

OverRuled Research Notes (System Notes)

Primary Sanctions Enforcement

Secondary Sanctions

Specific Licenses

Unpublished Correspondence/Guidance Letters

Advisories

Compliance

Expired/Revoked

General Licenses

Licenses Unrelated to Blocked Property

Non-profit/Humanitarian

OFAC Settlement Agreements

OFAC/USG Statements In Litigation

Other Guidance

Published (incl. Archived/Removed) OFAC-Related Guidance

Revoked

SEC Correspondence on Sanctions

Secondary Sanction Waivers

Secondary Sanctions Enforcement

Select Derivative Designation & Other Targeting Criteria

Terminated from Jan. 2020 Onward

Alerts

Blocked U.S. Real Estate-Related Licenses

Directives & Determinations

Licensing

Miscellaneous

Notable Federal Register Notice Preambles

OFAC Enforcement Correspondence

Parallel BIS Settlement Agreements

U.S. Government Business

Unpublished OFAC-Related Guidance

Criminal Sanctions Enforcement

Information for Industry Groups

Legal Services

Notable Customs Rulings

Statements of Licensing Policy

U.S. Legal Authorities

Excecutive Orders

Notable BIS-Issued Guidance

Repealed/Superseded Regulatory Provisions

Notable Reports to Congress

Other

Statutes

State Department Sanctions Guidance

Current OFAC FAQs

Internal/Intra-Governmental Correspondence

FAQs Removed From OFAC's Website

Notable Blocking/Unblocking Notices

FAQs "Archived" on OFAC's Website

Items Substantively Duplicative of Others in the Research Center

Miscellaneous

Miscellaneous

Other

Miscellaneous

 

<LegalIssues>

 

Primary Sanctions​​

Cross-Programmatic Issues​​​

Jurisdiction​

U.S./U.S. Person Definitions​

ITSR-Specific​

Re-Exports by Non-U.S. Persons Prohibition​

U.S.-Owned or -Controlled Foreign Entities

CACR- and IACR-Specific ​

Persons Subject to U.S. Jurisdiction/Within the U.S.

Property Subject to U.S. Jurisdiction​

Prohibited Facilitation

U.S. Employees of Non-U.S. Person Entities

Indirect Transactions/Transshipments

Provision of Funds to Non-Sanctioned Persons

General Inventory

Indirect Benefit

Third-Country Consortia

Bank-to-Bank Transfers

Ordinarily Incident

Ordinarily Incident to a Licensed Transaction

Application of Ordinarily Incident  Interpretive Provision

Application of Ordinarily Incident in Text of GLs

Transactions Incident to Exempt Transactions

Incident to Informational Materials Transactions

Travel Exemption

Underlying Transactions by Non-U.S. Persons

Exemptions

Informational Materials

Informational Materials Definition

"Substantive Alteration or Enhancement"

"In Existence" at Time of a Transaction

"Fully Created and In Existence"

Publishing GLs

Personal Communications Exemption

Conferences/Live Exchanges

Donations Exemption

Applicability of IEEPA Exemptions

Causing/Attempting/Evading/Avoiding/Conspiring

Evasion or Avoidance

Causing Violations

Conspiracy

Attempted Violations

Knowledge/Reason to Know

Meaning of "Knowledge"/"Reason to Know"

Due Diligence Expectations

Compliance Expectations for Correspondent Banks

Pre-Transactions Activities (e.g., Negotiations)

"Negotiations" vs. Preliminary Discussions

Entering Into vs. Executing Contracts

Other Pre-Transactional Activities

Miscellaneous

"Control" Tests in General

"Wind Down" or "Maintenance" Licenses

All Within Parent Category

"Maintenance"

"Wind Down"

"Relation of This Part to Other Laws and Regulations" Provision

Different OFAC Treatment of Similar Language Across Programs

Legal Separation of Related Programs

Noncommercial Personal Remittances GLs

Litigation Involving Blocked Persons/Property

"Effective Date"

"Official Business"

Telecommunications GLs

Communications/Personal Communications GLs

NGO GLs

"Effect of Amendment" Provisions

Voluntary Self-Disclosure Credit

Whether an Offshore Transaction Would be Prohibited if Engaged in by a U.S. Person

Brokering

EAR-Related

Blocking Sanctions Generally

Property/Property Interest Definitions

"Service" as "Property"

"Contracts" as "Property"

Property in Which a Blocked Person Has an Interest

Indirect Interest/50 Percent Rule

Application of 50 Percent Rule

Blocked Person Interests Arising Out of Contractual Chains

Non-Ownership "Interests" in Property

Contingent Interest in Property

Offshore Extinguishment of Interest in Property

Ongoing Interests in Items Manufactured by Blocked Producers

Interests Arising Out of "Control" Over Property

Non-Blocked Entities With Blocked Senior Executives

Special/Ad-Hoc "Affirmative Determinations"

"Termination and Acquisition of an Interest" Provision

Select "No Interest" Determinations

Unblocking of Persons and Property

By Operation of Law/Divestment

Offshore Divestments/FAQ #402

Delisting

Licensing Policies on Release of "Blocked Property"

"Effect of Transfers" Provision

"Transfer"/"Dealing in"

"Transferred, Paid, Exported, Withdrawn, or Otherwise Dealt in"

"Transfer" (Generally)

"Transfer" (Litigation)​

Provision/Receipt of Services Involving Blocked Property/Persons

Blocking by Operation of Law (Non-50 Percent Rule)

Blocked "Government of" Provision

Blocked Government "Control"

Specific Blocked Government "Control" Tests

"Acting on Behalf of"

Specific Blocked Government "Acting on Behalf of" Tests

"Acting on Behalf of" Tests in General

Cuban "National" Test

"Agent" of Foreign Terrorist Organization

Miscellaneous Blocking Issues

U.S. Person "Possession or Control"

Foreign Persons Physically Located in the U.S.

Non-Blocking Sanctions Generally (Incl. Services)

Importation/Exportation of "Service"

Exportation of Goods, Services and Technology

Exportation of Services "to"

"Ordinarily Resident"

Bank-to-Bank Transfers

Meaning of Importation

"New Investment" (In General)

"New Investment" (Russia)

Program-Specific

Iranian Transactions and Sanctions Regulations-Specific

Dealing in Iranian-Origin Goods and Services Prohibition

"Iranian Origin" Good/Service

U.S.-Owned or -Controlled Foreign Entities Prohibition

Transactions "With" Government of Iran (and Related Examples)

Cuban Assets Control Regulations-Specific

CACR-Specific Blocking Prohibition

Cuba Travel

"New Debt"/"New Equity" Related Prohibitions

"New Equity"

"New Debt"

"Debt"

Debt "of" a Sanctions Target

"Dealing" in Debt

Pre-Sanctions Debt Conversion to "New Debt"

"Substantial Transformation" and/or "Incorporation" of Items

Secondary Sanctions

OFAC Stating That Non-U.S. Persons Will Not Be Sanctioned Not Requiring a License for a USP​

Derivative Designation Criteria

Material Assistance/Support Designation Criteria

"Owned or Controlled" Designation Criteria

"Acting on Behalf of" Designation Criteria

"Operating In" a Targeted Sector Designation Criteria

Secondary Sanctions Generally

"Significant Transaction"

"Knowingly" Engaging in Sanctionable Conduct

 

<Programs>

 

Item Pertains to All or Many Discrete Sanctions Programs

All Counter Narcotics Sanctions Programs

Foreign Narcotics Kingpin Sanctions Regulations (FNKSR)(31 CFR 598)

Narcotics Trafficking Sanctions Regulations (NTSR) (31 CFR 536)

Illicit Drug Trade Sanctions Regulations (IDTSR) (31 CFR 599)

Sec. 7201 Et Seq. the FY 2020 NDAA (Fentanyl) ("Fentanyl Sanctions Act")

FEND off Fe​​ntanyl Act (2024 "National Security Supplemental")​

Illicit Captagon T​rafficking Suppression Act of 2023

Counter WMD Proliferation (Non Proliferation Sanctions)

Weapons of Mass Destruction Proliferators Sanctions Regulations (WMDPSR) (31 CFR 544)

Weapons of Mass Destruction Trade Control Regulations (WMDTCR) (31 CFR 539)

Iran-Iraq Arms Non-Proliferation Act (Administered by State Department) (IIANPA)

Iran, North Korea, and Syria Nonproliferation Act Sanctions (Administered by State Department) (INKSNA)

Foreign Sanctions Evaders Executive Order 13608 (Covers Evaders of Non-Proliferation Sanctions, Among Others)

Counter Terrorism Sanctions

Global Terrorism Sanctions Regulations (GTSR) (31 CFR 594) (Incl. the Unincorporated Secondary Sanctions in EO 13224 as Amended by EO 13886)

The Global Terrorism Sanctions Regulations (GTSR) as applied to the Taliban and/or the Haqqani Network

The Global Terrorism Sanctions Regulations (GTSR) as applied to Ansarallah ("the Houthis")

Hizballah Financial Sanctions Regulations (HFSR) (31 CFR 566)

Terrorism List Governments Sanctions Regulations (TLGSR) (31 CFR 596)

Foreign Terrorist Organizations Sanctions Regulations (FTOSR) (31 CFR 597)

Section 2993B of the Antiterrorism and Effective Death Penalty Act of 1996 (AEDPA) (the "Material Support" Statute)

Terrorism Sanctions Regulations (TSR) (31 CFR 595) [TERMINATED]

Hamas and Other Palestinian Terrorist Groups International Financing Prevention Act​​

Sanctions With Respect to Threats to Current or Former United States Officials

Cuba-Related Sanctions

Cuban Assets Control Regulations (CACR) (31 CFR 515)

Documents Related to the Cuba-Related "Secondary Sanctions" Imposed by the Helms-Burton Act of 1996 (Administered by the State Department)

Iran-Related Sanctions

Iran-Related Primary Sanctions Regulations and EOs (See Below for Hybrid Blocking/Secondary Sanctions Authorities)

Iranian Transactions and Sanctions Regulations (ITSR) (31 CFR 560)

Iranian Financial Sanctions Regulations (IFSR) (31 CFR 561)

The IRGC-Related Prohibition Pertaining to Persons Owned or Controlled by U.S. Financial Institutions (561.202 of the IFSR)

Iranian Sector and Human Rights Abuses Sanctions Regulations (ISHRASR) (31 CFR 562)

Iranian Assets Control Regulations (IACR) (31 CFR 535)

Grave Human Rights Abuses by the Governments of Iran and Syria Via Information Technology (GHRAVITY EO)

Executive Order 13949 - Blocking Property of Certain Persons With Respect to the Conventional Arms Activities of Iran

Documents Related to All Iran-Related Secondary Sanctions Authorities

Iranian Financial Sanctions Regulations (IFSR) (31 CFR 561), and Documents Related to the Authorities Incorporated Into the IFSR

The "CAPTA" Financial Sanctions, Derived From Sec. 104 of CISADA, Implemented at 561.201 of the IFSR

Petroleum-Related Sanctions in Sec. 1245 of the FY 2012 NDAA, as Amended, Implemented at 561.203 of the IFSR

Items Pertaining to the Sanctions Initially Imposed in Revoked EO 13622, and Reimposed in 2018 by EO 13846

Metals-Related CAPTA Financial Sanctions Derived From Sec. 2 of EO 13871, Implemented in the IFSR at 561.205

Executive Order 13846 (Reimposing Certain Sanctions With Respect to Iran) (Unincorporated in Regulations)

Items Pertaining to the Sanctions Initially Imposed in Revoked EO 13645, and Reimposed in 2018 by EO 13846

Executive Order 13876 (Sanctions With Respect to the Supreme Leader of Iran) (Unincorporated in Regulations)

Executive Order 13902 (Sanctions With Respect to Additional Sectors of Iran) (Unincorporated in regulations)

Iran-Related Statutes Containing Secondary Sanctions Authorities and Derivative Designation Criteria

Iran Threat Reduction and Syria Human Rights Act of 2012 (ITRSHRA)

Iran Freedom and Counter-Proliferation Act of 2012 (IFCA)

Iran Sanctions Act (ISA)

Countering America’s Adversaries Through Sanctions Act (CAATSA) (Iran-Related Title I)

Stop Harboring Iranian Petroleum Act

Fight and Combat Ramp​ant Iranian Missile Exports Act

Mahsa Amini Human rights and Security Accountability Act

JPOA and JCPOA-Related Documents Only

JPOA

JCPOA (Joint Comprehensive Plan of Action)

North Korea-Related Sanctions

North Korea Sanctions Regulations (NKSR) 31 CFR 510

Sec. 7121 the FY 2020 NDAA (Otto Warmbier North Korea Nuclear Sanctions and Enforcement Act of 2019)

Active North Korea-Related Secondary Sanctions

The Repealed Foreign Assets Control Regulations (FACR) (1950-2008, Applicable to North Korea and Others) (31 CFR 500)

Syrian and "Syria-Related" Sanctions

Syrian Sanctions Regulations (SySR) (31 CFR 542)

Syria-Related Sanctions Regulations (31 CFR 569) (Implementing (EO 13894)

CAATSA Sec. 234 (Implemented into SySR 6-5-24)

Syria-Related Secondary Sanctions - the FY 2020 NDAA (Syria) (the "Caesar Syria Civilian Protection Act of 2019") (Implemented into SySR 6-5-24)

Ukraine-/Russia-Related Sanctions

EO 14024 and the Russian Harmful Foreign Activities Sanctions Regulations

Directive 1/1A Under EO 14024 (prohibitions incorporated in the RuHSR)

Directive 2 Under EO 14024 (prohibitions incorporated in the RuHSR)

Directive 3 Under EO 14024 (prohibitions incorporated in the RuHSR)

Directive 4 Under EO 14024 (prohibitions incorporated in the RuHSR)

Items Related to the Various"Sectoral Determinations" Pursuant to EO 14024 that AuthorizeDesignation of Persons "Operating in" Specified Sectors of theRussian Economy

Items Related to the Secondary Sanctions Authority at EO14024, as Amended by EO 14114.

EO 14066 (Prohibiting Certain Imports and New Investments; prohibitions incorporated in the RuHSR)

EO 14068 ("Prohibiting Certain Imports, Exports, and New Investment"; prohibitions incorporated in the RuHSR)

Diamond-related Import ProhibitionsIssued Pursuant to EO EO 14068

Prohibitions Related to Imports of Aluminum, Copper, and Nickel of Russian Federation Origin Pursuant to EO 14068

Determination Pursuant to Section 1(a)(i) of EO 14068 (June 28, 2022) (Gold-related)

EO 14071 (Prohibiting New Investment in and Certain Services; prohibitions incorporated in the RuHSR)

The "New Investment" Prohibitionof EO 14071

Determination Related to Accounting, Management Consulting,and Trust and Corporate Formation Services

Determination Related to Architecture and Engineering Services

Determination Related to Services for the Acquisition of Aluminum, Copper, or Nickel of Russian Federation Origin

Determination Related to Quantum Computing Services

Determination in re: Services Related to Maritime Transportof Russian Oil and Petroleum Products (the "Price Cap" Prohibition)

Ukraine-/Russia-Related Sanctions Regulations (URSR) (31 CFR 589)

Documents Pertaining to the EO 13662-Based "Sectoral Sanctions" Directives (Prohibitions Incorporated in 589.201)

Executive Order 13685 (the Crimea Embargo and Certain Blocking Prohibitions; prohibitions incorporated in the URSR)

Executive Order 14065 (Luhansk/Donetsk/Donbass Embargo and Related Blocking Prohibitions; prohibitions incorporated in the URSR)

Russia-Related Directive Pursuant to EO 13883 the "CBW Act Directive"

Other Primary Sanctions Programs Focused on Russia

Magnitsky Act Sanctions Regulations (MASR) (31 CFR 584)

Cyber-Related Sanctions Regulations (31 CFR 578) (CRSR)

Russia-Related Secondary Sanctions Authorities

Support for the Sovereignty, Integrity, Democracy, and Economic Stability of Ukraine Act of 2014 (SSIDES), as Amended by CAATSA (Partially incorporated in the URSR)

Ukraine Freedom Support Act of 2014 (UFSA), as Amended by CAATSA (Partially incorporated in the URSR)

Secondary Sanctions and Derivative Designation Authorities in (Russia-Related Title II of CAATSA)

CAATSA Sec. 224 (Incorporated in the Cyber-related Sanctions Regulations)

CAATSA Sec. 231 (Transactions With the Defense/Intelligence Sectors)

CAATSA Sec. 232 (Development of Pipelines in Russia)

CAATSA Sec. 233 (Privatization of State-owned Assets)

Sec. 7503 the FY 2020 NDAA (Russia) ("PEESA") and/or E.O. 14039

Section 5590 of the FY 2023 NDAA (Gold-related Secondary Sanctions)

Venezuela-Related Sanctions, EOs Incorporated in the Venezuela Sanctions Regulations (31 CFR 591)

EO 13692 (Blocking Property and Suspending Entry of Certain Persons Contributing to the Situation in Venezuela (March 8, 2015))

EO 13850  (Blocking Property of Additional Persons Contributing to the Situation in Venezuela (November 1, 2018))

EO 13835  (Prohibiting Certain Additional Transactions with Respect to Venezuela (May 21, 2018))

EO 13827 (Taking Additional Steps to Address the Situation in Venezuela (March 19, 2018))

EO 13808 (Imposing Additional Sanctions with Respect to the Situation in Venezuela (August 24, 2017))

EO 13884 (Blocking Property of the Government of Venezuela (August 5, 2019))

All Other Primary Sanctions Programs

Reporting, Procedures and Penalties Regulations (RPPR) (31 CFR 501)

Balkans-Related Sanctions (Fmr. Yugoslavia) and EO 14033

Western Balkans Stabilization Regulations (WBSR)

Fed. Rep. of Yugoslavia (Serbia and Montenegro) and Bosnian Serb-controlled Areas of the Rep. of Bosnia and Herzegovina (31 CFR 585) [TERMINATED]

Fed. Rep. of Yugoslavia (Serbia & Montenegro) Kosovo Sanctions Regulations (31 CFR 586) [TERMINATED]

Belarus-Related Sanctions

BelarusSanctions Regulations (BeSR) (31 CFR 548)

Directive 1 Under Belarus Executive Order 14038

Burma-Related Sanctions (Myanmar)

Burmese Sanctions Regulations (BSR) (31 CFR 537) [TERMINATED, removed in 2017] (Myanmar)

Burma Sanctions Regulations (BSR) (31 CFR 525) (Implementing EO 14014)

Directive 1 Under EO 14014 (the "MOGE Financial Services Directive")

Côte d'Ivoire Sanctions Regulations (Cote) (31 CFR 543) [TERMINATED]

Central African Republic Sanctions Regulations (CARSR) (31 CFR 553)

Chinese Military Companies Sanctions (PRC - China) (EO 13959 as amended by EO 14032).

Democratic Republic of the Congo Sanctions Regulations (DRCSR) (31 CFR 547)

Ethiopia-Related Executive Order 14046

Foreign Assets Control Regulations (FACR) (31 CFR 500) [TERMINATED]

Foreign Interference in U.S. Elections Sanctions Regulations (31 CFR 579)

Foreign Sanctions Evaders Executive Order 13608 (Prohibitions Not Fully Incorporated in Regulations)

Global Magnitsky Sanctions Regulations (GMSR) (31 CFR 583)

Hong Kong-Related Sanctions

The Hong Kong Human Rights and Democracy Act of 2019

The Hong Kong Autonomy Act of 2020 (Including Its Secondary Sanctions Provisions)

Hong Kong-Related Sanctions Regulations (HKSR) (31 CFR 585)(Implementing EO 13936)

International Criminal Court-Related​ Sanctions Regulations (EO 13928 and 14203)​

Iraq-Related Sanctions

Iraqi Sanctions Regulations (ISR) (31 CFR 575) [TERMINATED]

Iraq Stabilization and Insurgency Sanctions Regulations (ISISR) (31 CFR 576)

Lebanon Sanctions Regulations (31 Part 549)

Former Liberian Regime of Charles Taylor Sanctions Regulations (31 CFR 593) [TERMINATED]

Libya-Related Sanctions

Libyan Sanctions Regulations (LSR) (31 CFR 550) [TERMINATED]

Libyan Sanctions Regulations (LSR) (31 CFR 570)

Mali Sanctions Regulations (31 CFR 555)

Nicaragua Sanctions Regulations (31 CFR 582)

Sec. 2 of the Protecting American Intellectual Property Act of 2022

Transnational Criminal Organizations Sanctions Regulations (TCOSR) (31 CFR 590)

Somalia Sanctions Regulations (SoSR) (31 CFR 551)

South Sudan Sanctions Regulations 31 CFR 558

Sudan-Related Sanctions (Incl. Darfur; Excluding South Sudan)

Sudanese Sanctions Regulations (31 CFR 538) (SSR) [TERMINATED]

Sudan Stabilization Sanctions Regulations (f/k/a Darfur Sanctions Regulations) (31 CFR 546) (Implementing EO 13400/EO 14098)

EO Blocking Certain Property of Da Afghanistan Bank (EO 14064)

Taliban (Afghanistan) Sanctions Regulations (TASR) (31 CFR 545) [TERMINATED]

Hostages and Wrongful Detention Sanctions Regulations (31 CFR 526)

Yemen Sanctions Regulations (YSR) (31 CFR 552)

Uyghur Human Rights Policy Act of 2020

West Bank-related EO 14115

Zimbabwe Sanctions Regulations (ZSR) (31 CFR 541) [TERMINATED]

 

<EnforcementCharacterization>

 

Exports of Goods to Sanctioned Destinations; Provision of Goods to Blocked Persons

Direct Export of Goods to Sanctioned Destination From U.S.

Direct Export of Goods (of Any Origin) From Third-Country to Sanctioned Destination by Person Subject to Export Prohibitions

Transshipment of Goods by Person Subject to Sanctions Prohibition, Through Third Country (Exporter Knew or Had Reason to Know of Sanctioned Destination)

Reexportation of U.S.-Origin Goods to Sanctioned Destination by a Person Not Otherwise Subject to Sanctions Prohibitions

Transshipment of Goods Through Sanctioned Destination (With Non-Sanctioned Destination)

Export of and/or Provision of Goods to Blocked Persons

Shipment of Components for Commingling With or Incorporating Into Product Destined for Prohibited Destination

Financial Sector Only: Exports of Financial Services to Sanctioned Destinations and/or Dealing in Blocked Property

Payment Processing by Intermediary Banks Only

Notable Enforcement Actions Arising Out of Bank-to-Bank Transfers, Initiated by Foreign Banks, Where the Foreign Bank Was Transacting on Its Own Account

[Excluding Financial Institutions] - Exports of Services to Sanctioned Destinations/Persons; Provision of Services or Funds (Excl. Goods) to Blocked Persons

Provision/Receipt of Funds to/From Blocked or Otherwise Sanctioned Persons; Exports of "Financial Services" to Such Persons

Export/Provision of Consulting, Marketing and Other Professional Services

Export/Provision of All Other Services (Internet Services, Telecom Services, Etc., Incl. Unspecified Services)

Imports of/Dealings in Services From Sanctioned Countries and/or "Dealing In" Services of/Provided by Blocked Persons

Imports of Goods from Sanctioned Countries and/or Blocked Persons, Incl. Prohibited Imports of Goods Containing Materials from Certain Sanctioned Countries

Prohibited Offshore Dealings in Goods of Cuban or Iranian Origin

Prohibited "Facilitation"

Actions, e.g. Approvals, Coordination, Planning, Etc., Performed by a U.S. Person to Facilitate an Otherwise Prohibited Transaction for Related Non-U.S. Company

The Transportation of Goods, Insuring Transactions, Brokering, Processing Payments and Other Activities Unrelated to the Business of the Primary Violator

Referral of Business Opportunities to Third Parties; Referring Sales to Related Companies

Miscellaneous "Dealing" in Blocked Property

Violation Based on a Dealing with a Person Blocked Pursuant to the 50% Rule (50 Percent Rule)

Dealing in Prohibited (Non-blocked) "Debt" or "Equity" (Venezuela/Russia Only)

Violation of the Reporting, Procedures and Penalties Regulations (RPPR)

Ignored Request to Furnish Information, Insufficient Responses

Failure to Retain Records

Failure to Submit of Blocking Report to OFAC on Time

Violation of the Prohibition Against "New Investment" in a Sanctioned Destination

Violation Connected to Unauthorized Travel

To Cuba

To Iraq

Certain "Trade-Related" Transactions Involving Iran (560.206); Incl. Offshore "Dealing In" Iranian Origin Goods or Services Other Than Importations Thereof

Conspiracy; Attempts; Evasion/Avoidance of Prohibitions

Attempt

Evasion/Avoidance (Evade/Avoid)

Violations Resulting From Contracts, Negotiations, Invoicing and Other "Pre-Transactional" Activities

Execution of/Entry Into "Contracts"

Execution of Documents/Agreements Other Than "Contracts"

Negotiation

Invoicing

Other

Direct Violation Committed by a Non-U.S. Person Entity Subject to Sanctions Prohibitions

Violation of the ITSR (Iran) (560.215) (U.S.-Owned or -Controlled Foreign Entity)

Violation of the CACR (Cuba) (515.201 Read in Light of 515.329)

Violation by Non-U.S. "Branch" (Non-Subsidiary) Qualifying for Treatment as a "U.S. Person" (Excl. Direct ITSR/CACR Violations by Non-U.S. Persons)

Non-U.S. Person Not Otherwise Subject to Sanctions Prohibitions "Caused" U.S. Person to Violate One or More Primary Sanctions Prohibitions

Foreign Bank Not Subject to Sanctions Prohibitions "Caused" U.S. Bank or Financial Service Provider to Violate Sanctions Prohibitions

Violation "Caused" Intentionally; e.g. Through Payment Message Stripping; Obfuscation; Failure to Disclose Nature of Parties Involved

Violation "Caused" as a Result of Lack of Adequate Diligence on the Part of the Foreign Bank

Foreign (Non-Bank) PaymentOriginator "Caused" U.S. Bank to Export Fin. Services to Destination and/orOtherwise Engage in Prohibited Dealing

Foreign Person "Caused" Person Subject to U.S. Jurisdiction to Export and/or Transship Goods

Foreign Non-bank Person "Caused" Violation Through the Issuance of U.S.-Implicating Invoices

Factual; Legal Characterizations of Circumstances Underlying the Violation(s)

"Quasi-Extraterritorial" Applications of "Primary Sanctions" Laws (E.g. "Causing" Violations of Sanctions Laws)

Penalties Sorted by Descriptions of Diligence/Compliance Program Failures (Where Applicable)

Problems Related to Screening Software

Filter Inadequate With Respect to Fields Scanned and/or Keywords Triggering Alerts

Failure to Re-Screen Pre-Existing Customers; Inadequate Updating of Interdiction Software

Flagged Payment That Should Have Been Blocked Was Only Rejected

Insufficiently Competent Remedying of Receipt of Negative Information (Incl. Post-Alert Delays)

Failure to Affirmatively Investigate Purpose of a Transaction, End Use/Users; Missed Red Flags; Failure Screen All Parties to a Transaction

Failure to Ensure Acquired Foreign Company Ceases Engaging in Activities Prohibited as a Result of Acquisition

Violations Committed by Predecessor Entity Prior toAcquisition by a U.S. Person (Successor Liability)

Reliance on Incorrect Legal; Compliance-Related Advice Re: Sanctions Laws

Supply Chain Diligence Failure (Contents of Items Purchased From Third Country Distributors)

Failure to Detect Entity Blocked Pursuant to the 50% (50 Percent) Rule

 

###Output Format Guidance###

 

Structure your output in the following format:

 

{

    DateIssuedBegin: date?,

    DateIssuedEnd: date?,

    LegalIssue: [string, string...],

    Program: [string, string...],

    DocumentType: [string, string...],

    RegulatoryProvision: [string, string...],

    Published: boolean,

    EnforcementCharacterization: [string, string...],

    NumberOfViolationsLow: int?,

    NumberOfViolationsHigh: int?,

    OFACPenalty: [string, string...],

    AggregatePenalty: [string, string...],

    Industry: [string, string...],

    VoluntaryDisclosure: [{1}, {0}, {-1}], //1=yes, 2=no, -1=Not Stated}

    EgregiousCase: [{1}, {0}, {-1}], //1=yes, 2=no, -1=Not Stated},

    KeyWords: string,

    ExcludeCommentaries: boolean //when true only documenttext is searched, not commentary

}

 

### Examples ###

 

User: give me all documents that contain the words "global distribution system"

Assistant: {

    "DateIssuedBegin": null,

    "DateIssuedEnd": null,

    "LegalIssue": [],

    "Program": [],

    "DocumentType": [],

    "RegulatoryProvision": [],

    "Published": null,

    "EnforcementCharacterization": [],

    "NumberOfViolationsLow": null,

    "NumberOfViolationsHigh": null,

    "OFACPenalty": [],

    "AggregatePenalty": [],

    "Industry": [],

    "RespondentNationality": [],

    "VoluntaryDisclosure": [],

    "EgregiousCase": [],

    "KeyWords": "\"global distribution system\"",

    "ExcludeCommentaries": false

}

 

User: give me all documents that contain the words "global distribution system" (but not if the term appears only in the commentary section)

Assistant: {

    "DateIssuedBegin": null,

    "DateIssuedEnd": null,

    "LegalIssue": [],

    "Program": [],

    "DocumentType": [],

    "RegulatoryProvision": [],

    "Published": null,

    "EnforcementCharacterization": [],

    "NumberOfViolationsLow": null,

    "NumberOfViolationsHigh": null,

    "OFACPenalty": [],

    "AggregatePenalty": [],

    "Industry": [],

    "VoluntaryDisclosure": [],

    "EgregiousCase": [],

    "KeyWords": "\"global distribution system\"",

    "ExcludeCommentaries": true

}

 

User: give me all OFAC FAQs that contain the name "deripaska"

Assistant: {

    "DateIssuedBegin": null,

    "DateIssuedEnd": null,

    "LegalIssue": [],

    "Program": [],

    "DocumentType": ["OFAC FAQs"],

    "RegulatoryProvision": [],

    "Published": null,

    "EnforcementCharacterization": [],

    "NumberOfViolationsLow": null,

    "NumberOfViolationsHigh": null,

    "OFACPenalty": [],

    "AggregatePenalty": [],

    "Industry": [],

    "VoluntaryDisclosure": [],

    "EgregiousCase": [],

    "KeyWords": "deripaska",

    "ExcludeCommentaries": false

}

 

User: give me all items that relate to section 515.204 of the CACR

Assistant: {

    "DateIssuedBegin": null,

    "DateIssuedEnd": null,

    "LegalIssue": [],

    "Program": [],

    "DocumentType": [],

    "RegulatoryProvision": ["515.204"],

    "Published": null,

    "EnforcementCharacterization": [],

    "NumberOfViolationsLow": null,

    "NumberOfViolationsHigh": null,

    "OFACPenalty": [],

    "AggregatePenalty": [],

    "Industry": [],

    "VoluntaryDisclosure": [],

    "EgregiousCase": [],

    "KeyWords": "",

    "ExcludeCommentaries": false

}

 

User: give me a list of all ofac enforcment actions from 2024

Assistant: {

    "DateIssuedBegin": 2024,

    "DateIssuedEnd": 2024,

    "LegalIssue": [],

    "Program": [],

    "DocumentType": ["Enforcement Releases", "OFAC Settlement Agreements"],

    "RegulatoryProvision": [],

    "Published": null,

    "EnforcementCharacterization": [],

    "NumberOfViolationsLow": null,

    "NumberOfViolationsHigh": null,

    "OFACPenalty": [],

    "AggregatePenalty": [],

    "Industry": [],

    "VoluntaryDisclosure": [],

    "EgregiousCase": [],

    "KeyWords": "",

    "ExcludeCommentaries": false

}




"""

advanced_doc_search_prompt = """
Review the provided documents and commentary to answer the user's question.

### Guidance ###

1. From the list of provided documents, list out which are relevant to the user's question.
2. For each relevant document, explain how it addresses the user's question. Make sure to cite the document title and put the title in brackets. Always refer to the documents by [title], not by number.
3. Commentary may also be relevant to the user's question. If so, explain how it addresses the user's question.
4. If there is no relevant information in the documents or commentary, say that you couldn't find any relevant information to answer the question. Under no circumstances should you answer with anything outside of the context of the search results. This is a legal search engine AI, accuracy is paramount. Do not make assumptions, inferences, or fabricate information.
5. If a document is only partially relevant, specify which parts are relevant and which are not.
6. Do not use any external knowledge or prior training; only use the provided search results.
7. Do not repeat the user's question in your answer.

### Output Format ###

- Always begin your answer stating which documents you're referencing (e.g., "According to [Document Title]...").
- When referencing information, clearly indicate which document it came from.
- Use the document titles provided in the TITLE sections to identify sources.
- If information comes from multiple documents, mention all relevant sources.
- Be specific about which document contains which information.
- Summarize the expert commentary at the end if relevant to the user's question.
- Use bullet points for clarity where appropriate.
- If the answer is unclear or incomplete, suggest what additional information would be needed to provide a definitive answer.

### Examples ###

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

question_classification_prompt = """

 

You are given a user question. Your job is to classify the question into one of the following categories:

 

1. Basic keyword search and/or filters

2. Advanced document search

3. Aggregation query

 

### Guidance ###

 

### Examples ###




"""

question_classification_prompt = """

You are given a user question. Your job is to classify the question into one of the following categories:

1. Basic keyword search and/or filters
2. Advanced document search
3. Aggregation query

### Guidance ###


### Examples ###



"""
