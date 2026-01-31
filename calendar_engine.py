import matplotlib.pyplot as plt
from datetime import datetime
from user_manager import load_database

def generate_calendar_plot(username):
    """
    Generates a health trend line chart for the user.
    Symptom severity is inferred based on keywords.
    """

    db = load_database()

    if username not in db["users"]:
        return None

    history = db["users"][username]["history"]

    if not history:
        return None  # No data to plot

    dates = []
    severity_scores = []

    # Severity scoring keywords
    severe_keywords = ["severe", "worse", "worsening", "increasing", "high fever"]
    mild_keywords = ["mild", "improving", "better", "reduced"]
    
    for entry in history:
        date = entry["date"]
        symptoms = entry["symptoms"].lower()

        score = 0

        for word in severe_keywords:
            if word in symptoms:
                score += 2
        
        for word in mild_keywords:
            if word in symptoms:
                score -= 1

        dates.append(datetime.strptime(date, "%Y-%m-%d"))
        severity_scores.append(score)

    # ---------------------- PLOT ----------------------
    fig, ax = plt.subplots(figsize=(6, 4))
    ax.plot(dates, severity_scores, marker='o', linewidth=2)

    ax.set_title("Health Trend Calendar")
    ax.set_xlabel("Date")
    ax.set_ylabel("Symptom Severity Score")
    ax.grid(True)

    return fig
