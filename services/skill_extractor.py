import re

# Skills with synonyms
SKILLS_DB = {
    "python": ["python"],
    "java": ["java"],
    "c++": ["c++", "cpp"],
    "flask": ["flask"],
    "django": ["django"],
    "docker": ["docker"],
    "kubernetes": ["kubernetes", "k8s"],
    "nlp": ["nlp", "natural language processing"],
    "machine learning": ["machine learning", "ml"],
    "deep learning": ["deep learning", "neural networks"],
    "pytorch": ["pytorch"],
    "tensorflow": ["tensorflow", "tf"],
    "sql": ["sql"],
    "spark": ["spark", "apache spark"],
    "aws": ["aws", "amazon web services"],
    "git": ["git"]
}

def extract_skills(text: str):
    text = text.lower()
    found_skills = []
    for skill, synonyms in SKILLS_DB.items():
        for syn in synonyms:
            if re.search(rf"\b{re.escape(syn)}\b", text):
                found_skills.append(skill)
                break
    return list(set(found_skills))