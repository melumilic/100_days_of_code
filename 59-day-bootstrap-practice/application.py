from flask import Flask
from flask import render_template
from post import Post
import requests

response = requests.get("https://api.npoint.io/c790b4d5cab58020d391")
blogs = response.json()
blog_data = [
    Post(blog["id"], blog["title"], blog["subtitle"], blog["body"])
    for blog in blogs
]

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html",blog_data=blog_data)


@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/posts/<post_id>")
def post(post_id):
    return render_template("post.html",blog_post=blog_data[int(post_id)-1])


@app.route("/contact")
def contact():
    return render_template("contact.html")