#https://github.com/Soulter/hugging-chat-api
import streamlit as st
from hugchat import hugchat
from hugchat.login import Login
import tiktoken
encoding = tiktoken.encoding_for_model("gpt-3.5-turbo")

# Log in to huggingface and grant authorization to huggingchat
account_name = st.text_input("Enter your HF account name:")
account_pwd = st.text_input("Enter your HF account password:")

sign = Login(account_name, account_pwd)
cookies = sign.login()

# Save cookies to usercookies/<email>.json
sign.saveCookiesToDir()

chat_resp = ""

# Create a ChatBot
chatbot = hugchat.ChatBot(cookies=cookies.get_dict())

# Create a new conversation
id = chatbot.new_conversation()
chatbot.change_conversation(id)

while True:
    user_input = st.text_input("What would you like me to answer? (Enter 'exit' to quit): ")
    if user_input.lower() == 'exit':
        break
    
    chat_resp = chatbot.chat(user_input)
    st.write("\n"+"Your input: "+user_input)
    st.write("\n"+"AI Response:"+"\n"+chat_resp)
    print("\n"+"Your input: "+user_input)
    print("\n"+"AI Response:"+"\n"+chat_resp)

    tokens = encoding.encode(chat_resp)
    token_count=len(tokens)
    st.write("\n"+"Token counts: "+str(token_count)+"\n")
    print("\n"+"Token counts: "+str(token_count)+"\n")

# Get conversation list
conversation_list = chatbot.get_conversation_list()
st.wreite("App Exited. Conversation list IDs: " + str(conversation_list))
print("App Exited. Conversation list IDs: " + str(conversation_list))
