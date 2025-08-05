from script.converter import parse_nessus_to_json
from script.finding_context_enhancer import attack_scenarious
from script.exploitability_riskprioritizer import exploitability_riskprioritizer
from script.remediation_recommendation_generator import remediation_generator
from script.report import generate_report_pdf
from script.filtered_vulnerability import filtered_vulnerability
from script.add_info_nmap import add_nmap_info
from script.nmap_scan import nmap_scan
from script.add_info_vuln import add_info_vunerability

if __name__ == '__main__':
    file_nessus="data/scan.nessus"
    file = "data/scan_results.json"
    json_file="data/scan_results_prova.json" #da sostituire con scan_results_filtered.json

    #1 converter file -> converter.py
    #hostip=parse_nessus_to_json(file_nessus,file)

    #xxx filtro per prendere poche vulnerabilita
    #filtered_vulnerability("severity","4",file,json_file)

    # script nmap
    #nmap_scan(hostip)

    #aggiunegere le informazioni di nmap a oggetti filtrati
    #add_nmap_info(json_file)

    #2 attack scenarious -> finding_context_enhancer.py
    #attack_scenarious(json_file)


    #add_info_vunerability(json_file)

    #3 exploitability e risk priotitizer -> exploitability_riskprioritizer.py
    #exploitability_riskprioritizer(json_file)

    #4 remediation -> remediation_recommendation_generator.py
    #remediation_generator(json_file)

    #6 generate report -> report.py TODO-> aggiornare il report con informazioni aggiuntive es versione del protocollo
    generate_report_pdf(json_file)

    print(f"[✓] 7. L'intero processo è terminato con successo!")


