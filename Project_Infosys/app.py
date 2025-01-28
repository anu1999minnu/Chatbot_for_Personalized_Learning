import streamlit as st
import requests

st.markdown("""
    <style>
    .reportview-container {
        background-color: blue;
    }
    .main .block-container {
        padding: 20px;
        background-color: blue;
        border-radius: 10px;
        box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
    }
    h1 {
        color: #4CAF50;
        text-align: center;
        font-family: 'Arial', sans-serif;
    }
    .chat-input {
        background-color: blue;
        border: 2px solid #4CAF50;
        border-radius: 5px;
        padding: 10px;
        font-size: 16px;
        font-family: 'Arial', sans-serif;
    }
    .stButton button {
        background-color: blue;
        color: #fff;
        border: none;
        border-radius: 5px;
        padding: 10px 20px;
        font-size: 16px;
        cursor: pointer;
    }
    .stButton button:hover {
        background-color: blue;
    }
    .message {
        padding: 10px;
        border-radius: 5px;
        margin: 10px 0;
    }
    .user-message {
        background-color: #dcf8c6;
        text-align: left;
    }
    .bot-message {
        background-color: #f1f0f0;
        text-align: left;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("The Chatbot for Personalized Learning")

def send_message(message):
    response = requests.post(
        'http://localhost:5005/webhooks/rest/webhook', 
        json={"sender": "user", "message": message}
    )
    return response.json()

def main():
    st.write("Welcome to the Yuki")
    if 'history' not in st.session_state:
        st.session_state.history = []

    if st.button("New Chat"):
        st.session_state.history = []

    message = st.chat_input("You: ", key="input")

    if message:
        responses = send_message(message)
        for response in responses:
            if 'text' in response:
                st.session_state.history.append((message, response['text']))

    for user_msg, bot_msg in st.session_state.history:
        st.markdown(f"<div class='message user-message'>You: {user_msg}</div>", unsafe_allow_html=True)
        st.markdown(f"<div class='message bot-message'>Answer: {bot_msg}</div>", unsafe_allow_html=True)
if __name__ == "__main__":
    main()
