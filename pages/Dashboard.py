import streamlit as st
import pandas as pd
import subprocess
st.set_page_config(
    page_title="AI Government Opportunity Tracker",
    page_icon="🚀",
    layout="wide"
)

if not st.session_state.get("logged_in"):
    st.warning("Please Login First")
    st.stop()

st.title("📊 Internship Dashboard")

st.success(
    f"Welcome {st.session_state.username}"
)


from utils.profile_db import get_profile
from utils.profile_score import build_profile
from utils.profile_db import get_profile

profile = get_profile(
    st.session_state.user_id
)

st.write(profile)
profile_score = build_profile(profile)

st.metric(
    "Profile Score",
    profile_score
)

if profile:

    st.write(
        f"CGPA: {profile[6]}"
    )

    st.write(
        f"Skills: {profile[7]}"
    )

    st.write(
        f"Interests: {profile[8]}"
    )
# ==================================
# LOGIN SYSTEM
# ==================================

# ==================================
# PAGE CONFIG
# ==================================



st.info(
    "Track DRDO, ISRO and BARC internship opportunities in one dashboard."
)

# ==================================
# ACTION BUTTONS
# ==================================

col1, col2 = st.columns(2)

with col1:
    if st.button("🔄 Refresh Internship Data"):
        subprocess.run(["python", "scraper.py"])
        st.success("Internship data updated!")

with col2:
    if st.button("📧 Send Internship Report"):
        import email_alert
        st.success("Internship report sent successfully!")

# ==================================
# LOAD DATA
# ==================================

df = pd.read_csv("data/internships.csv")
df.columns = df.columns.str.strip()


df.columns = df.columns.str.strip()

if "Status" not in df.columns:
    df["Status"] = "Open"

df["Status"] = df["Status"].fillna("Open")

df["Deadline"] = pd.to_datetime(
    df["Deadline"],
    errors="coerce"
)

today = pd.Timestamp.today().normalize()

df["Days Left"] = (
    df["Deadline"] - today
).dt.days

df["Days Left"] = df["Days Left"].fillna(-1)
# ==================================
# FILTERS
# ==================================

source_filter = st.selectbox(
    "Filter by Organization",
    ["All", "DRDO", "ISRO", "BARC", "HAL", "BEL"]
)

search = st.text_input(
    "Search by Lab or Location"
)

status_filter = st.selectbox(
    "Filter by Status",
    ["All", "Open", "Closing Soon", "Expired"]
)

# ==================================
# TITLE
# ==================================

st.title("🚀 AI Government Opportunity Tracker")

# ==================================
# ADD INTERNSHIP
# ==================================


# ==================================
# ADD INTERNSHIP
# ==================================

st.subheader("Add New Internship")


with st.form("internship_form"):

    lab = st.text_input("Lab Name")

    location = st.text_input("Location")

    eligibility = st.text_input("Eligibility")

    deadline = st.date_input("Deadline")

    submit = st.form_submit_button(
        "➕ Add Internship"
    )

if submit:

    days_left = (
        pd.to_datetime(deadline)
        - pd.Timestamp.today()
    ).days

    if days_left < 0:

        status = "Expired"

    elif days_left <= 15:

        status = "Closing Soon"

    else:

        status = "Open"
    

    new_row = pd.DataFrame({
        "Lab": [lab],
        "Location": [location],
        "Eligibility": [eligibility],
        "Deadline": [deadline],
        "Source": ["Manual Entry"],
        "Status": [status]
    })

    df_save = pd.read_csv(
        "data/internships.csv"
    )

    df_save = pd.concat(
        [df_save, new_row],
        ignore_index=True
    )

    df_save.to_csv(
        "data/internships.csv",
        index=False
    )

    st.success(
        "✅ Internship Added Successfully!"
    )

    st.rerun()


# ==================================
# FILTER DATA
# ==================================

filtered_df = df.copy()

if source_filter != "All":
    filtered_df = filtered_df[
        filtered_df["Source"] == source_filter
    ]

if search:

    filtered_df = filtered_df[
        filtered_df["Lab"].str.contains(
            search,
            case=False,
            na=False
        )
        |
        filtered_df["Location"].str.contains(
            search,
            case=False,
            na=False
        )
        |
        filtered_df["Eligibility"].str.contains(
            search,
            case=False,
            na=False
        )
    ]
if status_filter != "All":
    filtered_df = filtered_df[
        filtered_df["Status"] == status_filter
    ]

# ==================================
# AVAILABLE INTERNSHIPS
# ==================================

st.subheader(
    "Available Internships"
)

display_columns = [
    "Lab",
    "Location",
    "Eligibility",
    "Deadline",
    "Source",
    "Status"
]

display_df = filtered_df[
    display_columns
].copy()

display_df["Status"] = (
    display_df["Status"]
    .replace({
        "Open": "🟢 Open",
        "Closing Soon": "🟠 Closing Soon"
    })
)

st.dataframe(
    display_df,
    width="stretch"
)

# ==================================
# CLOSING SOON
# ==================================

urgent = df[
    (df["Days Left"] <= 15)
    &
    (df["Days Left"] >= 0)
]

if not urgent.empty:

    st.warning(
        "⚠ Internships Closing Soon!"
    )
    display_columns = [
    "Lab",
    "Location",
    "Deadline",
    "Source",
    "Eligibility",
    "Status"
]

    st.dataframe(
            df[display_columns]
        )
    st.dataframe(
        urgent[
            [
                "Lab",
                "Deadline",
                "Days Left"
            ]
        ],
        use_container_width=True
    )

# ==================================
# DASHBOARD SUMMARY
# ==================================

st.subheader(
    "Dashboard Summary"
)

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Total Internships",
        len(df)
    )

with col2:
    st.metric(
        "Open Positions",
        len(
            df[df["Status"] == "Open"]
        )
    )

with col3:
    st.metric(
        "Closing Soon",
        len(
            df[df["Status"] == "Closing Soon"]
        )
    )
# ==================================
# CHART
# ==================================

st.subheader(
    "Internships by Location"
)

location_counts = (
    df["Location"]
    .value_counts()
)

st.bar_chart(location_counts)

# ==================================
# DOWNLOAD CSV
# ==================================

st.subheader(
    "Download Data"
)
from utils.pdf_report import generate_pdf

if st.button(
    "📄 Generate PDF Report",
    key="pdf_button"
):

    pdf_file = generate_pdf()

    with open(
        pdf_file,
        "rb"
    ) as file:

        st.download_button(
            label="⬇ Download PDF",
            data=file,
            file_name=pdf_file,
            mime="application/pdf"
        )
csv = df.to_csv(
    index=False
)

st.download_button(
    label="⬇ Download Internship Data",
    data=csv,
    file_name="internships.csv",
    mime="text/csv"
)

# ==================================
# DELETE INTERNSHIP
# ==================================

st.subheader(
    "Delete Internship"
)

lab_to_delete = st.selectbox(
    "Select Lab to Delete",
    df["Lab"].unique()
)

if st.button(
    "Delete Selected Internship"
):

    df_updated = df[
        df["Lab"] != lab_to_delete
    ]

    df_updated.to_csv(
        "data/internships.csv",
        index=False
    )

    st.success(
        f"✅ {lab_to_delete} deleted successfully!"
    )

    st.rerun()
st.markdown("---")

st.caption(
    "Built using Python, Streamlit, BeautifulSoup, PDF Parsing and Government Open Data Sources."
)