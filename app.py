from flask import Flask, render_template, request, jsonify, send_file

from backend.chat import getResponse
from backend.generate_resume import *

app = Flask(__name__, template_folder='templates', static_url_path='/static')

@app.get("/")
def index():
    return render_template("index.html")

@app.post("/predict")
def predict():
    txt = request.get_json().get("message")
    response = getResponse(txt)
    return jsonify({"answer": response})

@app.post("/generate_resume")
def generate_resume():
    data = request.get_json()
    pdfPath = generate_resume(data)
    return send_file(pdfPath, attachment_filename="resume.pdf", as_attachment=True)

if __name__ == "__main__":
    app.run(debug=False)