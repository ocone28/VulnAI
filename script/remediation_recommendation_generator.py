import json
from script.llm import query_llm
from tqdm import tqdm
import time

def remediation_generator(file_json):
    json_file = file_json

    with open(json_file, "r") as f:
        data = json.load(f)


    i = 0  # ad esempio, riprendi dal quarto elemento
    fine = len(data)
    time.sleep(0.5)
    for idx in tqdm(range(i, fine), desc="Generazione mitigazioni vulnerabilità:", leave=True):
        entry = data[idx]
        prompt = f"""
            Generate step-by-step remediation for:
            Service: {entry.get("svc_name", "N/A")}
            Description Vulnerability: {entry.get("description_vulnerability", "N/A")}
            Port: {entry.get("port", "N/A")}
            CVE: {"Missing data" if (temp := entry.get("cve", "N/A")) == "" else temp}
            CVSS: {"Missing data" if (temp := entry.get("csvv", "N/A")) == "" else temp}
            """

        value = query_llm(prompt)


        entry["remediation"] = value


    with open(json_file, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

    tqdm.write(f"[✓] 4. Report JSON aggiornato: {json_file}")