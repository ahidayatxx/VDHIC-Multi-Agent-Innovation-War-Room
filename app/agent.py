# ruff: noqa
import datetime
import os
from typing import Dict, Any, List

# Explicitly disable Vertex AI ADC mode so google.genai uses API key mode
os.environ["GOOGLE_GENAI_USE_VERTEXAI"] = "0"

api_key = os.environ.get("GEMINI_API_KEY") or os.environ.get("GOOGLE_API_KEY")
if api_key:
    os.environ["GOOGLE_API_KEY"] = api_key
    os.environ["GEMINI_API_KEY"] = api_key

from google.adk.agents import Agent
from google.adk.apps import App
from google.adk.models import Gemini

# Dynamic Model Selection: Z.AI / GLM (LiteLlm) vs Gemini
ZAI_KEY = os.environ.get("ZAI_API_KEY") or os.environ.get("GLM_API_KEY")
ZAI_BASE_URL = os.environ.get("ZAI_BASE_URL", "https://api.z.ai/api/coding/paas/v4")
ZAI_MODEL = os.environ.get("ZAI_MODEL", "glm-5.2")

if ZAI_KEY:
    os.environ["OPENAI_API_KEY"] = ZAI_KEY
    os.environ["OPENAI_API_BASE"] = ZAI_BASE_URL
    from google.adk.models.lite_llm import LiteLlm
    model_obj = LiteLlm(
        model=f"openai/{ZAI_MODEL}",
        api_key=ZAI_KEY,
        api_base=ZAI_BASE_URL,
    )
else:
    MODEL = os.environ.get("ADK_MODEL", "gemini-2.5-flash")
    model_obj = Gemini(model=MODEL)


# --- 1. VDHIC Lookup Tools ---

def kemenkes_regulatory_lookup(query: str) -> str:
    """Lookup Indonesian Kemenkes Regulatory Sandbox rules, SaMD risk levels, and UU PDP data governance.

    Args:
        query: Specific regulatory topic or device type (e.g. 'SaMD risk class', 'sandbox application', 'UU PDP localization').

    Returns:
        Authoritative guidance summary from Kemenkes & BPOM regulations.
    """
    query_lower = query.lower()
    if "samd" in query_lower or "device" in query_lower or "risk" in query_lower:
        return (
            "Kemenkes & BPOM SaMD Risk Classification (Block 10):\n"
            "- Class I (Low Risk): Non-invasive wellness & administrative tools.\n"
            "- Class IIa (Moderate-Low): Clinical decision support (CDS) with physician oversight.\n"
            "- Class IIb/III (High Risk): Autonomous AI diagnostics, triage, or direct therapy recommendation.\n"
            "Standards: ISO 13485 (QMS), IEC 62304 (Medical Software Lifecycle), ISO 14971 (Risk Management).\n"
            "Regulatory Sandbox: Pre-market testing pathway under Permenkes Regulatory Sandbox."
        )
    elif "pdp" in query_lower or "data" in query_lower or "privacy" in query_lower or "localization" in query_lower:
        return (
            "Indonesia Data Protection & Governance (Block 12 - UU PDP No. 27/2022):\n"
            "- Data Residency: Health data of Indonesian citizens must be hosted on local servers within Indonesia.\n"
            "- Consent: Explicit informed consent required prior to processing personal health data.\n"
            "- Encryption: AES-256 at rest, TLS 1.3 in transit.\n"
            "- Data Retention & Deletion: Retention per Kemenkes medical record regulations; right to erasure supported."
        )
    else:
        return (
            "Kemenkes Regulatory Overview:\n"
            "All digital health interventions must align with Renstra Kemenkes.\n"
            "Submissions to the Kemenkes Regulatory Sandbox require proof of clinical safety protocols and data security audit."
        )


