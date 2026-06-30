from flask import Flask, request
from flask import Response

app = Flask(__name__)

@app.route("/echo", methods=["POST"])
def echo():
    return Response("101010101", status=200, mimetype="text/plain")

if __name__ == "__main__":
    app.run()
