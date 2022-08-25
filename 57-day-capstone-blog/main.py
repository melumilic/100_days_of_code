from flask import Flask, render_template
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
    return render_template("index.html", blog_data=blog_data)

@app.route("/blogs/<blog_id>")
def blog_post(blog_id):
    return render_template("post.html",blog_data=blog_data[int(blog_id)-1])

if __name__ == "__main__":
    app.run(debug=True)
