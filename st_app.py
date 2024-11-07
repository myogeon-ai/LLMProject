# pip install langchain
import streamlit as st
from langchain_community.llms import OpenAI


st.title('🍎🍐🍊 나의 AI Chat 🥝🍅🍆')

# openai_api_key = st.sidebar.text_input('OpenAI API Key')
openai_api_key = st.secrets["openai"]["api_key"]

