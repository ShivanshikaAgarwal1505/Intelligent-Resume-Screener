from services.matcher import compute_bi_encoder_score, get_verdict

resume = "Experienced Python developer with Flask and ML background"
job = "Looking for a Flask backend engineer with Python skills"

score = compute_bi_encoder_score(resume, job)
verdict = get_verdict(score)

print("Score:", score)
print("Verdict:", verdict)