from flask import Flask, render_template, request
from my_form import MyForm

app = Flask(__name__)

app.secret_key = "secret_key"


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/login", methods=["POST", "GET"])
def login():
    form = MyForm()
    if request.method == "POST" and form.validate_on_submit():
        if form.password.data == str(12345678) and form.email.data == "admin@email.com":
            return render_template("success.html")
        return render_template("denied.html")
    else:
        return render_template("login.html", form=form)
    return render_template("login.html", form=form)
