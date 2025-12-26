from services.hybrid_matcher import HybridMatcher

resume = """
Python developer with experience in Flask, Docker, NLP and Machine Learning.
"""

job = """
Looking for a backend engineer skilled in Python, Flask, Docker and NLP.
"""

matcher = HybridMatcher()
result = matcher.match(resume, job)

print(result)