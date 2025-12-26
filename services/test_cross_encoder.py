from services.cross_encoder import CrossEncoderMatcher

matcher = CrossEncoderMatcher()

resume = "Worked on Flask APIs and backend development"
job = "Looking for backend developer with Flask experience"

score = matcher.compute_score(resume, job)

print("Cross-Encoder Score:", score)