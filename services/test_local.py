from services.hybrid_matcher import HybridMatcher
from services.explainer import generate_explanation

# Sample resume and job description
resume_text = """
Experienced Python developer with knowledge in machine learning, NLP, and AWS.
Worked with Flask, Django, Docker, and SQL databases.
"""

job_text = """
Looking for a software engineer skilled in Python, deep learning, NLP, and cloud services like AWS.
Experience with Flask or Django, Docker, and SQL is preferred.
"""

# Initialize matcher
matcher = HybridMatcher()

# Run hybrid match
result = matcher.match(resume_text, job_text)

# Generate explanation
result["explanation"] = generate_explanation(result)

# Print results
print("Final Score:", result["final_score"])
print("Bi-Encoder Score:", result["bi_encoder_score"])
print("Cross-Encoder Score:", result["cross_encoder_score"])
print("Skill Match Score:", result["skill_match_score"])
print("Matched Skills:", result["matched_skills"])
print("Explanation:", result["explanation"])