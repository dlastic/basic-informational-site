from flask import Flask, send_file
import os

app = Flask(__name__)


@app.route("/")
def index():
    return send_file("index.html")


@app.route("/about")
def about():
    return send_file("about.html")


@app.route("/contact-me")
def contact_me():
    return send_file("contact-me.html")


@app.route("/<path:path>")
def catch_all(path):
    return send_file("404.html"), 404


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    try:
        app.run(port=port, debug=True)
    except Exception as e:
        raise RuntimeError(f"Failed to start server: {e}")
