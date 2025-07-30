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

    #1 converter file -> converter.py
    hostip=parse_nessus_to_json("data/scan.nessus")

    #xxx filtro per prendere poche vulnerabilita
    filtered_vulnerability("severity","4")


    # script nmap
    #nmap_scan(hostip)

    #aggiunegere le informazioni di nmap a oggetti filtrati
    #add_nmap_info()

    #2 attack scenarious -> finding_context_enhancer.py
    #attack_scenarious()

    #TODO
    #add_info_vunerability()

    #3 exploitability e risk priotitizer -> exploitability_riskprioritizer.py
    #exploitability_riskprioritizer()

    #4 remediation -> remediation_recommendation_generator.py
    #remediation_generator()

    #5 generate json -> generate_json_complete.py
    #generate_json_complete()

    #6 generate report -> report.py TODO-> aggiornare il report con informazioni aggiuntive es versione del protocollo
    #generate_report_pdf()

    print(f"[✓] 7. L'intero processo è terminato con successo!")


