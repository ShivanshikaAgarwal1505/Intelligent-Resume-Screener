from services.embeddings import cosine_sim

resume = "Experienced Python and Flask developer"
job = "Looking for Flask backend engineer"

print(cosine_sim(resume, job))