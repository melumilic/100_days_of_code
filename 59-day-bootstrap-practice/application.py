from http.client import NOT_IMPLEMENTED
from flask import Flask
from flask import render_template
from flask import request
from post import Post
from smtplib import SMTP_SSL
from email.message import EmailMessage

import requests

response = requests.get("https://api.npoint.io/c790b4d5cab58020d391")
blogs = response.json()
blog_data = [
    Post(blog["id"], blog["title"], blog["subtitle"], blog["body"]) for blog in blogs
]

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html", blog_data=blog_data)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/posts/<post_id>")
def post(post_id):
    return render_template("post.html", blog_post=blog_data[int(post_id) - 1])


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/contact-sent", methods=["POST","GET"])
def receive_contact_data():
    error = None
    if request.method == "POST":
        # server = SMTP_SSL('smtp.gmail.com', 465)
        # server.login("username", "password")

        # message_email = EmailMessage()
        # message_email.set_content("Here is the message")
        # message_email["Subject"]="This is the subject"
        # message_email["From"]="examplefrom@gmail.com"
        # message_email["To"]="examplefrom@gmail.com"

        # server.sendmail(message_email)
        # server.quit()
        return request.form["name"]
    return "not implemented"
