from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Server is running!"

@app.route("/echo", methods=["POST"])
def echo():
    print("Headers:", dict(request.headers))
    print("Content-Type:", request.content_type)
    print("Raw body:", request.get_data(as_text=True))
    print("Form:", request.form)
    print("JSON:", request.get_json(silent=True))

    return "hello world my name is quandale dingle", 200, {
        "Content-Type": "text/plain"
    }

if __name__ == "__main__":
    app.run()
