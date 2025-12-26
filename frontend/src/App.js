import React, { useState } from "react";
import axios from "axios";
import "./App.css";

function App() {
  const [resumeText, setResumeText] = useState("");
  const [jobText, setJobText] = useState("");
  const [selectedFile, setSelectedFile] = useState(null);
  const [loading, setLoading] = useState(false);
  const [result, setResult] = useState(null);
  const [error, setError] = useState("");

  const handleSubmit = async (e) => {
    e.preventDefault();
    setError("");
    setResult(null);

    if (!selectedFile && !resumeText) {
      setError("Please provide resume text or upload a PDF.");
      return;
    }

    if (!jobText) {
      setError("Please provide job description text.");
      return;
    }

    setLoading(true);

    try {
      let res;
      if (selectedFile) {
        const formData = new FormData();
        formData.append("resume_file", selectedFile);
        formData.append("job_text", jobText);

        res = await axios.post("http://127.0.0.1:5000/match", formData, {
          headers: { "Content-Type": "multipart/form-data" },
        });
      } else {
        res = await axios.post("http://127.0.0.1:5000/match", {
          resume_text: resumeText,
          job_text: jobText,
        });
      }

      setResult(res.data);
    } catch (err) {
      console.error(err);
      setError(
        err.response?.data?.error ||
          "Something went wrong. Please check your input and backend."
      );
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="app-container">
      <h1>Resume Screening System</h1>
      <form onSubmit={handleSubmit} className="form-container">
        <label>Resume Text (optional if uploading PDF)</label>
        <textarea
          value={resumeText}
          onChange={(e) => setResumeText(e.target.value)}
          placeholder="Paste your resume text here..."
        />

        <label>Or Upload Resume PDF</label>
        <input
          type="file"
          accept=".pdf"
          onChange={(e) => setSelectedFile(e.target.files[0])}
        />

        <label>Job Description Text</label>
        <textarea
          value={jobText}
          onChange={(e) => setJobText(e.target.value)}
          placeholder="Paste job description here..."
        />

        <button type="submit" disabled={loading}>
          {loading ? "Processing..." : "Match Resume"}
        </button>
      </form>

      {error && <div className="error-box">{error}</div>}

      {loading && <div className="spinner">Loading...</div>}

      {result && (
        <div className="result-box">
          <h2>Results</h2>
          <p>
            <strong>Final Score:</strong> {result.final_score}%
          </p>
          <p>
            <strong>Verdict:</strong> {result.verdict} ({result.confidence}{" "}
            confidence)
          </p>
          <p>
            <strong>Matched Skills:</strong>{" "}
            {result.matched_skills.length
              ? result.matched_skills.join(", ")
              : "None"}
          </p>
          <p>
            <strong>Explanation:</strong>
          </p>
          <pre className="explanation">{result.explanation}</pre>
        </div>
      )}
    </div>
  );
}

export default App;