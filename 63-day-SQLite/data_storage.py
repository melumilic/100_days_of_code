from enum import unique
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///new-books-collection.db'
db = SQLAlchemy(app)



# db.create_all()

# new_book = Book(id=1, title="Harry Potter", author="J. K. Rowling", rating=9.3)
# db.session.add(new_book)
# db.session.commit()

# import sqlite3

# db = sqlite3.connect("books-collection.db")

# cursor = db.cursor()

# # cursor.execute(
# #     "CREATE TABLE books ("\
# #     "id INTEGER PRIMARY KEY,"\
# #     "title varchar(250) NOT NULL UNIQUE,"\
# #     "author varchar(250) NOT NULL,"\
# #     "rating FLOAT NOT NULL)"
# # )
# cursor.execute("INSERT INTO books VALUES(1, 'Harry Potter', 'J. K. Rowling', '9.3')")
# db.commit()