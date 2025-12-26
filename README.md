# Resume Screening System 

A **smart resume screening system** built with **Flask**, **React**, and **sentence-transformers** for AI-powered resume matching.  
The system uses **bi-encoder and cross-encoder embeddings** along with **skill extraction** to evaluate resumes against job descriptions.

---

## Demo

<img width="1180" height="684" alt="image" src="https://github.com/user-attachments/assets/aafd0b35-a723-41b9-9dd6-1fbdd9c72a76" />
<img width="1146" height="523" alt="image" src="https://github.com/user-attachments/assets/491736bd-5a60-4e59-ba4d-deb2f1be467f" />
<img width="1214" height="673" alt="image" src="https://github.com/user-attachments/assets/30b06240-3e51-4245-a4de-ccc58af9490f" />

---

## Features

- Upload resume as **PDF** or **paste as text**
- Match against job descriptions
- **Hybrid Matching**: Bi-Encoder + Cross-Encoder + Skill Overlap
- **Explainable AI**: Detailed reasoning for match scores
- Verdict: Strong / Moderate / Weak match
- Dark theme UI with spinner while processing

---

## Tech Stack

- **Backend**: Python, Flask, Flask-CORS
- **Frontend**: React, Axios
- **AI Models**: `sentence-transformers` (`all-MiniLM-L6-v2`, `cross-encoder/ms-marco-MiniLM-L-6-v2`)
- **PDF Parsing**: pypdf
---

## Installation

### 1. Clone Repository
```bash
git clone https://github.com/your-username/resume-screening-system.git
cd resume-screening-system/backend
```

### 2. Setup Python Virtual Environment
```bash
python -m venv .venv
.venv\Scripts\activate   # Windows
# source .venv/bin/activate   # macOS/Linux
```

### 3. Install Backend Dependencies
```bash
pip install -r requirements.txt
```

### 4. Start Backend
```bash
python app.py
```
API will run at: http://127.0.0.1:5000

### 5. Setup Frontend
```bash
cd ../frontend
npm install
npm start
```
Frontend will run at: http://localhost:3000

---

## API Endpoints

### POST `/match`

**JSON Request:**

```json
{
  "resume_text": "Paste resume here...",
  "job_text": "Paste job description here..."
}
```

**FormData Request (PDF Upload):**

```
resume_file: <file.pdf>
job_text: "Paste job description here..."
```

**Response:**

```json
{
  "final_score": 80.67,
  "bi_encoder_score": 51.88,
  "cross_encoder_score": 99.83,
  "skill_match_score": 100.0,
  "matched_skills": ["coaching", "communication", "organization", "sports equipment knowledge", "teamwork", "cash handling", "customer service"],
  "explanation": "Good alignment with most job requirements. Very strong contextual understanding detected. Key matching skills include coaching, communication, organization, sports equipment knowledge, teamwork, cash handling, customer service.",
  "verdict": "Moderate Match",
  "confidence": "Medium"
}
```

---

## Configuration

**Verdict thresholds** (`services/config.py`):

```python
VERDICT_THRESHOLDS = {
    "strong": 85,
    "moderate": 65,
    "weak": 0
}
```

**Hybrid Matcher Weights**:

```python
HYBRID_WEIGHTS = {
    "bi_encoder": 0.4,
    "cross_encoder": 0.5,
    "skill_overlap": 0.1
}
```

> Adjust weights and thresholds to tune matching behavior.

---

## Folder Structure

```
backend/
├─ services/
│  ├─ embeddings.py
│  ├─ matcher.py
│  ├─ cross_encoder.py
│  ├─ hybrid_matcher.py
│  ├─ skill_extractor.py
│  ├─ parser.py
│  ├─ explainer.py
│  └─ config.py
├─ app.py
├─ requirements.txt
frontend/
├─ src/
│  ├─ App.jsx
│  ├─ App.css
│  └─ ...
```

---

## How it Works

1. **Resume Input**: PDF upload or text paste  
2. **Job Input**: Text field for job description  
3. **Hybrid Matching**:
   - Bi-Encoder computes semantic similarity  
   - Cross-Encoder captures contextual relevance  
   - Skill overlap is calculated from extracted skills  
4. **Score Aggregation**: Weighted sum of all three components  
5. **Verdict**: Strong / Moderate / Weak match based on thresholds  
6. **Explanation**: Human-readable explanation with matched skills  

---

## Setup

### Backend

```bash
cd backend
python -m venv .venv
source .venv/Scripts/activate   # Windows
pip install -r requirements.txt
python app.py
```

### Frontend

```bash
cd frontend
npm install
npm start
```

---

## Contributing

1. Fork the repo  
2. Create your feature branch (`git checkout -b feature-name`)  
3. Commit your changes (`git commit -m "Add feature"`)  
4. Push to branch (`git push origin feature-name`)  
5. Create a pull request  

---

## License

MIT License © 2025
