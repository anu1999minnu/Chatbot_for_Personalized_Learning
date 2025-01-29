# Chatbot_for_Personalized_Learning

## Description 
The Chatbot_for_Personalized_Learning is an educational chatbot that helps students to get answers to questions that they ask to the bot. It uses Rasa module for training the bot and uses Streamlit for the front-end part. For the user details storage SQLite3 is used. It just takes the username and password from the user. The chatbot named YukiBot is a platform for understanding about the topic in concise format, it also provides video links based on the topic. For videos the Youtube API is used. The Chatbot can provide answers to basic mathematical calculation based questions. 

For running the chatbot use the following commands:
  1. rasa run  ### it keeps the server running
  2. rasa run actions ### for running the actions.py file
  3. streamlit run app.py   ### runs the app on the default browser