def satusehat_fhir_lookup(query: str) -> str:
    """Lookup SATUSEHAT FHIR R4 profile specifications and mandatory coding dictionaries in Indonesia.

    Args:
        query: Specific FHIR resource or terminology standard (e.g. 'Encounter', 'Observation', 'ICD-10', 'LOINC', 'SNOMED CT', 'KFA').

    Returns:
        Technical interoperability specifications for SATUSEHAT integration.
    """
    query_lower = query.lower()
    if "fhir" in query_lower or "resource" in query_lower or "encounter" in query_lower:
        return (
            "SATUSEHAT FHIR R4 Profile Requirements (Block 6):\n"
            "- Core Resources: Patient, Practitioner, Organization, Location, Encounter, Condition, Observation, DiagnosticReport, MedicationRequest.\n"
            "- API Gateway: OAuth2 / TLS 1.3 token authentication via SATUSEHAT Developer Portal.\n"
            "- Real-time vs Batch: Encounter and Condition synchronized in real-time; batch sync supported for telemetry."
        )
    elif "icd" in query_lower or "loinc" in query_lower or "snomed" in query_lower or "kfa" in query_lower or "terminology" in query_lower:
        return (
            "Indonesian Semantic Terminology Standards (Block 6):\n"
            "- Diagnosis: ICD-10 (International Classification of Diseases, 10th Revision).\n"
            "- Laboratory / Diagnostics: LOINC (Logical Observation Identifiers Names and Codes).\n"
            "- Clinical Concepts / Anatomy: SNOMED CT.\n"
            "- Medications: KFA (Kamus Farmasi dan Alat Kesehatan - Kemenkes National Drug Dictionary)."
        )
    else:
        return (
            "SATUSEHAT Interoperability Overview:\n"
            "Requires RESTful API integration using HL7 FHIR R4 standards.\n"
            "Interoperability must cover SIMRS (Hospital Information Systems) and PCare (Primary Care Systems)."
        )


def bpjs_reimbursement_lookup(query: str) -> str:
    """Lookup BPJS Kesehatan INA-CBGs tariff inclusion standards and primary care Kapitasi incentive frameworks in Indonesia.

    Args:
        query: Specific reimbursement mechanism or funding model (e.g. 'INA-CBGs', 'Kapitasi', 'B2B hospital', 'out of pocket').

    Returns:
        Health economic & reimbursement pathway guidance.
    """
    query_lower = query.lower()
    if "cbg" in query_lower or "ina-cbg" in query_lower or "hospital" in query_lower:
        return (
            "BPJS Kesehatan INA-CBGs Hospital Tariff Inclusion (Block 9):\n"
            "- Digital health interventions in secondary/tertiary hospitals are bundled into existing INA-CBGs case-based tariff groups.\n"
            "- Cost Reduction Value: Must prove reduction in Length of Stay (LOS) or re-admission rates to justify hospital ROI."
        )
    elif "kapitasi" in query_lower or "puskesmas" in query_lower or "primary" in query_lower:
        return (
            "Puskesmas Kapitasi & KBK Performance Incentive (Block 9):\n"
            "- Primary health centers operate on a per-capita monthly budget (Kapitasi).\n"
            "- KBK (Komitmen Pelayanan Kapitasi): Solutions driving chronic disease monitoring (Prolanis) earn performance bonus tariffs."
        )
    else:
        return (
            "Indonesian Healthcare Business Model Landscape (Block 9):\n"
            "- B2B: Direct SaaS subscription to private hospital chains (RS Swasta).\n"
            "- B2G: Kemenkes / Dinas Kesehatan APBD/APBN procurement for public health programs.\n"
            "- B2C: Patient out-of-pocket payment or corporate employee wellness packages."
        )


# --- 2. Specialist Sub-Agents ---

