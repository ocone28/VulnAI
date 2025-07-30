
# script che prendendo vulnerabilita protocollo e versione mi dia il cve associato con il relativo cvss
#devo gestire i seguenti casi
# Caso 1(facile): ho CVE ma non ho il cvss poss. soluzione: faccio una chiamata a cve.org/NVD e mi faccio ritornare cvss associata a quel CVE.
# Caso 2(medio): ho cvss ma non ho alcun CVE opzioni: 1) ignoro 2) chiedo all'llm data quella vuln che CVE ha associata.
# Caso 3(difficle): non ho ne cvss ne CVE soluzione: dall'llm mi faccio dire che cve è associato a quella vuln con il suo rispettivo cvss. (in caso piu di uno prendo quello con cvss piu alto)




#

def add_info_vunerability():
    print("ciao")