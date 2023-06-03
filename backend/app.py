from flask import Flask, render_template, request, jsonify

from chat import getResponse

app = Flask(__name__)

@app.get("/")
def index():
    return render_template("../frontend/index.html")

@app.post("/predict")
def predict():
    txt = request.get_json().get("message")
    response = getresponse(txt)
    return jsonify({"answer": response})

if __name__ == "__main__":
    app.run(debug=True)