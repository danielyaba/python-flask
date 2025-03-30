from flask import Flask, render_template, url_for
import os

app = Flask(__name__)


@app.route("/")
def hello_world():
    return render_template(
        "index.html", static_url=url_for("static", filename="style.css")
    )


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=os.getenv("FLASK_DEBUG", "False").lower() == "true",
    )
