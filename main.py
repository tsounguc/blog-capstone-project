from flask import Flask, render_template
import requests
from post import Post

app = Flask(__name__)

blog_url = "https://api.npoint.io/31f3edd52b60ab8cee6e"
response = requests.get(url=blog_url)
response.raise_for_status()
blog_data = response.json()
posts = []

for post in blog_data:
    post_object = Post(post['id'], post['title'], post['subtitle'], post['body'])
    posts.append(post_object)


@app.route('/')
def home():

    return render_template("index.html", blogs=posts)


@app.route('/post/<int:blog_id>')
def post_page(blog_id):
    requested_post = None
    for post in posts:
        if post.id == blog_id:
            requested_post = post
    return render_template("post.html", blog=requested_post)


if __name__ == "__main__":
    app.run(debug=True)
