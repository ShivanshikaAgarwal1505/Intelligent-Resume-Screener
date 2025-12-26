from flask import Flask, request, jsonify
from services.hybrid_matcher import HybridMatcher
from services.explainer import generate_explanation

app = Flask(__name__)

# Initialize Hybrid Matcher once
matcher = HybridMatcher()

@app.route("/")
def home():
    return "Resume Screening System API is running 🚀"

# ------------------ MATCH API ------------------
@app.route("/match", methods=["POST"])
def match_resume():
    data = request.get_json(silent=True)

    if not data:
        return jsonify({"error": "JSON body required"}), 400

    resume_text = data.get("resume_text")
    job_text = data.get("job_text")

    if not resume_text or not job_text:
        return jsonify({
            "error": "resume_text and job_text are required"
        }), 400

    # ---- Hybrid Matching ----
    result = matcher.match(resume_text, job_text)

    # ---- Explanation (LLM-style reasoning) ----
    explanation = generate_explanation(result)
    result["explanation"] = explanation

    # ---- Verdict Logic ----
    final_score = result["final_score"]

    if final_score >= 85:
        verdict = "Strong Match"
        confidence = "High"
    elif final_score >= 65:
        verdict = "Moderate Match"
        confidence = "Medium"
    else:
        verdict = "Weak Match"
        confidence = "Low"

    result["verdict"] = verdict
    result["confidence"] = confidence

    return jsonify(result), 200


if __name__ == "__main__":
    app.run(debug=True)