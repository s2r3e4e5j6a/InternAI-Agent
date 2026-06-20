import streamlit as st
import pandas as pd

from utils.matcher import rank_internship
from utils.eligibility_agent import check_eligibility

st.title("🎯 AI Internship Recommendations")

# User Profile
profile = {
    "skills": st.session_state.get(
        "skills",
        ""
    ),
    "cgpa": st.session_state.get(
        "cgpa",
        0
    ),
    "interests": st.session_state.get(
        "interests",
        ""
    )
}

# Load internships
df = pd.read_csv(
    "data/internships.csv"
)

scores = []

for _, row in df.iterrows():

    if check_eligibility(
        profile,
        row
    ):

        score = rank_internship(
            profile,
            row
        )

    else:

        score = 0

    scores.append(score)

df["Match Score"] = scores

df = df.sort_values(
    "Match Score",
    ascending=False
)

st.subheader("🏆 Top Recommended Internships")

for _, row in df.iterrows():

    st.markdown(
        f"### {row['Lab']}"
    )

    st.write(
        f"📍 {row['Location']}"
    )

    st.metric(
        "Match Score",
        f"{row['Match Score']}"
    )

    st.write(
        f"Eligibility: {row['Eligibility']}"
    )

    st.divider()