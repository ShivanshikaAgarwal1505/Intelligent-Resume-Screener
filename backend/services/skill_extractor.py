import re

SKILLS_DB = {
    # Technical skills
    "python": ["python"],
    "java": ["java"],
    # ... existing tech skills

    # Soft / retail skills
    "customer service": ["customer service", "serving customers", "client support"],
    "teamwork": ["teamwork", "team player", "collaboration", "collaborative"],
    "cash handling": ["cash handling", "cash register", "money management"],
    "coaching": ["coaching", "mentoring", "trainer", "assistant coach"],
    "communication": ["communication", "communicate", "speaking", "presentation"],
    "organization": ["organization", "organized", "time management", "planning"],
    "sports equipment knowledge": ["sports equipment", "sports gear"]
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