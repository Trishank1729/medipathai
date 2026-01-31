import json
from user_manager import load_database

def predict_progression(symptoms_text):
    """
    Predicts short-term symptom progression based on:
    1. Current symptom severity keywords
    2. User's previous symptom logs
    Returns "improving", "worsening", or "stable" with explanation.
    """

    if not symptoms_text or symptoms_text.strip() == "":
        return "Not enough data to predict progression."

    symptoms = symptoms_text.lower()

    severity_keywords = {
        "worsening": ["severe", "increasing", "persistent", "worse", "spreading"],
        "improving": ["mild", "improving", "better", "reduced"],
        "stable":    ["same", "unchanged", "manageable"]
    }

    # ---------------------- CHECK CURRENT SYMPTOMS ----------------------
    score = 0

    for word in severity_keywords["worsening"]:
        if word in symptoms:
            score += 2

    for word in severity_keywords["improving"]:
        if word in symptoms:
            score -= 2

    for word in severity_keywords["stable"]:
        if word in symptoms:
            score += 0

    # ---------------------- INTERPRET CURRENT STATUS ----------------------
    if score >= 2:
        status = "worsening"
    elif score <= -2:
        status = "improving"
    else:
        status = "stable"

    explanation = f"Based on symptom description, your condition appears to be **{status}**."

    return explanation
