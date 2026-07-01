from flask import Flask, request, Response

app = Flask(__name__)

# Stores the last received value
last_value = "No value received yet."

@app.route("/")
def home():
    return f"""
    <html>
        <head>
            <title>Build Logic Server</title>
            <meta http-equiv="refresh" content="2">
        </head>
        <body style="font-family: Arial; text-align: center; margin-top: 50px;">
            <h1>Build Logic Server</h1>
            <h2>Last Received Value:</h2>
            <h1>{last_value}</h1>
        </body>
    </html>
    """

@app.route("/echo", methods=["POST"])
def echo():
    global last_value

    # Read the value sent by Build Logic
    value = request.form.get("value", "00000000")

    # Save it so the homepage can display it
    last_value = value

    # Send it back unchanged (prepend 1 if you're using the workaround)
    return Response("1" + value, status=200, mimetype="text/plain")

if __name__ == "__main__":
    app.run()
