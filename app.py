
import os
import json
from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

app = Flask(__name__)

# Prompt pattern 1: Role/persona prompting
# Prompt pattern 2: Structured JSON output
SYSTEM_PROMPT = """
You are StudyBuddy AI, a friendly and patient personal tutor.
Adapt your explanations to the student's level.
Create a practical study plan that fits the student's available time.
Write clear, accurate multiple-choice questions with four options each.
Avoid overly complicated language for beginners.

Return only a valid JSON object with this structure:
{
  "title": "A short title for the study session",
  "study_plan": [
    {"time": "0-5 minutes", "task": "What the student should do"}
  ],
  "quiz": [
    {
      "question": "A multiple-choice question",
      "options": ["A. First option", "B. Second option", "C. Third option", "D. Fourth option"],
      "answer": "The correct option",
      "explanation": "Why the answer is correct"
    }
  ],
  "tips": ["A useful study tip"]
}

Create 3 to 6 study steps and exactly 5 quiz questions.
Include four answer options per question and make the correct answer clear.
Make the total study steps fit the time available.
Include 2 to 4 useful study tips.
Do not add markdown fences around the JSON.
"""


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/generate", methods=["POST"])
def generate():
    data = request.get_json(silent=True) or {}

    topic = (data.get("topic") or "").strip()
    level = (data.get("level") or "Beginner").strip()

    try:
        minutes = int(data.get("minutes", 30))
    except (TypeError, ValueError):
        return jsonify({"error": "Please select a valid study time."}), 400

    if not topic:
        return jsonify({"error": "Please enter a study topic."}), 400

    if minutes < 10 or minutes > 180:
        return jsonify({"error": "Choose between 10 and 180 minutes."}), 400

    api_key = os.getenv("GROQ_API_KEY")
    if not api_key:
        return jsonify({
            "error": "API key missing. Add GROQ_API_KEY to your .env file, then restart the app."
        }), 500

    try:
        client = Groq(api_key=api_key)

        response = client.chat.completions.create(
            model="openai/gpt-oss-20b",
            temperature=0.3,
            response_format={"type": "json_object"},
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {
                    "role": "user",
                    "content": (
                        f"Study topic: {topic}\n"
                        f"Available time: {minutes} minutes\n"
                        f"Student level: {level}\n"
                        "Generate the study plan, quiz, and tips."
                    )
                }
            ]
        )

        result = json.loads(response.choices[0].message.content)
        return jsonify(result)

    except Exception as error:
        print("AI generation error:", error)
        return jsonify({
            "error": "The AI request failed. Check your API key, model availability, and the terminal error."
        }), 500


if __name__ == "__main__":
    app.run(debug=True)
