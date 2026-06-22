import streamlit as st

st.title("🎤 Interview Preparation")

role = st.selectbox(
    "Select Role",
    [
        "AI Engineer",
        "Data Scientist",
        "Software Developer"
    ]
)

questions = {
    "AI Engineer": [
        "What is Machine Learning?",
        "What is Overfitting?",
        "Difference between CNN and RNN?",
        "Explain Gradient Descent."
    ],
    "Data Scientist": [
        "What is EDA?",
        "What is a Confusion Matrix?",
        "Difference between Mean and Median?"
    ],
    "Software Developer": [
        "What is OOP?",
        "Difference between Stack and Queue?",
        "Explain Linked List."
    ]
}

if st.button("Generate Questions"):

    for q in questions[role]:
        st.write(f"✅ {q}")