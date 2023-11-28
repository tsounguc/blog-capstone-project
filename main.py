from flask import Flask, render_template
import requests

app = Flask(__name__)

blog_data = []


@app.route('/')
def home():
    global blog_data
    blog_url = "https://api.npoint.io/31f3edd52b60ab8cee6e"
    response = requests.get(url=blog_url)
    response.raise_for_status()
    blog_data = response.json()
    return render_template("index.html", blogs=blog_data)


@app.route('/post/<int:blog_id>')
def post_page(blog_id):
    global blog_data
    blog = blog_data[blog_id]
    print(blog_data)
    print(blog)
    return render_template("post.html", blog=blog)


if __name__ == "__main__":
    app.run(debug=True)
