# severity_engine.py

def calculate_severity_and_recovery(symptoms: str):
    symptoms = symptoms.lower()

    severity_score = 0

    # High severity keywords
    high_keywords = ["severe", "difficulty breathing", "chest pain", "very weak", "high fever", "worsening"]
    for word in high_keywords:
        if word in symptoms:
            severity_score += 3

    # Medium severity
    medium_keywords = ["fever", "cough", "body pain", "vomiting", "headache"]
    for word in medium_keywords:
        if word in symptoms:
            severity_score += 2

    # Mild severity
    mild_keywords = ["mild", "slight", "little"]
    for word in mild_keywords:
        if word in symptoms:
            severity_score += 1

    # Cap severity at 10
    severity_score = min(severity_score, 10)

    # Recovery estimation
    if severity_score >= 8:
        recovery = "5–7 days (condition appears serious)"
    elif severity_score >= 5:
        recovery = "3–5 days (moderate condition)"
    elif severity_score >= 2:
        recovery = "2–3 days (mild condition)"
    else:
        recovery = "1–2 days (almost normal)"

    return severity_score, recovery
