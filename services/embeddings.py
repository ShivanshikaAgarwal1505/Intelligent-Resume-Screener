from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

# Load model once
model = SentenceTransformer("all-MiniLM-L6-v2")

def get_embedding(text):
    """
    Returns embedding for a single text
    """
    return model.encode(text)

def get_embeddings(texts):
    """
    Returns embeddings for multiple texts
    """
    return model.encode(texts)

def cosine_sim(text1, text2):
    """
    Returns cosine similarity percentage between two texts
    """
    emb1 = get_embedding(text1)
    emb2 = get_embedding(text2)

    score = cosine_similarity([emb1], [emb2])[0][0]
    return round(score * 100, 2)