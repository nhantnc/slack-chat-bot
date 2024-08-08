from flask import Flask
from chatbot import send_syncing_message
app = Flask(__name__)

@app.route("/rnd-daily-report")
def hello():
    send_syncing_message()
    return "Syncing message sent!"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=2101)