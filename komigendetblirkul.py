import base64
import random
from flask import abort, Flask, render_template, request, send_file

app = Flask(__name__)


@app.route("/", defaults={"phrase": None})
@app.route("/<path:phrase>")
def index(phrase):

    if request.path == "/favicon.ico":
        return send_file("favicon.ico")

    if phrase:
        try:
            phrase = base64.urlsafe_b64decode(phrase).decode()
        except:
            pass
    else:
        with open("komigendetblirkul.db") as f:
            db = [line for line in (line.strip() for line in f) if line]
        phrase = random.choice(db)


    b64 = base64.urlsafe_b64encode(phrase.encode()).decode()

    return render_template("komigendetblirkul.html", phrase=phrase, b64=b64)
