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

drdo_score = 0

if "python" in skills:
    drdo_score += 25

if "machine learning" in skills:
    drdo_score += 25

if cgpa >= 8.5:
    drdo_score += 50

st.metric(
    "DRDO Readiness",
    f"{drdo_score}%"
)

if drdo_score < 100:

    st.warning(
        "Learn Research Methodology and Publications"
    )

else:

    st.success(
        "Excellent DRDO Profile"
    )