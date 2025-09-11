from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/process", methods=["POST"])
def process_text():
    data = request.get_json()
    text = data.get("text", "")

    # Example "processing": make uppercase
    processed = text.upper()

    return jsonify({"original": text, "processed": processed})

@app.route("/")
def home():
    return "Text processing API is running 🚀"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
