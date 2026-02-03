def detect_red_flags(symptoms):
    red_flags = []

    s = symptoms.lower()
    if "chest pain" in s:
        red_flags.append("Chest pain is a medical emergency.")
    if "shortness of breath" in s:
        red_flags.append("Difficulty breathing requires urgent evaluation.")
    if "severe headache" in s:
        red_flags.append("Sudden severe headache can be serious.")

    return red_flags
