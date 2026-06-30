from flask import Flask, request, Response

app = Flask(__name__)

@app.route("/echo", methods=["POST"])
def echo():
    value = request.form.get("value", "00000000")

    # Invert the bits
    inverted = "".join(
        "1" if bit == "0" else "0"
        for bit in value
    )

    # Prepend a 1 so the game doesn't strip leading zeros
    return Response("1" + inverted, status=200, mimetype="text/plain")

if __name__ == "__main__":
    app.run()
