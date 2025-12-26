def generate_explanation(result):
    score = result["final_score"]
    skills = result["matched_skills"]
    cross = result["cross_encoder_score"]

    explanation = []

    if score >= 85:
        explanation.append("Excellent overall match between resume and job description.")
    elif score >= 70:
        explanation.append("Good alignment with most job requirements.")
    else:
        explanation.append("Partial match with room for improvement.")

    if cross >= 90:
        explanation.append("Very strong contextual understanding detected.")
    elif cross >= 75:
        explanation.append("Good contextual similarity between resume and role.")

    if skills:
        explanation.append(
            f"Key matching skills include {', '.join(skills)}."
        )
    else:
        explanation.append("No major skill overlap detected.")

    return " ".join(explanation)