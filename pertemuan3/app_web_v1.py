from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Halo Jambi: server Flask hidup"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
