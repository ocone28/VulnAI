from jinja2 import Environment, FileSystemLoader
from weasyprint import HTML
import json


def generate_report_pdf(json_file):
    env = Environment(loader=FileSystemLoader('templates'))
    template = env.get_template('report3.html')

    with open(json_file, encoding='utf-8') as f:
        data = json.load(f)

    html_content = template.render(data=data)

    # Salva anche l'HTML per apertura in Chrome
    with open("report/report2.html", "w", encoding="utf-8") as f_html:
        f_html.write(html_content)

    # Converte in PDF
    HTML(string=html_content).write_pdf("report/report2.pdf")
    print(f"[✓] 6. PDF generato con successo con WeasyPrint!")
    print("[i] HTML salvato: apri 'report/report2.html' con Chrome.")



