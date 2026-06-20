import streamlit as st
import sqlite3
import pandas as pd

from agents.profile_agent import build_profile
from agents.discovery_agent import discover_opportunities
from agents.eligibility_agent import check_eligibility
from agents.ranking_agent import rank_internship
from agents.career_agent import career_advice

st.title("🎯 AI Internship Recommendations")

if "user_id" not in st.session_state:
    st.warning("Please Login First")
    st.stop()

conn = sqlite3.connect("database/users.db")

profile_df = pd.read_sql_query(
    """
    SELECT *
    FROM profiles
    WHERE user_id=?
    ORDER BY id DESC
    LIMIT 1
    """,
    conn,
    params=(st.session_state.user_id,)
)

conn.close()

if profile_df.empty:
    st.warning("Please Complete Your Profile")
    st.stop()

profile = {
    "cgpa": profile_df.iloc[0]["cgpa"],
    "skills": profile_df.iloc[0]["skills"],
    "interests": profile_df.iloc[0]["interests"]
}

profile_result = build_profile(profile)

internships = discover_opportunities()

recommendations = []
st.write(df.columns)
for _, internship in internships.iterrows():

    if check_eligibility(profile, internship):

        score, reasons = rank_internship(
            profile,
            internship
        )

        recommendations.append(
            (
                score,
                internship
            )
        )

recommendations.sort(
    reverse=True,
    key=lambda x: x[0]
)

st.subheader("🏆 Top Recommended Internships")

for score, internship in recommendations[:5]:

    st.write(
        f"### {internship['Lab']}"
    )

    st.write(
        f"📍 {internship['Location']}"
    )

    st.write(
        f"🎯 Match Score: {score:.1f}"
    )
    for reason in reasons:
        st.write(f"✓ {reason}")

    st.write("---")

st.subheader("💡 Career Advice")

st.success(
    career_advice(profile)
)
if profile["cgpa"] >= 8.5:
    st.success(
        "Eligible for DRDO/ISRO Research Internships"
    )