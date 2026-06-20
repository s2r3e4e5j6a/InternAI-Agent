import streamlit as st

st.set_page_config(
    page_title="InternAI Agent",
    page_icon="🚀",
    layout="wide"
)

st.title("🚀 InternAI Agent")

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

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
""")