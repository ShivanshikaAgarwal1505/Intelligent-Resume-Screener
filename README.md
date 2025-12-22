# Intelligent Resume Screening System

An **end-to-end intelligent resume screening system** built with **Python, Flask, NLP, and Deep Learning**, designed to help recruiters quickly evaluate resumes against job descriptions. Beginner-friendly but scalable for advanced features like LLM explanations and skill extraction.

---

## Project Overview

This system allows users to:

- Upload a **resume (PDF)**
- Compare it against a **job description**
- Get a **match score (0–100)**
- Receive insights such as:
  - Missing skills
  - Reasons for a low match score
  - Suggestions for improvement

---

## Technologies Used

| Technology              | Purpose |
|-------------------------|---------|
| Python                  | Core programming |
| Flask                   | REST API framework |
| PyPDF                   | Extract text from resumes |
| Sentence Transformers   | Convert text to embeddings |
| Scikit-learn (Cosine Similarity) | Measure resume-job match |
| Docker (optional)       | Containerization |
| LLM (e.g., GPT)         | Explain match results in human language |
| Deep Learning (optional) | Skill extraction and advanced NLP models |

---

## Project Structure
resume_screener/
│
├── app.py # Main Flask application
├── services/
│ ├── parser.py # PDF parsing logic
│ ├── embeddings.py # Convert text to embeddings
│ ├── matcher.py # Resume-job matching logic
├── uploads/ # Store uploaded resumes
├── requirements.txt # Python dependencies
└── README.md # Project documentation

---

## Project Phases

### Phase 1 — Resume Upload & Text Extraction
- Implement Flask API for uploading PDF resumes
- Use `PyPDF` to extract text page by page
- Test via Postman

### Phase 2 — Resume-Job Matching (NLP Embeddings)
- Convert resume and job description text into embeddings using **Sentence Transformers**
- Calculate **cosine similarity** to produce a match score
- Expose `/match` API endpoint

### Phase 3 — Skill Extraction (Optional)
- Extract keywords/skills from resumes and job descriptions
- Highlight **missing skills** to provide actionable feedback

### Phase 4 — LLM Explanation (Optional)
- Integrate a **Large Language Model** to provide human-readable feedback:
  - Why score is high or low
  - Missing or underrepresented skills
  - Suggestions for improvement

### Phase 5 — Basic Deep Learning Model (Optional)
- Train a simple **text classification or named entity recognition model** to:
  - Classify resumes by job domain
  - Extract skills automatically
- Improves accuracy for automated resume screening

### Phase 6 — Dockerization (Optional)
- Containerize the app for **easy deployment**
- Run the API anywhere without worrying about environment setup

---

## Setup Instructions

1. **Clone the repository**:

```bash
git clone https://github.com/ShivanshikaAgarwal1505/Intelligent-Resume-Screener.git
cd Intelligent-Resume-Screener
```

2. Create and activate virtual environment:
```bash
python -m venv venv
venv\Scripts\activate   # Windows
source venv/bin/activate # Linux/Mac
```
3. Install dependencies:
```bash
pip install -r requirements.txt
```
4. Run the app:
```bash
python app.py
```
4. Test APIs via Postman:
- POST /upload_resume → Upload resume
- POST /match → Get match score

---

## API Endpoints
| Endpoint         | Method | Description                                      |
|-----------------|--------|--------------------------------------------------|
| /upload_resume  | POST   | Upload a resume PDF and extract text           |
| /match          | POST   | Compare resume text with job description and return match score |

---

## Future Enhancements
- Integrate LLM explanations
- Train deep learning model for skill extraction
- Add job description upload
