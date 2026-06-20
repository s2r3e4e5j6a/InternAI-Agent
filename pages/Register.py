import streamlit as st
from utils.auth import register_user

st.title("📝 Register")

username = st.text_input("Username")

email = st.text_input("Email")

password = st.text_input(
    "Password",
    type="password"
)

if st.button("Register"):

    success = register_user(
        username,
        email,
        password
    )

    if success:
        st.success("Registration Successful")
    else:
        st.error("Username already exists")