import json
from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql.expression import func, select
import random
app = Flask(__name__)

##Connect to Database
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///cafes.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

##Cafe TABLE Configuration
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)

    def to_dict(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}

@app.route("/")
def home():
    return render_template("index.html")


## HTTP GET - Read Record
@app.route("/random", methods=["GET"])
def random_cafe():
    random_cafe = db.session.query(Cafe).order_by(func.random()).first()
    # cafes = db.session.query(Cafe).all()
    # random_cafe = random.choice(cafes)
    # return jsonify(cafe={
    #     "name":random_cafe.name,
    #     "map_url":random_cafe.map_url,
    #     "img_url":random_cafe.img_url,
    #     "location":random_cafe.location,
    #     "seats":random_cafe.seats,
    #     "amenities":{
    #         "has_toilet":random_cafe.has_toilet,
    #         "has_wifi":random_cafe.has_wifi,
    #         "has_sockets":random_cafe.has_sockets,
    #         "can_take_calls":random_cafe.can_take_calls,
    #         "coffee_price":random_cafe.coffee_price
    #     }
    # })
    return jsonify(cafe=random_cafe.to_dict())

@app.route("/all",methods=["GET"])
def all_cafes():
    cafe_query_list = db.session.query(Cafe).all()
    cafe_list = [row.to_dict() for row in cafe_query_list]
    return jsonify(cafes=cafe_list)
## HTTP POST - Create Record

## HTTP PUT/PATCH - Update Record

## HTTP DELETE - Delete Record


if __name__ == "__main__":
    app.run(debug=True)
