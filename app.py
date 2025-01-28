import streamlit as st
import requests
import hashlib
import sqlite3

st.markdown("""
    <style>
        # MyApp {
            background-color: blue;
            color: white;
            padding: 20px;
            font-family: Arial, sans-serif;
        }
        .chat-input {
            background-color: #dcf8c6;
            border: 2px solid #4CAF50;
            border-radius: 5px;
            padding: 10px;
            font-size: 16px;
        }
        .stButton button {
            background-color: #4CAF50;
            color: #fff;
            border: none;
            border-radius: 5px;
            padding: 10px 20px;
            font-size: 16px;
            cursor: pointer;
        }
        .stButton button:hover {
            background-color: #3e8e41;
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

conn = sqlite3.connect('chatbot.db')
c = conn.cursor()
c.execute('CREATE TABLE IF NOT EXISTS users (username text PRIMARY KEY, password text)')
conn.commit()

def get_user(username):
    c.execute('SELECT * FROM users WHERE username = ?', (username,))
    return c.fetchone()

def register(username, password):
    hash_pwd = hashlib.sha256(password.encode()).hexdigest()
    c.execute('INSERT INTO users VALUES (?, ?)', (username, hash_pwd))
    conn.commit()

def login(username, password):
    hash_pwd = hashlib.sha256(password.encode()).hexdigest()
    c.execute('SELECT * FROM users WHERE username = ? AND password = ?', (username, hash_pwd))
    user = c.fetchone()
    if user:
        return username
    return None


st.title("YukiBot - The Chatbot for Personalized Learning") 

def send_message(message):
    response = requests.post(
        'http://localhost:5005/webhooks/rest/webhook',
        json={"sender": "user", "message": message}
    )
    return response.json()

def main():
    if 'history' not in st.session_state:
        st.session_state.history = []

    if 'logged_in_user' not in st.session_state:
        st.session_state.logged_in_user = None

    with st.sidebar:
        st.header("User Menu")
        if st.button("New Chat"):
            st.session_state.history = [] 

    # Registration/Login section
    if not st.session_state.logged_in_user:
        with st.expander("Register/Login"):
            username = st.text_input("Username")
            password = st.text_input("Password", type="password")

            if st.button("Register"):
                if username and password:
                    try:
                        register(username, password)
                        st.success("Registration successful!")
                    except sqlite3.IntegrityError:
                        st.error("Username already exists.")

            if st.button("Login"):
                if username and password:
                    session_token = login(username, password)
                    if session_token:
                        st.session_state.logged_in_user = session_token
                        st.success("Login successful!")
                    else:
                        st.error("Invalid login credentials.")

    # Chat interface - log-in users
    if st.session_state.logged_in_user:
        st.write(f"Welcome to YukiBot, {st.session_state.logged_in_user}!")
        user_data = get_user(st.session_state.logged_in_user)

        message = st.chat_input("You: ", key="input")

        chat_con = st.container()
        chat_history = st.sidebar

        with chat_con:
            if message:
                responses = send_message(message)
                all_bot_responses = ""
                for response in responses:
                    if 'text' in response:
                        all_bot_responses += response['text'] + "\n"
                    st.session_state.history.append((message, all_bot_responses))
                    
                    
            user_msg, bot_msg = st.session_state.history[-1] if st.session_state.history else ("", "")
            st.markdown(f"<div class='message user-message'>You: {user_msg}</div>", unsafe_allow_html=True)
            st.markdown(f"<div class='message bot-message'>Answer: {bot_msg}</div>", unsafe_allow_html=True)

        with chat_history:
            if len(st.session_state.history) > 1:
                st.header("Old Chats")
                for user_msg, bot_msg in st.session_state.history[len(st.session_state.history) - 2:len(st.session_state.history) - 3:-1]:
                    st.markdown(f"<div class='message user-message'>You: {user_msg}</div>", unsafe_allow_html=True)
                    st.markdown(f"<div class='message bot-message'>Answer: {bot_msg}</div>", unsafe_allow_html=True)

if __name__ == "__main__":
    main()