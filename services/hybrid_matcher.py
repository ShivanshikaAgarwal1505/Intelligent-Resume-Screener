from services.matcher import match_resume
from services.cross_encoder import CrossEncoderMatcher
from services.skill_extractor import extract_skills
from services.config import HYBRID_WEIGHTS

class HybridMatcher:
    def __init__(self):
        self.cross_encoder = CrossEncoderMatcher()
        self.cross_encoder_cache = {}  # optional cache for repeated pairs

    @staticmethod
    def get_hash(text):
        """Generate hash for caching"""
        import hashlib
        return hashlib.md5(text.encode("utf-8")).hexdigest()

    def match(self, resume_text: str, job_text: str):
        # -------------------------------
        # 1️⃣ Bi-Encoder score
        # -------------------------------
        bi_score = match_resume(resume_text, job_text)

        # -------------------------------
        # 2️⃣ Cross-Encoder score (optimized)
        # -------------------------------
        # Skip Cross-Encoder if Bi-Encoder score is low
        CROSS_ENCODER_THRESHOLD = 50  # configurable
        key = (self.get_hash(resume_text), self.get_hash(job_text))

        if bi_score >= CROSS_ENCODER_THRESHOLD:
            # Check cache
            if key in self.cross_encoder_cache:
                cross_score = self.cross_encoder_cache[key]
            else:
                cross_score = self.cross_encoder.compute_score(resume_text, job_text)
                self.cross_encoder_cache[key] = cross_score
        else:
            cross_score = 0

        # -------------------------------
        # 3️⃣ Skill overlap
        # -------------------------------
        resume_skills = set(extract_skills(resume_text))
        job_skills = set(extract_skills(job_text))

        if job_skills:
            skill_score = len(resume_skills & job_skills) / len(job_skills) * 100
        else:
            skill_score = 0

        # -------------------------------
        # 4️⃣ Final weighted score
        # -------------------------------
        final_score = (
            HYBRID_WEIGHTS["bi_encoder"] * bi_score +
            HYBRID_WEIGHTS["cross_encoder"] * cross_score +
            HYBRID_WEIGHTS["skill_overlap"] * skill_score
        )

        return {
            "final_score": round(final_score, 2),
            "bi_encoder_score": bi_score,
            "cross_encoder_score": round(cross_score, 2),
            "skill_match_score": round(skill_score, 2),
            "matched_skills": list(resume_skills & job_skills)
        }