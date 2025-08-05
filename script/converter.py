import xml.etree.ElementTree as ET
import json
import re

def parse_nessus_to_json(nessus_file,json_file):
    output_json_file=json_file
    try:
        tree = ET.parse(nessus_file)
        root = tree.getroot()

        report_data = []
        host_ip_vect = []
        value = 1
        for report_host in root.findall(".//ReportHost"):
            host_ip = report_host.attrib.get("name", "unknown")
            if host_ip not in host_ip_vect:
                host_ip_vect.append(host_ip)

            for report_item in report_host.findall("ReportItem"):
                cves = [cve.text for cve in report_item.findall("cve")]

                risk_factor = report_item.findtext("risk_factor")
                if risk_factor is None or risk_factor.strip() == "" or risk_factor.strip() == "None" :
                    risk_factor = "Info"


                description = re.sub(r"\s+", " ", report_item.findtext("description", default="")).strip()
                solution= re.sub(r"\s+", " ", report_item.findtext("solution", default="")).strip()

                item = {
                    "id": value,
                    "host": host_ip,
                    "port": report_item.attrib.get("port"),
                    "protocol": report_item.attrib.get("protocol"),
                    "svc_name": report_item.attrib.get("svc_name"),
                    "plugin_name": report_item.attrib.get("pluginName"),
                    "plugin_id": report_item.attrib.get("pluginID"),
                    "severity": report_item.attrib.get("severity"),
                    "exploit_available": report_item.findtext("exploit_available", default=""),
                    "exploitability_ease": report_item.findtext("exploitability_ease", default=""),
                    "description": description,
                    "solution": "" if (solution == "n/a")  else solution,
                    "risk_factor": risk_factor,
                    "cve_list": "" if cves == [] else cves,
                    "cwe": report_item.findtext("cwe", default=""),
                    "cvss3_base_score": report_item.findtext("cvss3_base_score", default=""),
                    "cvss3_vector": report_item.findtext("cvss3_vector", default=""),
                    "cvss3_temporal_score": report_item.findtext("cvss3_temporal_score", default=""),
                    "cvss3_temporal_vector": report_item.findtext("cvss3_temporal_vector", default=""),
                    "cvss2_base_score": report_item.findtext("cvss_base_score", default=""),
                    "cvss2_vector": report_item.findtext("cvss_vector", default=""),
                    "cvss2_temporal_score": report_item.findtext("cvss_temporal_score", default=""),
                    "cvss2_temporal_vector": report_item.findtext("cvss_temporal_vector", default="")
                }


                value += 1


                report_data.append(item)

        with open(output_json_file, "w") as f:
            json.dump(report_data, f, indent=4)

        print(f"[✓] 1. Report JSON generato: {output_json_file}")
        return host_ip_vect
    except Exception as e:
        print(f"[ERRORE] {e}")


