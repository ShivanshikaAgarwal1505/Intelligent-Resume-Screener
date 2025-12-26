from sklearn.metrics.pairwise import cosine_similarity
from services.embeddings import get_embedding

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
    Returns human-readable verdict based on score
    """
    if score >= 75:
        return "Strong Match"
    elif score >= 50:
        return "Moderate Match"
    else:
        return "Weak Match"

# Backward compatibility (DO NOT REMOVE)
def match_resume(resume_text, job_text):
    return compute_bi_encoder_score(resume_text, job_text)