import streamlit as st
from langchain_groq import ChatGroq
from langchain_community.tools.tavily_search import TavilySearchResults
from langchain_core.messages import HumanMessage
from langgraph.checkpoint.memory import MemorySaver
from langgraph.prebuilt import create_react_agent
from dotenv import load_dotenv
import os

load_dotenv()

st.set_page_config(page_title="ChatBot do Schulze", page_icon="🤖")
st.title("Bem vindos ao ChatBot do Schulze!")

def generate_response(input_text):
    # Instancia MemorySaver sem configuração extra
    memory = MemorySaver()
    
    llm = ChatGroq(
        model="mixtral-8x7b-32768",
        temperature=0.0,
        max_retries=2,
    )  
    search = TavilySearchResults(
        max_results=2
    )
    tools = [search]

    agent_executor = create_react_agent(llm, tools, checkpointer=memory)
    
    generator = agent_executor.stream(
        HumanMessage(content=input_text), 
        config={"configurable": {"messages": True, "thread_id": "abc123"}}
    )
    
    last_message = None
    for message in generator:
        last_message = message
    
    if last_message is not None:
        st.info(last_message.content)
    else:
        st.info("Nenhuma mensagem foi recebida.")

groq_api_key = os.getenv("GROQ_API_KEY")
if not groq_api_key or not groq_api_key.startswith("gsk_"):
    st.warning("Por favor, insira uma chave válida de GROQ no arquivo .env", icon="⚠")
else:
    with st.form("my_form"):
        text = st.text_area("Coloque seu texto abaixo:", "Sobre o que vamos conversar hoje?")
        submitted = st.form_submit_button("Submit")
        if submitted:
            generate_response(text)
