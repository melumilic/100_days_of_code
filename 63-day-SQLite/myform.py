from xml.dom import ValidationErr
from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, SubmitField
from wtforms.validators import DataRequired, NumberRange

# def validate_rating(form,field):
#     if field.data < 0 and field.data >5:
#         raise ValidationErr('Rating must be between 0 and 5')

class BookForm(FlaskForm):
    book_name = StringField(label="Book Title",validators=[DataRequired()])
    author = StringField(label="Author",validators=[DataRequired()])
    rating = FloatField(label="Rating",validators=[DataRequired(),NumberRange(min=0,max=5)])
    submit = SubmitField(label="Add Book")
