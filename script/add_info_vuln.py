import json
from script.llm import query_llm
from cvss import CVSS3
# script che prendendo vulnerabilita protocollo e versione mi dia il cve associato con il relativo cvss
#devo gestire i seguenti casi
# Caso 1(facile): ho CVE ma non ho il cvss poss. soluzione: faccio una chiamata a cve.org/NVD e mi faccio ritornare cvss associata a quel CVE.
# Caso 2(medio): ho cvss ma non ho alcun CVE opzioni: 1) ignoro 2) chiedo all'llm data quella vuln che CVE ha associata.
# Caso 3(difficle): non ho ne cvss ne CVE soluzione: dall'llm mi faccio dire che cve è associato a quella vuln con il suo rispettivo cvss. (in caso piu di uno prendo quello con cvss piu alto)




#
def add_cvss_llm(data):
    for entry in data:
        prompt = f"Given the following vulnerability description, generate only the CVSS v3 vector:\n\n{entry.get('description', 'N/A')}\n\nOutput: [CVSS vector only]"
        value= query_llm(prompt)
        entry["cvss3_llm_vector_by_description"] = value
        cvss = CVSS3(value)
        entry["cvss3_llm_base_score_by_description"] = str(cvss.scores()[0])

def from_cvss2_to_cvss3_with_llm(data):
    for entry in data:
        if entry.get("cvss2_vector") and not entry.get("cvss3_vector"):
            prompt = f"""Given the following CVSS v2 vector:{entry.get('cvss2_vector', 'N/A')}Convert it to an equivalent CVSS v3.0 vector.Output only the CVSS v3.0 base vector string (no explanation)."""
            value = query_llm(prompt)
            entry["cvss3_vector_by_cvss2_vector_with_llm"] = value
            cvss = CVSS3(value)
            entry["cvss3_base_score_by_cvss2_vector"] = str(cvss.scores()[0])

def average_cvss(data):
    for entry in data:
        values = []
        for key in [
            "cvss3_llm_base_score_by_description",
            "cvss3_base_score_by_cvss2_vector",
            "cvss2_base_score",
            "cvss3_base_score"
        ]:
            val = entry.get(key, "").strip()
            if val:
                try:
                    values.append(float(val))
                except ValueError:
                    continue
        if values:
            entry["cvss_average_score"] = round(sum(values) / len(values), 1)



def add_info_vunerability(file_json):
    json_file = file_json

    # Carica il file
    with open(json_file, "r") as f:
        data = json.load(f)

    add_cvss_llm(data)
    from_cvss2_to_cvss3_with_llm(data)
    average_cvss(data)

    with open(json_file, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
