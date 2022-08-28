from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, URL


class MyCafeForm(FlaskForm):
    cafe_name = StringField(label="Cafe Name", validators=[DataRequired()])
    maps_url = StringField(label="Google Maps Link", validators=[DataRequired(), URL()])
    open_time = StringField(label="Opening Time", validators=[DataRequired()])
    close_time = StringField(label="Closing Time", validators=[DataRequired()])
    coffee_rating = SelectField(
        label="Coffee Rating",
        choices=["☕️☕️☕️☕️☕️", "☕️☕️☕️☕️", "☕️☕️☕️", "☕️☕️", "☕️"],
        validators=[DataRequired()],
    )
    wifi_strength = SelectField(
        label="Wifi Strength Rating",
        choices=["💪💪💪💪💪", "💪💪💪💪", "💪💪💪", "💪💪", "💪", "✘"],
        validators=[DataRequired()],
    )
    power_sockets = SelectField(
        label="Power Socket Availability",
        choices=["🔌🔌🔌🔌🔌", "🔌🔌🔌🔌", "🔌🔌🔌", "🔌🔌", "🔌"],
        validators=[DataRequired()],
    )
    submit = SubmitField(label="Add Entry")
