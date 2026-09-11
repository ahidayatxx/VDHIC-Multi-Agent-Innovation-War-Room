import pytest
from app.agent import (
    kemenkes_regulatory_lookup,
    satusehat_fhir_lookup,
    bpjs_reimbursement_lookup,
    root_agent,
    regulatory_specialist,
    interop_specialist,
    clinical_specialist,
    economics_specialist,
)


def test_kemenkes_regulatory_lookup() -> None:
    samd_res = kemenkes_regulatory_lookup("SaMD risk classification")
    assert "SaMD Risk Classification" in samd_res
    assert "ISO 13485" in samd_res

    pdp_res = kemenkes_regulatory_lookup("UU PDP data localization")
    assert "UU PDP No. 27/2022" in pdp_res
    assert "Data Residency" in pdp_res


def test_satusehat_fhir_lookup() -> None:
    fhir_res = satusehat_fhir_lookup("FHIR R4 Observation resource")
    assert "SATUSEHAT FHIR R4" in fhir_res
    assert "Encounter" in fhir_res

    term_res = satusehat_fhir_lookup("ICD-10 LOINC SNOMED KFA terminology")
    assert "ICD-10" in term_res
    assert "SNOMED CT" in term_res
    assert "KFA" in term_res


def test_bpjs_reimbursement_lookup() -> None:
    cbg_res = bpjs_reimbursement_lookup("INA-CBGs hospital tariff")
    assert "INA-CBGs" in cbg_res

    kap_res = bpjs_reimbursement_lookup("Puskesmas Kapitasi KBK")
    assert "Kapitasi" in kap_res
    assert "KBK" in kap_res


def test_agent_structure() -> None:
    assert root_agent.name == "vdhic_warroom_agent"
    assert len(root_agent.sub_agents) == 4
    sub_agent_names = [sub.name for sub in root_agent.sub_agents]
    assert "regulatory_specialist" in sub_agent_names
    assert "interop_specialist" in sub_agent_names
    assert "clinical_specialist" in sub_agent_names
    assert "economics_specialist" in sub_agent_names
