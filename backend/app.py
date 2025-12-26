from flask import Flask, request, jsonify
from services.hybrid_matcher import HybridMatcher
from services.explainer import generate_explanation
from services.config import VERDICT_THRESHOLDS
from services.parser import extract_text
import tempfile

app = Flask(__name__)
matcher = HybridMatcher()

@app.route("/match", methods=["POST"])
def match_resume_api():
    # 1️⃣ Check for JSON or file upload
    data = request.get_json(silent=True)
    resume_text = job_text = None

    # Option 1: JSON body
    if data:
        resume_text = data.get("resume_text")
        job_text = data.get("job_text")

    # Option 2: File upload (resume PDF)
    if 'resume_file' in request.files:
        resume_file = request.files['resume_file']
        if resume_file.filename.endswith(".pdf"):
            with tempfile.NamedTemporaryFile(delete=True) as tmp:
                resume_file.save(tmp.name)
                resume_text = extract_text(tmp.name)
        else:
            return jsonify({"error": "Only PDF files are supported"}), 400

        # Job text must still come from JSON
        if data:
            job_text = data.get("job_text")

    # Validate input
    if not resume_text or not job_text:
        return jsonify({"error": "resume_text and job_text are required"}), 400

    # ---- Hybrid Matching ----
    result = matcher.match(resume_text, job_text)

    # ---- Explanation ----
    result["explanation"] = generate_explanation(result)

    # ---- Verdict Logic ----
    final_score = result["final_score"]
    if final_score >= VERDICT_THRESHOLDS["strong"]:
        verdict = "Strong Match"
        confidence = "High"
    elif final_score >= VERDICT_THRESHOLDS["moderate"]:
        verdict = "Moderate Match"
        confidence = "Medium"
    else:
        verdict = "Weak Match"
        confidence = "Low"

    result["verdict"] = verdict
    result["confidence"] = confidence

    return jsonify(result), 200