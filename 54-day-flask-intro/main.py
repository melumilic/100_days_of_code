from flask import Flask


def make_bold(function):
    def wrapper():
        return "<b>" + function() + "</b>"
    return wrapper


app = Flask(__name__)

@app.route("/")
@make_bold
def hello_world():
    return "<p>Hello, World!</p>"