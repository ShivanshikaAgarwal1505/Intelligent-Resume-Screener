from flask import Flask, request, jsonify
import os
from services.parser import extract_text
from services.matcher import match_resume

app = Flask(__name__)

@app.route("/")
def home():
    return "Resume Screener API Running"

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/upload_resume", methods=["POST"])
def upload_resume():
    if "resume" not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    file = request.files["resume"]

    path = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(path)

    text = extract_text(path)

    print(request.files)

    return jsonify({
        "message": "Resume uploaded",
        "text_preview": text[:500]
    })

@app.route("/match", methods=["POST"])
def match():
    data = request.get_json()

    resume = data.get("resume")
    job = data.get("job")

    if not resume or not job:
        return jsonify({"error": "Resume and Job description required"}), 400

    score = match_resume(resume, job)

    return jsonify({
        "match_score": score
    })


if __name__ == "__main__":
    app.run(debug=True)
app = Flask(__name__)
