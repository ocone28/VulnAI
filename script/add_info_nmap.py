import json
import xml.etree.ElementTree as ET

def add_nmap_info(file_json):
    # Step 1: Estrai 'product' e 'version' dal file XML
    xml_file = "data/myscan.xml"
    tree = ET.parse(xml_file)
    root = tree.getroot()

    service_info_map = {}

    for port in root.findall(".//port"):
        portid = port.get("portid")
        service = port.find("service")
        if service is not None:
            version = service.get("version", "Missing Data")
            product = service.get("product", "Missing Data")
            service_info_map[portid] = {
                "version": version,
                "product": product
            }

    # Step 2: Carica il file JSON e aggiorna i campi
    json_file = file_json

    with open(json_file, "r", encoding="utf-8") as f:
        dati = json.load(f)

    for item in dati:
        port = item.get("port")
        if port in service_info_map:
            item["version"] = service_info_map[port]["version"]
            item["product"] = service_info_map[port]["product"]

    # Step 3: Salva il file JSON aggiornato
    with open(json_file, "w", encoding="utf-8") as f:
        json.dump(dati, f, indent=4, ensure_ascii=False)


