from flask import render_template
from app import app

@app.route("/")
@app.route("/index")

def index():
    user={"username": "Boris"}
    posts=[
        {
            "author": {"username": "Harry"},
            "body": "Learning me some python"
        },
        {
            "author": {"username": "Harry again"},
            "body": "Learning me some json too"
        }
    ]
    return render_template("index.htm", title="Steve Holmes' github homepage", user=user, posts=posts)