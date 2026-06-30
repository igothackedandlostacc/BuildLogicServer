from flask import Flask, request

app = Flask(__name__)

@app.route("/echo", methods=["POST"])
def echo():
    # Read the binary string sent by Build Logic
    value = request.form.get("value", "00000000")

    # Invert every bit
    inverted = "".join(
        "1" if bit == "0" else "0"
        for bit in value
    )

    return inverted, 200, {
        "Content-Type": "text/plain"
    }

    print("Received:", repr(value))
    print("Sending:", repr(inverted))
    print("Length:", len(inverted))

if __name__ == "__main__":
    app.run()
