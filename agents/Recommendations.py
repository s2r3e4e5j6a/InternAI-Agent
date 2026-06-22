import streamlit as st
import pandas as pd
from utils.profile_db import get_profile
from utils.matcher import rank_internship
from utils.eligibility_agent import check_eligibility

st.title("🎯 AI Internship Recommendations")
db_profile = get_profile(
    st.session_state.user_id
)

profile = {
    "skills": db_profile[7],
    "cgpa": db_profile[6],
    "interests": db_profile[8]
}
st.write(profile)

df = pd.read_csv(
    "data/internships.csv"
)

df["cgpa_required"] = df[
    "cgpa_required"
].fillna(7.0)

df["skills_required"] = df[
    "skills_required"
].fillna("")

results = []

for _, row in df.iterrows():
    result = check_eligibility(
        profile["cgpa"],
        profile["skills"],
        row["cgpa_required"],
        row["skills_required"]
    )

    status = result["status"]

    if status != "Not Eligible":

        score, reasons = rank_internship(
            profile,
            row
        )

    else:

        score = 0
        reasons = []

    results.append(
        (
            score,
            status,
            reasons,
            row
        )
    )

results.sort(
    reverse=True,
    key=lambda x: x[0]
)

st.subheader(
    "🏆 Top Recommended Internships"
)

for score, status, reasons, row in results[:10]:

    st.markdown(
        f"### {row['Lab']}"
    )

    st.write(
        f"📍 {row['Location']}"
    )

    if status == "Eligible":

        st.success(
            "✅ Eligible"
        )

    elif status == "Partial Match":

        st.warning(
            "🟡 Partial Match"
        )

    else:

        st.error(
            "❌ Not Eligible"
        )

    st.metric(
        "Match Score",
        score
    )

    st.write(
        f"Eligibility: {row['Eligibility']}"
    )

    if reasons:

        st.write(
            "**Why Recommended:**"
        )

        for reason in reasons:

            st.write(
                f"✓ {reason}"
            )

    st.divider()