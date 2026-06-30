from flask import Flask, request
from flask import Response

app = Flask(__name__)

@app.route("/echo", methods=["POST"])
def echo():
    value = request.form.get("value", "00000000")

    return res(value, status=200, mimetype="text/plain")

if __name__ == "__main__":
    app.run()
