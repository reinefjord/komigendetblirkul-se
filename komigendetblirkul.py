import base64
import random
from flask import abort, Flask, render_template, request

app = Flask(__name__)


@app.route("/", defaults={"phrase": None})
@app.route("/<path:phrase>")
def index(phrase):
    if phrase:
        try:
            phrase = base64.urlsafe_b64decode(phrase).decode()
        except:
            pass
    else:
        with open("komigendetblirkul.db") as f:
            db = [line for line in (line.strip() for line in f) if line]
        phrase = random.choice(db)

    counter_file = "counter.db"
    try:
        counter = int(open(counter_file, "r").read())
        counter += 1
    except:
        counter = 1
    open(counter_file, "w").write(str(counter))

    b64 = base64.urlsafe_b64encode(phrase.encode()).decode()

    return render_template("komigendetblirkul.html", phrase=phrase, b64=b64)
