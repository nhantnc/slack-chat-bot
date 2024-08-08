from flask import Flask
from chatbot import send_syncing_message
app = Flask(__name__)

@app.route("/")
def hello():
    send_syncing_message()
    return "Hello, World!"

if __name__ == "__main__":
    app.run(host='0.0.0.0')