from flask import Flask, request

app = Flask(__name__)

@app.route("/echo", methods=["POST"])
def echo():
    print("===== NEW REQUEST =====")
    print("Content-Type:", request.content_type)
    print("Headers:", dict(request.headers))
    print("Raw body:", repr(request.get_data(as_text=True)))
    print("Form:", request.form)
    print("Args:", request.args)

    return "10101010", 200, {"Content-Type": "text/plain"}

if __name__ == "__main__":
    app.run()
