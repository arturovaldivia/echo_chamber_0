from flask import Flask, request, jsonify  # custom library (Flask)
import requests                           # custom library (requests)
import os                                 # base Python library

DISC_ACCOUNT = os.getenv("DISC_ACCOUNT")
DISC_SECRET = os.getenv("DISC_SECRET")

def send_webhook_message(url = "https://my_account.discourse.group/chat/hooks/", message = "Hello from server!"):
    payload = {"text": message}
    response = requests.post(url, json=payload)

    print(response.status_code)
    print(response.text)

app = Flask(__name__)

@app.route("/process", methods=["POST"])
def process_text():
    data = request.get_json()
    if data is None:
        return jsonify({"error": "Invalid JSON"}), 400
    # Return the entire received payload for debugging
    print("Received data:", data)

    # Format 'data' as a string before sending
    formatted_message = str(data)
    URL = "https://"+DISC_ACCOUNT+".discourse.group/chat/hooks/"+DISC_SECRET
    send_webhook_message(url = URL, message=formatted_message)

    return jsonify({"received": data})

@app.route("/check", methods=["POST"])
def check_text():
    return "POST received ✅", 200

@app.route("/")
def home():
    return "Text processing API is running 🚀"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", 5000)))
