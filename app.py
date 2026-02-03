import streamlit as st
import json
from datetime import datetime

# LLM + Prompting
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

# Engines
from user_manager import register_user, authenticate_user, load_database, save_database
from clinical_pathway_engine import generate_clinical_pathway
from drug_interaction_engine import check_drug_interactions
from redflag_engine import detect_red_flags
from prediction_engine import predict_progression
from calendar_engine import generate_calendar_plot

# New Engines
from severity_engine import calculate_severity_and_recovery
from probability_engine import get_possible_conditions
from lab_test_engine import recommend_lab_tests

# ============================
# 🔐 LOAD API KEY FROM SECRETS
# ============================
GROQ_API_KEY = st.secrets["GROQ_API_KEY"]

# ============================
# 🔽 SIMPLE PATHWAY CLEANER
# ============================
def simplify_pathway(pathway):
    simple_steps = []
    for step in pathway:
        cleaned = step.replace("Step", "").replace(":", "").strip()
        words = cleaned.split()
        short = " ".join(words[:4]) + "..."
        simple_steps.append(short)
    return simple_steps

# ============================
# 🤖 LLM SETUP
# ============================
llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    api_key=GROQ_API_KEY
)

parser = StrOutputParser()

prompt = ChatPromptTemplate.from_messages([
    ("system",
    """
    You are MediPathAI v3 — a safe medical guide.
    Always give simple, easy-to-understand answers.

    Rules:
    - Use bullet points
    - Do NOT diagnose or prescribe
    - Avoid medical jargon
    - Keep explanations simple
    """),

    ("user",
    """
    Symptoms: {symptoms}
    Medical History: {history}
    Medications: {meds}

    Clinical Pathway: {pathway}
    Prediction: {prediction}
    Red Flags: {redflags}

    Severity: {severity}
    Recovery Time: {recovery}
    Possible Conditions: {conditions}
    Lab Tests: {labtests}

    Explain everything very simply.
    """)
])

chain = prompt | llm | parser

# ============================
# UI SETUP
# ============================
st.set_page_config(layout="wide", page_title="MediPathAI v3")
st.title("🧠 MediPathAI v3 — Advanced Clinical Intelligence System")

db = load_database()

# ============================
# LOGIN SYSTEM
# ============================
menu = ["Login", "Register"]
choice = st.sidebar.selectbox("Account", menu)

if "user" not in st.session_state:
    st.session_state.user = None

# REGISTER
if choice == "Register":
    st.subheader("Create Account")
    new_user = st.text_input("Username")
    new_pass = st.text_input("Password", type="password")

    if st.button("Register"):
        if register_user(new_user, new_pass):
            st.success("Account created! Please login.")
        else:
            st.error("Username already exists.")

# LOGIN
elif choice == "Login":
    st.subheader("Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if authenticate_user(username, password):
            st.session_state.user = username
            st.success(f"Welcome {username}!")
        else:
            st.error("Invalid username or password")

if not st.session_state.user:
    st.stop()

# ============================
# MAIN APP
# ============================
st.success(f"Logged in as: {st.session_state.user}")

col1, col2 = st.columns([1.5, 1])

# ============================
# LEFT PANEL — INPUT
# ============================
with col1:
    st.header("💬 Describe Your Symptoms")

    symptoms = st.text_area("Symptoms:")
    history = st.text_input("Medical History:")
    meds = st.text_input("Medications (comma separated):")

    if st.button("Analyze"):

        # Engines
        pathway = generate_clinical_pathway(symptoms, history)
        simple_pathway = simplify_pathway(pathway)

        interactions = check_drug_interactions(meds)
        redflags = detect_red_flags(symptoms)
        prediction = predict_progression(symptoms)

        # New engines
        severity, recovery = calculate_severity_and_recovery(symptoms)
        conditions = get_possible_conditions(symptoms)
        labtests = recommend_lab_tests(symptoms)

        # LLM response
        response = chain.invoke({
            "symptoms": symptoms,
            "history": history,
            "meds": meds,
            "pathway": simple_pathway,
            "prediction": prediction,
            "redflags": redflags,
            "severity": severity,
            "recovery": recovery,
            "conditions": conditions,
            "labtests": labtests
        })

        # ============================
        # FIXED — SAVE HISTORY CORRECTLY
        # ============================
        db = load_database()
        db["users"][st.session_state.user]["history"].append({
            "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "symptoms": symptoms,
            "pathway": simple_pathway,
            "severity": severity,
            "prediction": prediction
        })

        save_database(db)   # <— FIXED (prevents wrong file paths)

        # ============================
        # DISPLAY RESULTS
        # ============================
        st.subheader("🧠 AI Summary")
        st.markdown(response)

        st.subheader("📊 Severity & Recovery")
        st.markdown(f"- **Severity:** {severity}/10")
        st.markdown(f"- **Recovery Time:** {recovery}")

        st.subheader("🩺 Clinical Pathway")
        for step in simple_pathway:
            st.markdown(f"- {step}")

        st.subheader("⚠️ Drug Interaction Warnings")
        if isinstance(interactions, list):
            for i in interactions:
                st.markdown(f"- {i}")
        else:
            st.markdown(interactions)

        st.subheader("🚨 Red Flags")
        if redflags:
            for r in redflags:
                st.markdown(f"- {r}")
        else:
            st.markdown("✔ No red flags detected.")

        st.subheader("🔍 Possible Conditions")
        for c in conditions:
            st.markdown(f"- {c}")

        st.subheader("🧪 Recommended Lab Tests")
        for t in labtests:
            st.markdown(f"- {t}")

# ============================
# RIGHT PANEL — CALENDAR & HISTORY
# ============================
with col2:
    st.header("📅 Health Calendar")
    fig = generate_calendar_plot(st.session_state.user)
    if fig:
        st.pyplot(fig)
    else:
        st.info("Not enough history to plot.")

    st.header("📜 Medical History (Simple)")
    user_data = db["users"][st.session_state.user]["history"]

    if user_data:
        for entry in user_data:
            st.markdown(f"""
            **📅 Date:** {entry['date']}  
            **📝 Symptoms:** {entry['symptoms']}  
            **📌 Pathway:**  
            {"<br>".join([f"- {p}" for p in entry['pathway']])}  
            **🔥 Severity:** {entry['severity']}/10  
            **🔮 Prediction:** {entry['prediction']}  
            ---
            """, unsafe_allow_html=True)
    else:
        st.info("No medical history yet.")
