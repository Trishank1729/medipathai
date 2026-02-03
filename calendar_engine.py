import matplotlib.pyplot as plt
from datetime import datetime
from user_manager import load_database

def generate_calendar_plot(username):

    db = load_database()

    if username not in db["users"]:
        return None

    history = db["users"][username]["history"]

    if not history:
        return None

    dates = []
    severity_scores = []

    for entry in history:
        date_str = entry["date"]

        # Accept both "YYYY-MM-DD" and "YYYY-MM-DD HH:MM:SS"
        try:
            date_obj = datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S")
        except:
            date_obj = datetime.strptime(date_str, "%Y-%m-%d")

        dates.append(date_obj)

        # Use real severity score
        score = entry.get("severity", 0)
        if score == "N/A":
            score = 0

        severity_scores.append(score)

    fig, ax = plt.subplots(figsize=(6, 4))
    ax.plot(dates, severity_scores, marker='o', linewidth=2)

    ax.set_title("Health Trend Calendar")
    ax.set_xlabel("Date")
    ax.set_ylabel("Severity Score")
    ax.grid(True)

    return fig
