from flask import Flask, request, jsonify
import requests
import os

DISC_SECRET = os.getenv("DISC_SECRET")

def send_webhook_message(url = "https://my_account.discourse.group/chat/hooks/", message = "Hello from server!"):
    payload = {"text": message}
    response = requests.post(url+DISC_SECRET, json=payload)

    print(response.status_code)
    print(response.text)

app = Flask(__name__)

@app.route("/process", methods=["POST"])
def process_text():
    data = request.get_json(force=True, silent=True)
    # Return the entire received payload for debugging

    # Format 'data' as a string before sending
    formatted_message = str(data)
    send_webhook_message(message=formatted_message)

    return jsonify({"received": data})

@app.route("/")
def home():
    return "Text processing API is running 🚀"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", 5000)))
