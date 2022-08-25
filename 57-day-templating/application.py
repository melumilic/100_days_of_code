from curses import napms
from flask import Flask
from flask import render_template
import datetime
import requests
import json

app = Flask(__name__)


@app.route("/")
def home():
    cur_year = datetime.datetime.now().strftime("%Y")
    return render_template("index.html", cur_year=cur_year)


@app.route("/guess/<name>")
def guess(name):
    params_value = {"name":name}
    response = requests.get(url=f"https://api.agify.io/",params=params_value)
    age_json = response.json()
    response = requests.get(url=f"https://api.genderize.io/",params=params_value)
    gender_json = response.json()
    return render_template(
        "guess.html",
        gender_guess=gender_json["gender"],
        age_guess=age_json["age"],
        person_name=name
    )

@app.route("/blog/<num>")
def get_blog(num):
    print(num)
    response = requests.get("https://api.npoint.io/c790b4d5cab58020d391")
    blog_data = response.json()
    return render_template("blog.html",posts=blog_data)