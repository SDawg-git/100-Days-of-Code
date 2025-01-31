from flask import Flask, render_template
from post import Post
import requests

app = Flask(__name__)

@app.route('/')
def home():
    response = requests.get(url="https://api.npoint.io/c790b4d5cab58020d391")
    data = response.json()
    return render_template("index.html", data=data)


@app.route('/post/<int:post_ID>')
def view_post(post_ID):

    response = requests.get(url="https://api.npoint.io/c790b4d5cab58020d391")
    data = response.json()

    if post_ID == 0:
        blog_post = Post(post_id=data[0]["id"], title=data[0]["title"], subtitle=data[0]["subtitle"], body=data[0]["body"])


    elif post_ID == 1:
        blog_post = Post(post_id=data[1]["id"], title=data[1]["title"], subtitle=data[1]["subtitle"], body=data[1]["body"])

    return render_template("post.html", post_data = blog_post)



if __name__ == "__main__":
    app.run(debug=True)

