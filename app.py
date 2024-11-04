import streamlit as st
from dotenv import load_dotenv
import os
from langgraph.agent_grafo import send_question

load_dotenv()

st.set_page_config(page_title="ChatBot do Meu Crediário", page_icon="🤖")
st.title("Bem vindos ao ChatBot do Meu Crediário!")

def generate_response(input_text):
    response = send_question(input_text)
    st.write(response)
    
groq_api_key = os.getenv("GROQ_API_KEY")
if not groq_api_key or not groq_api_key.startswith("gsk_"):
    st.warning("Por favor, insira uma chave válida de GROQ no arquivo .env", icon="⚠")
else:
    with st.form("my_form"):
        text = st.text_area("Coloque seu texto abaixo:", "Sobre o que vamos conversar hoje?")
        submitted = st.form_submit_button("Submit")
        if submitted:
            generate_response(text)