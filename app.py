from flask import Flask, request, jsonify
from sentence_transformers import SentenceTransformer, util

app = Flask(__name__)

# ------------------ LOAD MODEL ------------------
model = SentenceTransformer("all-MiniLM-L6-v2")

# ------------------ SKILL LIST ------------------
SKILLS = [
    "python",
    "java",
    "machine learning",
    "deep learning",
    "nlp",
    "data science",
    "flask",
    "docker",
    "kubernetes",
    "sql",
    "spark"
]

# ------------------ SKILL EXTRACTION ------------------
def extract_skills(text):
    text = text.lower()
    found_skills = []

    for skill in SKILLS:
        if skill in text:
            found_skills.append(skill)

    return list(set(found_skills))

# ------------------ MATCH API ------------------
@app.route("/match", methods=["POST"])
def match_resume():
    data = request.get_json(silent=True)

    if not data:
        return jsonify({"error": "JSON body required"}), 400

    resume_text = data.get("resume_text")
    job_text = data.get("job_text")

    if not resume_text or not job_text:
        return jsonify({"error": "resume_text and job_text required"}), 400

    # ---- Semantic similarity ----
    resume_emb = model.encode(resume_text, convert_to_tensor=True)
    job_emb = model.encode(job_text, convert_to_tensor=True)
    similarity = util.cos_sim(resume_emb, job_emb).item() * 100

    # ---- Skill extraction ----
    resume_skills = extract_skills(resume_text)
    job_skills = extract_skills(job_text)

    matched_skills = list(set(resume_skills) & set(job_skills))
    missing_skills = list(set(job_skills) - set(resume_skills))

    skill_score = 0
    if len(job_skills) > 0:
        skill_score = (len(matched_skills) / len(job_skills)) * 100

    # ---- Final verdict ----
    if similarity >= 75 and skill_score >= 60:
        verdict = "Strong Match"
        confidence = "High"
    elif similarity >= 50:
        verdict = "Moderate Match"
        confidence = "Medium"
    else:
        verdict = "Weak Match"
        confidence = "Low"

    return jsonify({
        "semantic_similarity": round(similarity, 2),
        "skill_match_percentage": round(skill_score, 2),
        "matched_skills": matched_skills,
        "missing_skills": missing_skills,
        "verdict": verdict,
        "confidence": confidence
    })

# ------------------ RUN ------------------
if __name__ == "__main__":
    app.run(debug=True)