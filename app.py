from flask import Flask, render_template, request, jsonify, send_file

from backend.chat import getResponse

app = Flask(__name__, template_folder='templates', static_url_path='/static')

@app.get("/")
def index():
    return render_template("index.html")

@app.post("/predict")
def predict():
    txt = request.get_json().get("message")
    response = getResponse(txt)
    return jsonify({"answer": response})

if __name__ == "__main__":
    app.run(debug=False)