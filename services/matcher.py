from sklearn.metrics.pairwise import cosine_similarity
from services.embeddings import get_embedding
from services.config import VERDICT_THRESHOLDS

def compute_bi_encoder_score(resume_text: str, job_text: str) -> float:
    """
    Computes Bi-Encoder cosine similarity score (0–100)
    """
    emb1 = get_embedding(resume_text)
    emb2 = get_embedding(job_text)

    score = cosine_similarity([emb1], [emb2])[0][0]
    return round(float(score) * 100, 2)

def get_verdict(score: float) -> str:
    """
    Returns human-readable verdict based on centralized thresholds
    """
    if score >= VERDICT_THRESHOLDS["strong"]:
        return "Strong Match"
    elif score >= VERDICT_THRESHOLDS["moderate"]:
        return "Moderate Match"
    else:
        return "Weak Match"

# Backward compatibility
def match_resume(resume_text, job_text):
    return compute_bi_encoder_score(resume_text, job_text)
