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

elif score >= 60:

    st.warning(
        "Good profile. Build more projects and apply actively."
    )

else:

    st.error(
        "Needs improvement before applying to competitive internships."
    )

st.subheader("📌 Recommended Next Steps")

if "python" not in skills:
    st.write("✓ Learn Python")

if "machine learning" not in skills:
    st.write("✓ Learn Machine Learning")

if "deep learning" not in skills:
    st.write("✓ Learn Deep Learning")

if cgpa < 8.5:
    st.write("✓ Improve CGPA above 8.5")

st.write("✓ Build 2–3 AI/ML Projects")
st.write("✓ Practice Aptitude and DSA")
st.write("✓ Apply for DRDO, ISRO, CDAC, NIC internships")