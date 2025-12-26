from sentence_transformers import CrossEncoder
import math

class CrossEncoderMatcher:
    def __init__(self):
        self.model = CrossEncoder("cross-encoder/ms-marco-MiniLM-L-6-v2")

    def compute_score(self, resume_text: str, job_text: str) -> float:
        """
        Returns normalized relevance score (0–100)
        """
        raw_score = self.model.predict([(resume_text, job_text)])[0]

        # Sigmoid normalization
        normalized = 1 / (1 + math.exp(-raw_score))

        return round(normalized * 100, 2)