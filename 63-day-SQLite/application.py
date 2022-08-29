from flask import Flask, render_template, request, redirect, url_for
from flask_bootstrap import Bootstrap5
from myform import BookForm
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SECRET_KEY"] = "8BYkEfBA6O6donzWlSihBXox7C0sKR6b"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///new-books-collection.db"

db = SQLAlchemy(app)
bootstrap = Bootstrap5(app)

class Book(db.Model):
    id  = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True,nullable=False)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False)

    def __repr__(self) -> str:
        return f"<Book: {self.title}>"

@app.route("/")
def home():
    all_books = Book.query.all()
    return render_template("index.html",book_list=all_books)


@app.route("/add", methods=["POST", "GET"])
def add():
    form = BookForm()
    if request.method == "POST" and form.validate_on_submit():
        book_entry = Book(title=form.book_name.data,author=form.author.data,rating=form.rating.data)
        db.session.add(book_entry)
        db.session.commit()
        return redirect(url_for("home"))
    return render_template("add.html", form=form)

