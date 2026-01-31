def generate_clinical_pathway(symptoms, history):
    """
    Generates a clinical pathway based on symptoms and medical history.
    NO DIAGNOSIS. Only pathway suggestions.
    """

    symptoms = symptoms.lower()
    history = history.lower()

    pathway = []

    # ---------------------- EMERGENCY CHECK ----------------------
    if any(keyword in symptoms for keyword in [
        "chest pain", "severe breathlessness", "difficulty breathing", 
        "unconscious", "fainting", "stroke symptoms"
    ]):
        pathway.append("🔴 Step 1: Seek emergency medical care immediately.")
        pathway.append("🔴 Step 2: Avoid physical activity and stay calm.")
        return pathway

    # ---------------------- GENERAL PATHWAY ----------------------
    pathway.append("Step 1: Monitor symptoms for the next 24 hours.")
    pathway.append("Step 2: Maintain proper hydration and rest.")

    # Fever-related
    if "fever" in symptoms:
        pathway.append("Step 3: Take oral rehydration fluids and check temperature every 6 hours.")

    # Cough-related
    if "cough" in symptoms:
        pathway.append("Step 4: Try warm water steam inhalation twice a day.")

    # Cold/flu
    if "cold" in symptoms or "runny nose" in symptoms or "sore throat" in symptoms:
        pathway.append("Step 5: Warm salt-water gargling may help soothe the throat.")

    # Gastrointestinal
    if "vomit" in symptoms or "diarrhea" in symptoms:
        pathway.append("Step 6: ORS (oral rehydration solution) every few hours is recommended.")

    # Chronic disease modifiers
    if "diabetes" in history or "asthma" in history or "bp" in history:
        pathway.append("Step 7: Due to your medical history, consider consulting a doctor earlier if symptoms persist.")

    # Escalation
    pathway.append("Step 8: If symptoms worsen or do not improve in 48 hours, consult a doctor.")

    return pathway
