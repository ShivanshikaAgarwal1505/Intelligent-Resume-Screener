import re

# Simple predefined skill vocabulary (expand later)
SKILLS_DB = [
    "python", "java", "c++", "flask", "django",
    "docker", "kubernetes", "nlp", "machine learning",
    "deep learning", "pytorch", "tensorflow",
    "sql", "spark", "aws", "git"
]

def extract_skills(text: str):
    text = text.lower()
    found_skills = []

    for skill in SKILLS_DB:
        # word-boundary safe matching
        if re.search(rf"\b{re.escape(skill)}\b", text):
            found_skills.append(skill)

    return found_skills