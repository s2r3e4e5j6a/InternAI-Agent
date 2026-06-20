import streamlit as st

st.title("🎓 AI Career Coach")

skills = st.session_state.get("skills", "")

st.subheader("Current Skills")
st.write(skills)

missing_skills = []

if "Python" not in skills:
    missing_skills.append("Python")

if "SQL" not in skills:
    missing_skills.append("SQL")

if "Machine Learning" not in skills:
    missing_skills.append("Machine Learning")

if "Data Structures" not in skills:
    missing_skills.append("Data Structures")

st.subheader("Recommended Skills")

if missing_skills:
    for skill in missing_skills:
        st.write("❌", skill)
else:
    st.success("You already have strong skills!")

st.subheader("Recommended Certifications")

st.write("🎖 Google Data Analytics")
st.write("🎖 AWS Cloud Practitioner")
st.write("🎖 Microsoft AI Fundamentals")