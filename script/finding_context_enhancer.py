#Use LLMs to add threat context and business impact analysis
import json
from script.llm import query_llm
from tqdm import tqdm
import time

def attack_scenarious():
    json_file= "data/scan_results_filtered.json"

    # Carica il file
    with open(json_file, "r") as f:
        data = json.load(f)


    i = 0  # ad esempio, riprendi dal quarto elemento
    fine = len(data)
    time.sleep(0.5)
    for idx in tqdm(range(i, fine), desc="Elaborazione possibili scenari attacco:", leave=True):
        entry=data[idx]

        # Esempio: stampa plugin_name e host per ciascuno

        prompt = f"Vulnerability: {entry.get("description", "N/A")}.\nProvide a 3-sentence analysis of potential real-world attack scenarios and business risks"

        entry["attack_scenarious"] = query_llm(prompt)

    with open(json_file, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

    tqdm.write(f"[✓] 2. Attack scenarios generati correttamente. File JSON: {json_file}")
