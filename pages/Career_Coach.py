import streamlit as st

st.title("🎓 Career Coach")

skills = st.session_state.get(
    "skills",
    ""
).lower()

cgpa = st.session_state.get(
    "cgpa",
    0
)

score = 0

if "python" in skills:
    score += 25

if "machine learning" in skills:
    score += 25

if cgpa >= 8.5:
    score += 50

st.metric(
    "Career Readiness",
    f"{score}%"
)

if score >= 80:

    st.success(
        "Excellent profile for AI and Research internships"
    )

else:

    st.warning(
        "Improve skills and projects"
    )