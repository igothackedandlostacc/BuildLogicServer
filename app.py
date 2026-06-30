from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Server is running!"

@app.route("/echo", methods=["POST"])
def echo():
    data = request.get_json()

    print(data)

    return jsonify({
        "value": data["value"]
    })

if __name__ == "__main__":
    app.run()