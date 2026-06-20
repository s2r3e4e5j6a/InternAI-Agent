import streamlit as st

st.set_page_config(
    page_title="InternAI Agent",
    page_icon="🚀",
    layout="wide"
)

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

# Debug (temporary)
st.write(st.session_state)

# Logout Button
if st.session_state.get("logged_in"):

    if st.sidebar.button("🚪 Logout"):

        st.session_state.clear()
        st.rerun()

st.title("🚀 InternAI Agent")

if st.session_state.logged_in:

    st.success(
        f"Logged in as {st.session_state.username}"
    )

else:

    st.warning(
        "Please Login First"
    )

st.markdown("""
### Modules

- Dashboard
- Profile
- Login
- Register
- Resume Upload
- Recommendations
- Career Coach
""")