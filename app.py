import os
from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv
import openai

load_dotenv()  # loads .env in development
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
# If a key isn't set, warn instead of crashing so the dev server can run locally.
# Replace the placeholder in `.env` or set the environment variable for real API access.
if not OPENAI_API_KEY or OPENAI_API_KEY.strip() == "" or OPENAI_API_KEY.startswith("YOUR_") or OPENAI_API_KEY == "sk-FAKE_KEY_FOR_LOCAL_DEV":
    print("Warning: OPENAI_API_KEY not set or is a placeholder. Set a real key in environment or a .env file to enable API calls.")
    openai.api_key = None
else:
    openai.api_key = OPENAI_API_KEY

app = Flask(__name__)

# helper to call chat completion (simple wrapper)
def ask_ai(system_prompt, user_prompt, model="gpt-4o-mini" ):
    """
    Sends a chat-style request to the API and returns assistant content.
    Adjust model as needed; e.g., "gpt-3.5-turbo" or other available models.
    """
    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt}
    ]
    # you can tune temperature, max_tokens, etc.
    resp = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0.2,
        max_tokens=600
    )
    # extract assistant reply
    return resp.choices[0].message.content.strip()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/summarize", methods=["POST"])
def summarize():
    data = request.json or {}
    text = data.get("text", "")
    if not text:
        return jsonify({"error": "No text provided"}), 400

    sys = "You are a helpful study assistant. Summarize the user's text in 5–8 short bullet points."
    user_prompt = f"Summarize the following text:\n\n{text}"

    try:
        result = ask_ai(sys, user_prompt)
        return jsonify({"result": result})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/api/explain", methods=["POST"])
def explain():
    data = request.json or {}
    text = data.get("text", "")
    level = data.get("level", "highschool")  # e.g., 'middle', 'highschool', 'college'
    if not text:
        return jsonify({"error": "No text provided"}), 400

    sys = "You are a patient teacher who explains concepts in simple language."
    user_prompt = f"Explain the following to a {level} student in simple terms, with a short example:\n\n{text}"

    try:
        result = ask_ai(sys, user_prompt)
        return jsonify({"result": result})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/api/quiz", methods=["POST"])
def quiz():
    data = request.json or {}
    text = data.get("text", "")
    qcount = int(data.get("count", 3))
    if not text:
        return jsonify({"error": "No text provided"}), 400

    sys = "You are an assistant that generates short study quizzes with answers."
    user_prompt = f"Create {qcount} short quiz questions (with 4 options each) based on the text below. Provide the correct answer letter after each question.\n\n{text}"

    try:
        result = ask_ai(sys, user_prompt)
        return jsonify({"result": result})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)