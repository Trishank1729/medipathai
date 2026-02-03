def check_drug_interactions(meds):
    risky_pairs = [
        ("paracetamol", "alcohol"),
        ("ibuprofen", "blood thinner"),
        ("antibiotic", "antacid"),
    ]

    meds_list = [m.strip().lower() for m in meds.split(",")]

    warnings = []
    for m1 in meds_list:
        for m2 in meds_list:
            if (m1, m2) in risky_pairs:
                warnings.append(f"Interaction risk between {m1} and {m2}")

    return warnings if warnings else "No interactions detected."
