from services.matcher import match_resume
from services.cross_encoder import CrossEncoderMatcher
from services.skill_extractor import extract_skills
from services.config import HYBRID_WEIGHTS
import re

class HybridMatcher:
    def __init__(self):
        self.cross_encoder = CrossEncoderMatcher()
        self.cross_encoder_cache = {}

    @staticmethod
    def get_hash(text):
        import hashlib
        return hashlib.md5(text.encode("utf-8")).hexdigest()

    def split_sentences(self, text):
        # Simple sentence split by punctuation
        sentences = re.split(r"[.!?]", text)
        return [s.strip() for s in sentences if s.strip()]

    def match(self, resume_text: str, job_text: str):
        # -------------------------------
        # 1️⃣ Bi-Encoder score
        # -------------------------------
        bi_score = match_resume(resume_text, job_text)
        print(f"[DEBUG] Bi-Encoder Score: {bi_score}")

        # -------------------------------
        # 2️⃣ Cross-Encoder score per sentence
        # -------------------------------
        CROSS_ENCODER_THRESHOLD = 50
        key = (self.get_hash(resume_text), self.get_hash(job_text))

        if bi_score >= CROSS_ENCODER_THRESHOLD:
            if key in self.cross_encoder_cache:
                cross_score = self.cross_encoder_cache[key]
            else:
                # Split resume into sentences
                sentences = self.split_sentences(resume_text)
                cross_scores = [self.cross_encoder.compute_score(s, job_text) for s in sentences]
                cross_score = max(cross_scores) if cross_scores else 0
                self.cross_encoder_cache[key] = cross_score
        else:
            cross_score = 0
        print(f"[DEBUG] Cross-Encoder Score: {cross_score}")

        # -------------------------------
        # 3️⃣ Skill overlap
        # -------------------------------
        resume_skills = set(extract_skills(resume_text))
        job_skills = set(extract_skills(job_text))

        skill_score = len(resume_skills & job_skills) / len(job_skills) * 100 if job_skills else 0
        print(f"[DEBUG] Matched Skills: {resume_skills & job_skills}")
        print(f"[DEBUG] Skill Match Score: {skill_score}")

        # -------------------------------
        # 4️⃣ Final weighted score
        # -------------------------------
        final_score = (
            HYBRID_WEIGHTS["bi_encoder"] * bi_score +
            HYBRID_WEIGHTS["cross_encoder"] * cross_score +
            HYBRID_WEIGHTS["skill_overlap"] * skill_score
        )
        final_score = round(final_score, 2)
        print(f"[DEBUG] Final Weighted Score: {final_score}")

        # -------------------------------
        # 5️⃣ Explanation & Verdict
        # -------------------------------
        from services.explainer import generate_explanation
        result = {
            "final_score": final_score,
            "bi_encoder_score": round(bi_score, 2),
            "cross_encoder_score": round(cross_score, 2),
            "skill_match_score": round(skill_score, 2),
            "matched_skills": list(resume_skills & job_skills)
        }

        # Add explanation
        result["explanation"] = generate_explanation(result)

        # Verdict based on thresholds
        from services.config import VERDICT_THRESHOLDS
        fs = final_score
        if fs >= VERDICT_THRESHOLDS["strong"]:
            result["verdict"] = "Strong Match"
            result["confidence"] = "High"
        elif fs >= VERDICT_THRESHOLDS["moderate"]:
            result["verdict"] = "Moderate Match"
            result["confidence"] = "Medium"
        else:
            result["verdict"] = "Weak Match"
            result["confidence"] = "Low"

        return result
