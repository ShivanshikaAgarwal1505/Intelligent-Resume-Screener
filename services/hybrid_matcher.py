from services.matcher import match_resume
from services.cross_encoder import CrossEncoderMatcher
from services.skill_extractor import extract_skills

class HybridMatcher:
    def __init__(self):
        self.cross_encoder = CrossEncoderMatcher()

    def match(self, resume_text: str, job_text: str):
        # 1️⃣ Bi-Encoder score
        bi_score = match_resume(resume_text, job_text)

        # 2️⃣ Cross-Encoder score
        cross_score = self.cross_encoder.compute_score(resume_text, job_text)

        # 3️⃣ Skill overlap
        resume_skills = set(extract_skills(resume_text))
        job_skills = set(extract_skills(job_text))

        skill_overlap = len(resume_skills & job_skills)
        skill_score = min(skill_overlap * 10, 100)

        # 4️⃣ Final weighted score
        final_score = (
            0.4 * bi_score +
            0.5 * cross_score +
            0.1 * skill_score
        )

        return {
            "final_score": round(final_score, 2),
            "bi_encoder_score": bi_score,
            "cross_encoder_score": cross_score,
            "skill_match_score": skill_score,
            "matched_skills": list(resume_skills & job_skills)
        }