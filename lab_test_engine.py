# lab_test_engine.py

def recommend_lab_tests(symptoms: str):
    symptoms = symptoms.lower()
    tests = []

    if "fever" in symptoms:
        tests.append("CBC (Complete Blood Count)")
        tests.append("CRP (Inflammation Marker)")

    if "difficulty breathing" in symptoms or "chest pain" in symptoms:
        tests.append("Chest X-Ray")
        tests.append("Pulse Oximeter Check")

    if "fatigue" in symptoms:
        tests.append("Thyroid (TSH) Test")

    if "vomiting" in symptoms:
        tests.append("Electrolyte Test")

    if not tests:
        tests.append("No lab tests needed based on symptoms")

    return tests
