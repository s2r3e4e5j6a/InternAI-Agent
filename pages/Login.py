import streamlit as st
from utils.auth import login_user

st.title("🔐 Login")

username = st.text_input("Username")

password = st.text_input(
    "Password",
    type="password"
)

if st.button("Login"):

    user = login_user(
        username,
        password
    )

    if user:

        st.session_state["logged_in"] = True
        st.session_state["user_id"] = user[0]
        st.session_state["username"] = user[1]

        st.success("Login Successful")
        st.rerun()

    else:
        st.error("Invalid Credentials")