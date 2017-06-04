import os

from flask import Flask, render_template
from textmaker import MarkovMaker

DEBUG = not int(os.environ.get("NO_DEBUG", 0))
PORT = int(os.environ.get("PORT", 5001))

app = Flask(__name__)

generator = MarkovMaker()
generator.train("texts/trump.txt")


@app.route("/")
def text_maker():
    text, meta = generator.make_text(return_meta=True)
    return render_template("text_maker.html", text=text, meta=meta)


if __name__ == '__main__':
    app.run(debug=DEBUG, host="0.0.0.0", port=PORT)
