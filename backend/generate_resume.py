from jinja2 import Environment, FileSystemLoader
import json
import pdfkit

def generate_resume(data):
    resume_data = json.loads(data)
    env = Environment(loader=FileSystemLoader('../templates'))
    template = env.get_template('resume_template.html')
    rendered_html = template.render(resume=resume_data['resume'])
    pdf_path = "../generated_files/resume.pdf"
    pdfkit.from_string(rendered_html, pdf_path)
    return pdf_path
