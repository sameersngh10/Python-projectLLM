import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI

import getpass
import os
GOOGLE_API_KEY='AIzaSyAEyyFk4J-OIufaUNUAfysoLkO0D60T_0A'
if "GOOGLE_API_KEY" not in os.environ:
    os.environ["GOOGLE_API_KEY"] = getpass.getpass("Provide your Google API Key")

st.title('🦜🔗 Quickstart App')

# openai_api_key = st.sidebar.text_input('GOOGLE_API_KEY', type='password')

# def generate_response(input_text):
llm =  ChatGoogleGenerativeAI(model="gemini-pro")
    # st.info(llm(input_text))
    
result = llm.invoke("Write a ballad about LangChain")
print(result.content)

# with st.form('my_form'):
#     text = st.text_area('Enter text:', 'What are the three key pieces of advice for learning how to code?')
#     submitted = st.form_submit_button('Submit')
    # if not openai_api_key.startswith('sk-'):
    #     st.warning('Please enter your OpenAI API key!', icon='⚠')
    # if submitted and openai_api_key.startswith('sk-'):
    #     generate_response(text)