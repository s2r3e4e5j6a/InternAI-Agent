import streamlit as st
import pandas as pd

from utils.matcher import rank_internship

st.title("🎯 AI Internship Recommendations")

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

df = pd.read_csv(
    "data/internships.csv"
)

scores = []

for _, row in df.iterrows():

    score = rank_internship(
        profile,
        row
    )

    scores.append(score)

df["Match Score"] = scores

df = df.sort_values(
    "Match Score",
    ascending=False
)

st.dataframe(
    df[
        [
            "Lab",
            "Location",
            "Eligibility",
            "Match Score"
        ]
    ],
    use_container_width=True
)