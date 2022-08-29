from optparse import Option
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FloatField, IntegerField
from wtforms.validators import DataRequired, NumberRange, URL, Length, Optional


class AddMovie(FlaskForm):
    title = StringField(label="Title", validators=[DataRequired(),Length(max=250)])
    year = StringField(label="Year", validators=[DataRequired(), Length(max=4)])
    description = StringField(label="Description", validators=[DataRequired(), Length(max=250)])
    rating = FloatField(
        label="Rating", validators=[DataRequired(), NumberRange(min=0, max=10)]
    )
    ranking = IntegerField(
        label="Ranking", validators=[DataRequired(), NumberRange(min=0, max=10)]
    )
    review = StringField(label="Review", validators=[DataRequired(),Length(max=250)])
    img_url = StringField(label="Image URL", validators=[DataRequired(), URL()])
    submit = SubmitField(label="Add Movie")


class UpdateMovie(FlaskForm):
    title = StringField(label="Title", validators=[Length(max=250)])
    year = StringField(label="Year", validators=[Length(max=250)])
    description = StringField(label="Description", validators=[Length(max=250)])
    rating = FloatField(label="Rating", validators=[NumberRange(min=0,max=10),Optional()])
    ranking = IntegerField(label="Ranking", validators=[NumberRange(min=0,max=10),Optional()])
    review = StringField(label="Review", validators=[Length(max=250)])
    img_url = StringField(label="Image URL", validators=[Length(max=250)])
    submit = SubmitField(label="Update")
# class Select():
