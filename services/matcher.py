from sklearn.metrics.pairwise import cosine_similarity
from services.embeddings import get_embedding

def match_resume(resume_text, job_text):
    emb1 = get_embedding(resume_text)
    emb2 = get_embedding(job_text)

    score = cosine_similarity([emb1], [emb2])[0][0]
    return round(float(score) * 100, 2)  # Convert to Python float here