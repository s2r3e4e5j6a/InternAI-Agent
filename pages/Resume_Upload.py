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

    # Save PDF
    with open(
        "uploaded_resume.pdf",
        "wb"
    ) as f:

        f.write(
            uploaded_file.read()
        )

    # Extract text
    text = extract_text(
        "uploaded_resume.pdf"
    )

    # Extract profile details
    profile = extract_profile(text)

    st.session_state["name"] = profile["name"]
    st.session_state["degree"] = profile["degree"]
    st.session_state["branch"] = profile["branch"]
    st.session_state["cgpa"] = profile["cgpa"]

    # Show extracted profile
    st.subheader("👤 Detected Profile")

    st.write(
        f"**Name:** {profile['name']}"
    )

    st.write(
        f"**Degree:** {profile['degree']}"
    )

    st.write(
        f"**Branch:** {profile['branch']}"
    )

    st.write(
        f"**CGPA:** {profile['cgpa']}"
    )

    # Extract skills
    skills = extract_skills(text)

    skills_text = ", ".join(skills)

    st.session_state["skills"] = skills_text

    st.subheader("🎯 Extracted Skills")

    st.success(
        "Resume Parsed Successfully"
    )

    st.write(skills_text)

    st.subheader(
        "📄 Extracted Resume Text"
    )

    st.text_area(
        "Resume Content",
        text,
        height=300
    )