from crypt import methods
from flask import Flask, render_template, request, redirect, url_for
from flask_bootstrap import Bootstrap5
from myform import BookForm


app = Flask(__name__)
app.config["SECRET_KEY"] = "8BYkEfBA6O6donzWlSihBXox7C0sKR6b"

bootstrap = Bootstrap5(app)

all_books = []


@app.route('/')
def home():
    return render_template("index.html")


@app.route("/add", methods=["POST","GET"])
def add():
    form = BookForm()
    if request.method=="POST" and form.validate_on_submit():
        pass
    return render_template("add.html",form=form)


if __name__ == "__main__":
    app.run(debug=True)

