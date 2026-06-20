import streamlit as st
from utils.auth import save_profile
from utils.profile_score import build_profile

st.title("👤 Student Profile")


if "logged_in" not in st.session_state:
    st.warning("Please Login First")
    st.stop()

name = st.text_input(
    "Name",
    value=st.session_state.get(
        "name",
        ""
    )
)

degree = st.text_input(
    "Degree",
    value=st.session_state.get(
        "degree",
        ""
    )
)

branch = st.text_input(
    "Branch",
    value=st.session_state.get(
        "branch",
        ""
    )
)
year = st.selectbox(
    "Year",
    ["1st", "2nd", "3rd", "4th"]
)

cgpa = st.number_input(
    "CGPA",
    min_value=0.0,
    max_value=10.0,
    value=float(
        st.session_state.get(
            "cgpa",
            0.0
        )
    ),
    step=0.01
)

# Auto-load skills from Resume Upload page
skills = st.text_area(
    "Skills",
    value=st.session_state.get("skills", "")
)

interests = st.multiselect(
    "Domains",
    [
        "AI/ML",
        "Software",
        "Government",
        "Research",
        "Cyber Security",
        "Data Science"
    ]
)
profile = {
    "skills": str(skills),
    "cgpa": float(cgpa)
}

score = build_profile(profile)

st.subheader("📊 Profile Strength")

st.progress(score / 100)

st.metric(
    "Profile Score",
    f"{score}/100"
)
if st.button("Save Profile"):

    save_profile(
        st.session_state.user_id,
        name,
        degree,
        branch,
        year,
        cgpa,
        skills,
        ",".join(interests)
    )

    st.session_state["interests"] = ",".join(interests)


    st.success(
        "✅ Profile Saved Successfully"
    )