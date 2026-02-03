def generate_clinical_pathway(symptoms, history):
    steps = []

    if "fever" in symptoms.lower():
        steps.append("Step 1: Check temperature regularly.")
        steps.append("Step 2: Increase hydration.")
        steps.append("Step 3: Rest for 24 hours.")
        steps.append("Step 4: Avoid heavy activity.")

    if "breathing" in symptoms.lower():
        steps.append("Step 1: Sit upright to ease breathing.")
        steps.append("Step 2: Avoid dust and cold air.")
        steps.append("Step 3: Use inhaler if prescribed.")

    if not steps:
        steps.append("Step 1: Monitor symptoms and rest.")

    return steps
