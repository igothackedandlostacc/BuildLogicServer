from flask import Flask, request

app = Flask(__name__)

@app.route("/echo", methods=["POST"])
def echo():
    value = request.form.get("value", "00000000")

    inverted = "".join("1" if b == "0" else "0" for b in value)

    return Response(
        inverted,
        status=200,
        mimetype="text/plain"
    )

if __name__ == "__main__":
    app.run()
