from flask import Flask, render_template, request, jsonify, send_file

from backend.chat import *
from backend.generate_resume import *
from backend.generate_openai_description import *

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

@app.get("/generate_openai_description")
def generate_openai_description():
    data = request.get_json()
    user_description = data.get("user_description")
    openai_description = generate_openai_description(user_description)
    return jsonify({"openai_description": openai_description})

if __name__ == "__main__":
    app.run(debug=False)