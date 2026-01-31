# redflag_engine.py

def detect_red_flags(symptoms: str):
    symptoms = symptoms.lower()
    red_flags = []

    if "difficulty breathing" in symptoms or "shortness of breath" in symptoms:
        red_flags.append("Breathing difficulty (seek medical help if it worsens).")

    if "chest pain" in symptoms:
        red_flags.append("Chest pain detected (may need immediate attention).")

    if "unconscious" in symptoms or "fainting" in symptoms:
        red_flags.append("Fainting / unconsciousness (critical).")

    if "severe headache" in symptoms:
        red_flags.append("Severe headache (possible serious condition).")

    if "high fever" in symptoms:
        red_flags.append("High fever (monitor closely).")

    # If no red flags found; return empty list (not None)
    return red_flags
