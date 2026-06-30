from flask import Flask, request

app = Flask(__name__)

@app.route("/echo", methods=["POST"])
def echo():
    # Read the binary string sent by Build Logic
    value = request.form.get("value", "00000000")

    print("Received:", value)

    # Invert every bit
    inverted = "".join(
        "1" if bit == "0" else "0"
        for bit in value
    )

    print("Sending:", inverted)

    return inverted, 200, {
        "Content-Type": "text/plain"
    }

if __name__ == "__main__":
    app.run()
