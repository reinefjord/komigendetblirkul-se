import random
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def random_phrase():
    with open("komigendetblirkul.db") as f:
        db = [line for line in (line.strip() for line in f) if line]

    phrase = random.choice(db)

    return render_template("komigendetblirkul.html", phrase=phrase)


@app.route("/<path:phrase>")
def user_phrase(phrase):
    return render_template("komigendetblirkul.html", phrase=phrase)
