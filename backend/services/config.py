# services/config.py

# Verdict thresholds
VERDICT_THRESHOLDS = {
    "strong": 85,
    "moderate": 65,
    "weak": 0  # anything below moderate
}

# Hybrid Matcher weights
HYBRID_WEIGHTS = {
    "bi_encoder": 0.4,
    "cross_encoder": 0.5,
    "skill_overlap": 0.1
}