from flask import Flask, jsonify
from flask.helpers import make_response

app = Flask(__name__)

@app.route("/")
def hello():
    r = make_response(jsonify({"message": "Hello My world!"}))
    r.mimetype = 'application/json'
    return r

