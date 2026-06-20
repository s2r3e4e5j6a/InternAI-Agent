import streamlit as st

from utils.resume_parser import (
    extract_text,
    extract_skills,
    extract_profile
)

st.title("📄 Resume Upload")

uploaded_file = st.file_uploader(
    "Upload Resume",
    type=["pdf"]
)

if uploaded_file:

    with open("uploaded_resume.pdf", "wb") as f:
        f.write(uploaded_file.read())

    text = extract_text("uploaded_resume.pdf")

    profile = extract_profile(text)

    st.session_state["name"] = profile["name"]
    st.session_state["degree"] = profile["degree"]
    st.session_state["branch"] = profile["branch"]
    st.session_state["cgpa"] = profile["cgpa"]

    skills = extract_skills(text)

    st.subheader("🎯 Extracted Skills")

    skills_text = ", ".join(skills)

    st.success("Skills extracted successfully!")

    st.session_state["skills"] = skills_text

    st.write(skills_text)

    st.subheader("📄 Extracted Resume Text")

    st.text_area(
        "Resume Content",
        text,
        height=300
    )