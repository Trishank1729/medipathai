def check_drug_interactions(medications_text):
    """
    Checks for drug-drug and drug-food interactions.
    Returns warnings if detected.
    """

    if not medications_text or medications_text.strip() == "":
        return "No medications mentioned."

    meds = [m.strip().lower() for m in medications_text.split(",")]

    warnings = []

    # ---------------------- PREDEFINED INTERACTION DATABASE ----------------------
    drug_interactions = {
        ("ibuprofen", "warfarin"): "High bleeding risk when Ibuprofen is taken with Warfarin.",
        ("aspirin", "warfarin"): "Increased bleeding risk with Aspirin + Warfarin.",
        ("metformin", "alcohol"): "Alcohol increases risk of lactic acidosis with Metformin.",
        ("paracetamol", "alcohol"): "Frequent alcohol use increases liver strain with Paracetamol.",
        ("azithromycin", "antacids"): "Antacids reduce the effectiveness of Azithromycin.",
    }

    # ---------------------- DRUG–FOOD INTERACTIONS ----------------------
    food_interactions = {
        "grapefruit": ["statins", "amlodipine", "colchicine"],
        "alcohol": ["metformin", "paracetamol", "ibuprofen"]
    }

    # ---------------------- DRUG–DRUG CHECK ----------------------
    for d1 in meds:
        for d2 in meds:
            if d1 == d2:
                continue
            
            key = tuple(sorted([d1, d2]))
            if key in drug_interactions:
                warnings.append(f"⚠️ {drug_interactions[key]}")

    # ---------------------- DRUG–FOOD CHECK ----------------------
    for food, affected_drugs in food_interactions.items():
        for drug in meds:
            if drug in affected_drugs:
                warnings.append(f"⚠️ {drug.capitalize()} interacts with {food}.")

    if warnings:
        return warnings

    return "No known interactions found based on provided medications."
