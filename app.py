from flask import Flask, request

app = Flask(__name__)

@app.route("/echo", methods=["POST"])
def echo():
    # Print everything we receive
    print("Headers:", dict(request.headers))
    print("Raw body:", request.get_data(as_text=True))

    # Try reading JSON
    data = request.get_json(silent=True)

    if data and "value" in data:
        value = data["value"]
    else:
        # If nothing was received, return all zeros
        return "00000000", 200, {"Content-Type": "text/plain"}

    print("Received value:", value)

    # Invert every bit
    inverted = "".join(
        "1" if bit == "0" else "0"
        for bit in value
    )

    print("Sending back:", inverted)

    return inverted, 200, {"Content-Type": "text/plain"}

if __name__ == "__main__":
    app.run()
