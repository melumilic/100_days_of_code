from pprint import pprint
from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import pandas as pd

app = Flask(__name__)
app.config["SECRET_KEY"] = "8BYkEfBA6O6donzWlSihBXox7C0sKR6b"


class CafeForm(FlaskForm):
    cafe = StringField("Cafe name", validators=[DataRequired()])
    submit = SubmitField("Submit")


# Exercise:
# add: Location URL, open time, closing time, coffee rating, wifi rating, power outlet rating fields
# make coffee/wifi/power a select element with choice of 0 to 5.
# e.g. You could use emojis ☕️/💪/✘/🔌
# make all fields required except submit
# use a validator to check that the URL field has a URL entered.
# ---------------------------------------------------------------------------


# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")


@app.route("/add")
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        print("True")
    # Exercise:
    # Make the form write a new row into cafe-data.csv
    # with   if form.validate_on_submit()
    return render_template("add.html", form=form)


@app.route("/cafes")
def cafes():
    coffee_df = pd.read_csv("cafe-data.csv")
    # coffee_df.style.hide(axis="index")
    # lazy way to create a table
    # {{ cafes.to_html(classes="table-dark")|safe }}
    a = coffee_df.columns.values.tolist()
    coffee_list = coffee_df.values.tolist()
    coffee_list.insert(0,a)
    print(coffee_list)
    # can get length of list with array_name|length
    return render_template("cafes.html", cafes=coffee_list)


if __name__ == "__main__":
    app.run(debug=True)
