import subprocess

#Codice funziona su kali impostando Metasploitable 2 rete con Nat Corso (10.0.2.4)
#Codice non funziona in locale impostando Metasploitable 2 scheda con bridge (192.158.1.xxx)

def nmap_scan(addr):
    xml_file = "data/myscan2.xml"

    ip_str = ', '.join(addr)

    command = ["nmap", "-sV", "-p-", "-oX", xml_file, ip_str]

    print(command)

    try:
        print(f"Eseguendo: {' '.join(command)}")
        subprocess.run(command, capture_output=True, text=True)
        print(f"[✓] xxx. Il processo nmap è terminato con successo!")
    except Exception as e:
        print(f"[ERRORE] Errore durante l'esecuzione del comando Nmap: {e}")

