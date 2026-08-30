import requests
from flask import Flask, render_template, abort
from app import ambil_cuaca

app = Flask(__name__)

@app.route("/")
def index():
    try:
        data = ambil_cuaca()
    except requests.exceptions.RequestException:
        abort(503)   # API cuaca tidak dapat dijangkau
    return render_template("dashboard.html", cuaca=data)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
