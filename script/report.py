from socket import fromfd

from jinja2 import Environment, FileSystemLoader
from weasyprint import HTML
import json

def generate_report_pdf():

    env = Environment(loader=FileSystemLoader('templates'))
    template = env.get_template('report2.html')

    with open('data/scan_results_filtered.json', encoding='utf-8') as f:
        data = json.load(f)


    html_content = template.render(data=data)

    # Converte direttamente in PDF
    HTML(string=html_content).write_pdf("report/report.pdf")
    print(f"[✓] 6. PDF generato con successo con WeasyPrint!")



