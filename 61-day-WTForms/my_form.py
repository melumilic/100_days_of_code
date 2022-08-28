from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, Email, Regexp

class MyForm(FlaskForm):
    email = StringField(label="email", validators=[DataRequired(),Length(8,120),Email()])
    # Regexp("^.*(?=.{8,})(?=.*[a-zA-Z])(?=.*\d)(?=.*[!#$%&? \"]).*$")
    password = PasswordField(label="password", validators=[DataRequired(),Length(8,120)])
    submit = SubmitField(label="Submit")