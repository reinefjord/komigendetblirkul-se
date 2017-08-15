import base64
import random
from flask import abort, Flask, render_template, request

app = Flask(__name__)

@app.route("/e/<b64>")
def encoded(b64):
    try:
        phrase = base64.urlsafe_b64decode(b64).decode()
    except:
        return index(request.path[1:])

    return index(phrase)

@app.route("/", defaults={"phrase": None})
@app.route("/<path:phrase>")
def index(phrase):
    if not phrase:
        with open("komigendetblirkul.db") as f:
            db = [line for line in (line.strip() for line in f) if line]
        phrase = random.choice(db)

    b64 = base64.urlsafe_b64encode(phrase.encode()).decode()

    return render_template("komigendetblirkul.html", phrase=phrase, b64=b64)
