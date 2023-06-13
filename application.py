from flask import Flask, render_template, request, jsonify, send_file
from flask_cors import CORS
from backend.chat import getResponse

application = Flask(__name__, template_folder='templates', static_url_path='/static')
CORS(application)
application.debug = True

@application.route("/", methods=['GET'])
def index():
    return render_template("index.html")

@application.route("/predict", methods=['POST'])
def predict():
    txt = request.get_json().get("message")
    response = getResponse(txt)
    return jsonify({"answer": response})

if __name__ == "__main__":
    application.run()
