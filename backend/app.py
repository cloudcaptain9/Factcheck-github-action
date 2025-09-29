from flask import Flask, request, jsonify, send_from_directory
from dotenv import load_dotenv   # <--- add this
from openai import OpenAI
import os

# Load .env variables
load_dotenv()

# Path to frontend folder (one level up from backend)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FRONTEND_DIR = os.path.join(BASE_DIR, "..", "frontend")

app = Flask(__name__)

# Initialize OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

@app.route("/")
def index():
    return send_from_directory(FRONTEND_DIR, "index.html")

@app.route("/<path:path>")
def static_files(path):
    return send_from_directory(FRONTEND_DIR, path)

@app.route("/factcheck", methods=["POST"])
def factcheck():
    data = request.get_json()
    claim = data.get("claim", "")

    if not claim:
        return jsonify({"error": "No claim provided"}), 400

    prompt = f"""
    You are a fact-checking AI.
    Verify the following claim:
    '{claim}'

    Steps:
    1. Break down the claim into entities and facts.
    2. Compare with common knowledge and likely truth.
    3. Return only JSON in this format:
    {{
        "verdict": "True/False/Unverifiable",
        "reason": "Your explanation"
    }}
    """

    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a fact-checking assistant."},
                {"role": "user", "content": prompt}
            ],
            temperature=0
        )
        output = response.choices[0].message.content
        return jsonify({"result": output})

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
