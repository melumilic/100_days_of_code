from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/login", methods=["POST", "GET"])
def login():
    error = None
    if request.method == "POST":
        return request.form["email"]
    return "not implemented"
