from random import Random
from flask import Flask
import random

app = Flask(__name__)

@app.route("/")
def root():
    return "<h1>Guess a number between 0 and 9</h1>"

@app.route("/<int:guess>")
def guess(guess):
    if guess < NUMBER_TO_GUESS:
        return "<h1>Higher</h1>"
    elif guess > NUMBER_TO_GUESS:
        return "<h1>Lower</h1>"
    else:
        return "<h1>You Guessed Correctly</h1>"\
               "<img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif'/>"


NUMBER_TO_GUESS = random.randint(0,9)