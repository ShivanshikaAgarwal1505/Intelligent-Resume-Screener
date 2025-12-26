from services.matcher import match_resume
from services.cross_encoder import CrossEncoderMatcher
from services.skill_extractor import extract_skills

class HybridMatcher:
    def __init__(self):
        self.w_bi = 0.4
        self.w_cross = 0.4
        self.w_skill = 0.2

    def match(self, resume_text, job_text):
        bi_score = bi_encoder_match(resume_text, job_text)
        cross_score = cross_encoder_match(resume_text, job_text)
        skill_score, matched_skills = skill_match(resume_text, job_text)

        final_score = (
            self.w_bi * bi_score +
            self.w_cross * cross_score +
            self.w_skill * skill_score
        )

        return {
            "final_score": round(final_score, 2),
            "bi_encoder_score": bi_score,
            "cross_encoder_score": cross_score,
            "skill_match_score": skill_score,
            "matched_skills": matched_skills
        }