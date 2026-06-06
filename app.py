from flask import Flask, render_template
import random

app = Flask(__name__)

quotes = [
    "Success is not final",
    "Dream big",
    "Never give up"
]

@app.route("/")
def home():
    quote = random.choice(quotes)
    return render_template("index.html", quote=quote)

if __name__ == "__main__":
    app.run(debug=True)