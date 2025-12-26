from flask import Flask, request, jsonify
from flask_cors import CORS
import re
import os
import tempfile

from services.hybrid_matcher import HybridMatcher
from services.parser import extract_text

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

matcher = HybridMatcher()

def clean_text(text):
    """Preprocess text for better embedding scores"""
    text = text.replace("\n", " ")
    text = re.sub(r"[-•]", "", text)
    text = re.sub(r"\s+", " ", text)
    return text.strip().lower()

@app.route("/", methods=["GET"])
def home():
    return "Resume Screening System API is running 🚀"

@app.route("/match", methods=["POST"])
def match_resume_api():
    resume_text = None
    job_text = None

    # JSON body
    if request.is_json:
        data = request.get_json()
        resume_text = data.get("resume_text")
        job_text = data.get("job_text")

    # File upload
    if "resume_file" in request.files:
        resume_file = request.files["resume_file"]
        if resume_file.filename.lower().endswith(".pdf"):
            with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
                resume_file.save(tmp.name)
                resume_text = extract_text(tmp.name)
            os.unlink(tmp.name)
        job_text = request.form.get("job_text")

    if not resume_text or not job_text:
        return jsonify({"error": "resume_text (or resume_file) and job_text are required"}), 400

    # Preprocess texts
    resume_text_clean = clean_text(resume_text)
    job_text_clean = clean_text(job_text)

    print("\n===== DEBUG INPUT =====")
    print("Resume Text:", resume_text_clean[:500])
    print("Job Text:", job_text_clean[:500])
    print("======================\n")

    # Call matcher
    result = matcher.match(resume_text_clean, job_text_clean)

    print("\n===== DEBUG OUTPUT =====")
    for k, v in result.items():
        print(f"{k}: {v}")
    print("======================\n")

    return jsonify(result), 200

if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)