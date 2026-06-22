import streamlit as st
import sqlite3
import pandas as pd

from agents.profile_agent import build_profile
from agents.discovery_agent import discover_opportunities
from agents.eligibility_agent import check_eligibility
from agents.ranking_agent import rank_internship
from agents.career_agent import career_advice

st.title("🎯 AI Internship Recommendations")

# ==========================
# LOGIN CHECK
# ==========================

if not st.session_state.get("logged_in"):
    st.warning("Please Login First")
    st.stop()

# ==========================
# LOAD PROFILE
# ==========================

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

    st.warning(
        "Please Complete Your Profile"
    )

    st.stop()

profile = {
    "cgpa": profile_df.iloc[0]["cgpa"],
    "skills": profile_df.iloc[0]["skills"],
    "interests": profile_df.iloc[0]["interests"]
}

# ==========================
# PROFILE SCORE
# ==========================

profile_score = build_profile(profile)

if isinstance(profile_score, dict):
    profile_score = profile_score["profile_score"]

st.metric(
    "Profile Score",
    profile_score
)

# ==========================
# LOAD INTERNSHIPS
# ==========================


internships = discover_opportunities()

internships["cgpa_required"] = internships[
    "cgpa_required"
].fillna(7.0)

internships["skills_required"] = internships[
    "skills_required"
].fillna("")



# ==========================
# ELIGIBILITY ANALYTICS
# ==========================

eligible = 0
partial = 0
not_eligible = 0

recommendations = []

for _, internship in internships.iterrows():

    result = check_eligibility(
        profile["cgpa"],
        profile["skills"],
        internship["cgpa_required"],
        internship["skills_required"]
    )

    if result["status"] == "Eligible":

        eligible += 1

    elif result["status"] == "Partial Match":

        partial += 1

    else:

        not_eligible += 1

    if result["status"] != "Not Eligible":

        score, reasons = rank_internship(
            profile,
            internship
        )

        recommendations.append(
            (
                score,
                internship,
                reasons
            )
        )

# ==========================
# SORT RECOMMENDATIONS
# ==========================

best_score = recommendations[0][0]

st.metric(
    "Best Match",
    f"{best_score}%"
)
recommendations.sort(
    reverse=True,
    key=lambda x: x[0]
)
if len(recommendations) == 0:

    st.warning(
        "No internships match your profile currently."
    )

    st.stop()

best_score = recommendations[0][0]

st.metric(
    "Best Match",
    f"{best_score}%"
)
# ==========================
# ANALYTICS DISPLAY
# ==========================

st.subheader(
    "📊 Eligibility Analytics"
)

col1, col2, col3 = st.columns(3)

with col1:

    st.metric(
        "Eligible",
        eligible
    )

with col2:

    st.metric(
        "Partial Match",
        partial
    )

with col3:

    st.metric(
        "Not Eligible",
        not_eligible
    )

# ==========================
# TOP RECOMMENDATIONS
# ==========================

st.subheader(
    "🏆 Top Recommended Internships"
)

for score, internship, reasons in recommendations[:10]:

    st.write(
        f"### {internship['Lab']}"
    )

    st.write(
        f"📍 {internship['Location']}"
    )

    st.write(
        f"🎯 Match Score: {score}"
    )
    if score >= 85:

        st.success(
            "Highly Recommended"
        )

    elif score >= 70:

        st.warning(
            "Recommended"
        )

    else:

        st.info(
            "Consider Applying"
        )
    if reasons:

        for reason in reasons:

            st.write(
                f"✓ {reason}"
            )

    st.divider()

# ==========================
# CAREER COACH
# ==========================

st.subheader(
    "💡 Personalized Career Advice"
)

advice = career_advice(
    profile
)

for item in advice:

    st.success(item)

if profile["cgpa"] >= 8.5:

    st.success(
        "Eligible for DRDO / ISRO / BARC Research Internships"
    )