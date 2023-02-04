import streamlit as st
from revChatGPT.Official import Chatbot

api_key = st.secrets["OPENAI_API_KEY"]
chatbot = Chatbot(api_key)

def ask():
	prompt = st.text_input("请输入你要问老胡的问题")
	return prompt

st.header("ChatGPT老胡模拟器")
prompt = ask()
if prompt:
	chatbot.ask("你要像胡锡进那样回答我的问题。开头加上“老胡认为”，中间加上“但是，老胡还认为”，并且后半段的回答要用来反驳前半段的回答。")
	output = chatbot.ask(prompt)["choices"][0]["text"]
	st.write(output)
	chatbot.reset()
