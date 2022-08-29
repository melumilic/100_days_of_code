from flask import Flask, render_template, redirect, url_for, request
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap5
from my_forms import AddMovie, UpdateMovie
import requests

app = Flask(__name__)
app.config["SECRET_KEY"] = "8BYkEfBA6O6donzWlSihBXox7C0sKR6b"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///top-movies-collection.db"

db = SQLAlchemy(app)

bootstrap = Bootstrap5(app)


class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    year = db.Column(db.String(4), nullable=False)
    description = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False)
    ranking = db.Column(db.Integer, nullable=False)
    review = db.Column(db.String(250), nullable=False)
    img_url = db.Column(db.String(250), nullable=False)

    def __repr__(self) -> str:
        return f"<Movie: { self.title }"


# db.create_all()


@app.route("/")
def home():
    return render_template(
        "index.html", movies=Movie.query.order_by(Movie.ranking).limit(10).all()
    )


@app.route("/add", methods=["POST", "GET"])
def add():
    form = AddMovie()
    if request.method == "POST" and form.validate_on_submit():
        movie_entry = Movie(
            title=form.title.data,
            year=form.year.data,
            description=form.description.data,
            rating=form.rating.data,
            ranking=form.ranking.data,
            review=form.review.data,
            img_url=form.img_url.data,
        )
        db.session.add(movie_entry)
        db.session.commit()
        return redirect(url_for("home"))
    return render_template("add.html", form=form)

@app.route("/update/<entry_id>",methods=["POST","GET"])
def update(entry_id):
    form = UpdateMovie()
    entry = Movie.query.get(entry_id)
    if request.method=="POST" and form.validate_on_submit():
        if form.title.data != "":
            entry.title = form.title.data
        if form.year.data != "":
            entry.year = form.year.data
        if form.description.data != "":
            entry.description = form.description.data
        if form.rating.data is not None:
            entry.rating = form.rating.data
        if form.ranking.data is not None:
            entry.ranking = form.ranking.data
        if form.review.data != "":
            entry.review = form.review.data
        if form.img_url.data != "":
            entry.img_url = form.img_url.data
        db.session.commit()
        return redirect(url_for("home"))
    elif request.method=="GET":
        return render_template("edit.html",form=form,update_id=entry_id)
    return render_template("edit.html",form=form,update_id=entry_id)



@app.route("/delete/<entry_id>")
def delete(entry_id):
    entry_to_delete = Movie.query.get(entry_id)
    db.session.delete(entry_to_delete)
    db.session.commit()
    return redirect(url_for("home"))