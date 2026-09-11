# VDHIC Multi-Agent Innovation War Room 🏥🤖

> **Value-Based Digital Health Innovation Canvas (VDHIC v1.25) AI War Room**  
> Built with Google Agent Development Kit (ADK) and scaffolded via [google/agents-cli](https://github.com/google/agents-cli).

---

## 📌 Executive Overview

The **VDHIC Multi-Agent Innovation War Room** is an autonomous multi-disciplinary AI evaluation engine designed for digital health innovators, hospital systems, health tech startups, and regulatory bodies (such as Ministry of Health / Kemenkes RI). 

It automates the rigorous, multi-perspective evaluation of digital health proposals against the **Value-Based Digital Health Innovation Canvas (VDHIC v1.25)** framework, auditing 4 Governance Spine blocks, 9 Phased execution blocks, and the 5 Quintuple Aim healthcare value dimensions.

```
                      ┌──────────────────────────────────────────────────┐
                      │    VDHIC WAR ROOM LEAD INNOVATION COORDINATOR    │
                      │               (root_agent / GLM-5.2)             │
                      └────────────────────────┬─────────────────────────┘
                                               │
         ┌───────────────────┬─────────────────┴─────────────────┬───────────────────┐
         ▼                   ▼                                   ▼                   ▼
┌─────────────────┐ ┌─────────────────┐                 ┌─────────────────┐ ┌─────────────────┐
│   Regulatory    │ │ Interoperability│                 │    Clinical     │ │ Health Economics│
│   Specialist    │ │   Specialist    │                 │   Specialist    │ │   Specialist    │
│  (Block 10,12)  │ │  (Block 6, 13)  │                 │ (Block 1, 7, 11)│ │  (Block 8, 9)   │
└────────┬────────┘ └────────┬────────┘                 └────────┬────────┘ └────────┬────────┘
         │                   │                                   │                   │
         ▼                   ▼                                   ▼                   ▼
┌─────────────────┐ ┌─────────────────┐                 ┌─────────────────┐ ┌─────────────────┐
│ Kemenkes & BPOM │ │ SATUSEHAT FHIR  │                 │ Quintuple Aim   │ │ BPJS Reimburse  │
│ Sandbox Lookup  │ │  R4 & Coding    │                 │ Clinical Safety │ │ INA-CBGs & KBK  │
└─────────────────┘ └─────────────────┘                 └─────────────────┘ └─────────────────┘
```

---

## 🏛️ Multi-Agent Architecture

The War Room operates as a coordinated multi-agent system built on the Google Agent Development Kit (ADK) runtime:

### 1. Root Coordinator (`vdhic_warroom_agent`)
* Chairs the Innovation War Room.
* Receives raw digital health proposal submissions (JSON or text canvas drafts).
* Orchestrates cross-functional analysis by delegating sub-tasks to specialist sub-agents.
* Synthesizes individual specialist audits into an executive **VDHIC v1.25 Review Report** with maturity classification (`Concept`, `Validated`, `Implemented`, `Scaled`).

### 2. Specialist Sub-Agents
* ⚖️ **Regulatory & Data Protection Specialist (`regulatory_specialist`)**: Audits SaMD risk classification (Class I / IIa / IIb / III), ISO 13485/IEC 62304 standards, Kemenkes Regulatory Sandbox compliance, and Indonesia UU PDP No. 27/2022 data protection laws.
* 🔌 **Interoperability & Tech Architect Specialist (`interop_specialist`)**: Evaluates enterprise solution architecture, HL7 FHIR R4 profile mappings, SATUSEHAT integration, medical terminology standards (ICD-10, LOINC, SNOMED-CT, KFA), and ISO 27001 cybersecurity.
* 🩺 **Clinical & Evidence Lead Specialist (`clinical_specialist`)**: Assesses clinical burden, guidelines alignment (WHO/ADA/ACC), red-flag triage protocols, clinical audit criteria, and 3-stage evidence generation plans (Feasibility Pilot → RCT → RWE).
* 💰 **Health Economics & Scale Lead Specialist (`economics_specialist`)**: Evaluates commercial viability, scale strategy, GTM execution, and reimbursement pathways (BPJS Kesehatan INA-CBGs hospital tariff bundling & Puskesmas Kapitasi KBK performance incentives).

---

## 🧰 Domain Knowledge Tools

The War Room features built-in lookup tools tailored for the Indonesian and Asia-Pacific healthcare ecosystem:

1. **`kemenkes_regulatory_lookup(query)`**: Retrieves authoritative rules for Kemenkes RI Permenkes Regulatory Sandbox, SaMD risk levels, ISO 13485/IEC 62304/ISO 14971 standards, and UU PDP data localization laws.
2. **`satusehat_fhir_lookup(query)`**: Retrieves HL7 FHIR R4 resource specifications for SATUSEHAT integration, OAuth2 security requirements, and national terminology standards (ICD-10, LOINC, SNOMED-CT, KFA).
3. **`bpjs_reimbursement_lookup(query)`**: Provides health economics guidance on BPJS Kesehatan INA-CBGs hospital tariff bundling, Puskesmas Kapitasi & KBK performance incentives, and B2B/B2G market pathways.

---

## 🎯 VDHIC v1.25 Framework Alignment

The War Room systematically evaluates digital health innovations across all 17 VDHIC v1.25 canvas blocks:

```
┌────────────────────────────────────────────────────────────────────────────────────────┐
│                        VDHIC v1.25 CANVAS EVALUATION MATRIX                            │
├────────────────────────────────────────────────────────────────────────────────────────┤
│ 🟢 GOVERNANCE SPINE                                                                    │
│   • Block 10: Medical Device & SaMD Risk Classification (ISO 13485 / Sandbox)          │
│   • Block 11: Clinical Governance, Protocol Safety, & Guidelines (WHO / ADA / ACC)   │
│   • Block 12: Data Protection & Governance (UU PDP No. 27/2022 / Consent / Encryption) │
│   • Block 13: Tech Governance, Cybersecurity (ISO 27001), & Low-Bandwidth Resilience   │
├────────────────────────────────────────────────────────────────────────────────────────┤
│ 🔵 PHASED CANVAS BLOCKS                                                                │
│   • Discover Phase (Blocks 1-3): Health Challenge, Target Users, Key Stakeholders      │
│   • Design Phase   (Blocks 4-6): Solution Architecture, UX, SATUSEHAT Interoperability│
│   • Deliver Phase  (Blocks 7-9): Evidence Plan, Scale/GTM Strategy, Business Model     │
├────────────────────────────────────────────────────────────────────────────────────────┤
│ 🟣 QUINTUPLE AIM VALUE DIMENSIONS                                                      │
│   1. Health Equity         2. Population Health       3. Patient Experience        │
│   4. Provider Experience   5. Cost Reduction / Avoidance                               │
└────────────────────────────────────────────────────────────────────────────────────────┘
```

---

## 💻 Tech Stack & LLM Providers

* **Agent Framework**: Google Agent Development Kit (ADK)
* **CLI & Tooling**: [google/agents-cli](https://github.com/google/agents-cli) (v1.5.0+)
* **Primary LLM Provider**: **Z.AI / Zhipu GLM** (`glm-5.2`, `glm-5.3`, `glm-4.6`) via custom `ZaiLiteLlm` bridge.
* **Fallback LLM Provider**: **Google Gemini API** (`gemini-2.5-flash`).
* **Backend Runtime**: FastAPI / Uvicorn with A2A Protocol support (`/a2a/app`).
* **Deployment Target**: Coolify Self-Hosted VPS / Docker / Cloud Run.

---

## 📁 Directory Structure

```
VDHIC-Multi-Agent-Innovation-War-Room/
├── app/
│   ├── agent.py               # Core multi-agent definitions, tools, & ZaiLiteLlm bridge
│   ├── fast_api_app.py        # FastAPI server & A2A protocol routes
│   └── app_utils/             # A2A session & artifact services
├── docs/
│   ├── vdhic_canvas_v1.25.svg # Canvas reference architecture diagram
│   ├── vdhic_instruction_guide_v1.25.docx # Canvas instruction guide
│   └── vdhic_review_telemedicine_chronic_disease.md # Sample generated report
├── tests/
│   └── unit/
│       └── test_vdhic_agent.py# Pytest unit tests (4/4 passed)
├── .agents-cli-spec.md        # Architectural specification file
├── Dockerfile                 # Production container image configuration
├── pyproject.toml             # Python package & dependency setup
└── README.md                  # Project documentation
```

---

## 🚀 Local Quick Start

### 1. Prerequisites
Install `uv` package manager and `google-agents-cli`:

```bash
# Install uv
curl -LsSf https://astral.sh/uv/install.sh | sh

# Install google-agents-cli (https://github.com/google/agents-cli)
uv tool install google-agents-cli
```

### 2. Environment Configuration
Create a `.env` file in the project root:

```env
ZAI_API_KEY=your_zai_api_key_here
GLM_API_KEY=your_zai_api_key_here
OPENAI_API_KEY=your_zai_api_key_here
OPENAI_API_BASE=https://api.z.ai/api/coding/paas/v4
ZAI_BASE_URL=https://api.z.ai/api/coding/paas/v4
ZAI_MODEL=glm-5.2
ADK_MODEL=gemini-2.5-flash
PORT=8501
ALLOW_ORIGINS=*
```

### 3. Run Development Playground
Launch the local web playground server:

```bash
agents-cli playground
```
Access the interactive UI at: **`http://127.0.0.1:8080/dev-ui/?app=app`**

### 4. Run Unit Tests
Execute the unit test suite:

```bash
uv run pytest tests/unit/test_vdhic_agent.py
```

---

## 🌐 Production Deployment (Coolify VPS / Docker)

The War Room is optimized for self-hosted deployment on Coolify VPS or Docker:

```bash
# Build Docker image locally
docker build -t vdhic-warroom-agent .

# Run container
docker run -d -p 8501:8501 --env-file .env vdhic-warroom-agent
```

For Coolify VPS configuration, see `.agents-cli-spec.md`.

---

## 🤝 Credits & Acknowledgments

* Scaffolded and managed via [google/agents-cli](https://github.com/google/agents-cli).
* Built on [Google Agent Development Kit (ADK)](https://google.github.io/adk/).
* Designed around the **Value-Based Digital Health Innovation Canvas (VDHIC v1.25)** framework by Dr. Ahmad Hidayat.
