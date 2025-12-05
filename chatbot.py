import streamlit as st


faq_data = {
    "what is codealpha": "CodeAlpha is an internship and training platform for students to enhance their skills.",
    "duration of internship": "The internship duration is usually 1 month.",
    "will i get certificate": "Yes! You will get a certificate after completing tasks successfully.",
    "what is python": "Python is a high-level, interpreted programming language used for AI, automation, web dev, etc.",
    "what is ai": "AI stands for Artificial Intelligence — machines performing tasks that require human intelligence!",
    "what is machine learning": "Machine Learning is a subset of AI where systems learn automatically from data.",
}


def get_response(user_query):
    query = user_query.lower()
    for key in faq_data.keys():
        if key in query:
            return faq_data[key]
    return "Sorry, I don't have an answer for that. Please ask something else! 🥲"


st.title("🤖 AI FAQ Chatbot")
st.write("Ask me something and I will try to answer!")

user_input = st.text_input("Enter your question:")

if st.button("Ask"):
    if user_input:
        response = get_response(user_input)
        st.success(f"Bot: {response}")
    else:
        st.warning("Please type a question!")
