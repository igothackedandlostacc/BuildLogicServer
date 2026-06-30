from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Server is running!"

@app.route("/echo", methods=["POST"])
def echo():
    data = request.get_json(silent=True)

    if data is None:
        return jsonify({"value": "00000000"})

    return jsonify({
        "value": data.get("value", "00000000")
    })

if __name__ == "__main__":
    app.run()