regulatory_specialist = Agent(
    name="regulatory_specialist",
    model=model_obj,
    instruction=(
        "You are the Regulatory & Data Protection Specialist for the VDHIC v1.25 Innovation War Room.\n"
        "Your focus is Governance Spine (Block 10: Medical Device / SaMD Classification, ISO 13485/IEC 62304, Kemenkes Regulatory Sandbox) "
        "and Data Governance (Block 12: UU PDP No. 27/2022, local data hosting in Indonesia, consent, encryption).\n"
        "Analyze proposals strictly against Indonesian health regulations and data protection laws. Use `kemenkes_regulatory_lookup` when needed."
    ),
    tools=[kemenkes_regulatory_lookup],
)

interop_specialist = Agent(
    name="interop_specialist",
    model=model_obj,
    instruction=(
        "You are the Interoperability & Tech Architect Specialist for the VDHIC v1.25 Innovation War Room.\n"
        "Your focus is Design Phase (Block 6: Enterprise Interoperability, SATUSEHAT FHIR R4, SIMRS/PCare integration, ICD-10/LOINC/SNOMED CT/KFA terminologies) "
        "and Tech Governance (Block 13: Cybersecurity, ISO 27001, API Gateways, DR/BC, SLAs).\n"
        "Provide concrete technical integration guidance. Use `satusehat_fhir_lookup` when needed."
    ),
    tools=[satusehat_fhir_lookup],
)

clinical_specialist = Agent(
    name="clinical_specialist",
    model=model_obj,
    instruction=(
        "You are the Clinical & Evidence Lead Specialist for the VDHIC v1.25 Innovation War Room.\n"
        "Your focus is Discover Phase (Block 1: Health Challenge & Clinical Burden), Deliver Phase (Block 7: Evidence Plan - Feasibility Pilot -> RCT -> RWE), "
        "Clinical Governance (Block 11: Safety protocols & risk mitigation), and Quintuple Aim dimensions (Population Health, Patient Experience, Provider Satisfaction).\n"
        "Evaluate clinical efficacy, safety protocols, and evidence generation roadmaps."
    ),
    tools=[],
)

economics_specialist = Agent(
    name="economics_specialist",
    model=model_obj,
    instruction=(
        "You are the Health Economics & Scale Lead Specialist for the VDHIC v1.25 Innovation War Room.\n"
        "Your focus is Deliver Phase (Block 8: Scale Strategy & Go-To-Market, Block 9: Business Model - BPJS INA-CBGs, Puskesmas Kapitasi, unit economics) "
        "and Quintuple Aim dimensions (Cost Reduction, Health Equity).\n"
        "Evaluate commercial viability and health system financial sustainability. Use `bpjs_reimbursement_lookup` when needed."
    ),
    tools=[bpjs_reimbursement_lookup],
)

# --- 3. Root Coordinator Agent ---

root_agent = Agent(
    name="vdhic_warroom_agent",
    model=model_obj,
    instruction=(
        "You are the Lead VDHIC Innovation Coordinator chairing the Value-Based Digital Health Innovation Canvas (VDHIC v1.25) War Room.\n"
        "When an innovator submits a digital health project proposal or canvas draft, coordinate a multi-disciplinary review:\n"
        "1. Consult your specialist sub-agents (Regulatory, Interoperability, Clinical, Economics) to analyze the 4 Governance Spine blocks, 9 Phased blocks, and 5 Quintuple Aim dimensions.\n"
        "2. Synthesize their evaluation into a clear, professional VDHIC v1.25 Review Report with:\n"
        "   - Executive Summary & VDHIC Maturity Level (Concept, Validated, Implemented, Scaled).\n"
        "   - Key Strengths and Critical Compliance / Technical Gaps.\n"
        "   - Block-by-Block Evaluation Matrix.\n"
        "   - Actionable Kemenkes Sandbox, SATUSEHAT FHIR, and GTM Roadmap.\n"
        "Maintain a supportive, highly professional, evidence-anchored tone suited for digital health innovators and Kemenkes regulators."
    ),
    sub_agents=[regulatory_specialist, interop_specialist, clinical_specialist, economics_specialist],
)

app = App(
    root_agent=root_agent,
    name="app",
)
