# probability_engine.py

def get_possible_conditions(symptoms: str):
    symptoms = symptoms.lower()
    results = []

    if "fever" in symptoms:
        results.append("Viral infection (high)")
        results.append("Flu (medium)")

    if "cough" in symptoms:
        results.append("Common cold (high)")
        results.append("Bronchitis (low)")

    if "difficulty breathing" in symptoms:
        results.append("Respiratory inflammation (medium)")

    if "headache" in symptoms:
        results.append("Migraine or stress-related (medium)")

    if not results:
        results.append("General fatigue or minor illness (low)")

    return results
