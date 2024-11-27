from langchain.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
from langchain.tools.retriever import create_retriever_tool

from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnableConfig, chain

load_dotenv()

llm = ChatGroq(model="llama3-8b-8192")

retrievers_cobranca = {}
retrievers_gestao = {}
retrievers_assinatura = {}
retrievers_vendas = {}
retrievers_perguntas_frequentes = {}

names_vendas = [
    "Vendas"
]

names_assinatura = [
    "Assinatura"
]

names_gestao = [
    "Gestao", 
]

names_cobranca = [
    "Cobranca"
]

def load_vectorstore(retrievers, name):
    vectorstore = Chroma(
        collection_name=name,
        persist_directory="langgraph/data",
        embedding_function= HuggingFaceEmbeddings()
    )
    retriever_tool = create_retriever_tool(vectorstore.as_retriever(search_kwargs={"k": 3}), f"retrieve_{name}_posts", f"Ferramenta para buscar informações sobre {name}")
    retrievers.update({name: retriever_tool})
    return retrievers

question = "crediario"

model_generated_tool_call = {
    "args" : {"query" : question},
    "id" : "1",
    "name" : "tavily",
    "type" : "tool_call"
}

prompt = ChatPromptTemplate(
    [
        ("system", f"Você é um assistente do meu crediário do módulo de gestão."),
        ("human", "{user_input}"),
        ("placeholder", "{messages}"),
    ]
)

# tavily_tool = tavily_search_tool_gestao()
# response = tavily_tool.invoke(model_generated_tool_call)

# retrievers_cobranca = load_vectorstore(retrievers_cobranca, name=names_cobranca[0])
# retrievers_gestao = load_vectorstore(retrievers_gestao, name=names_gestao[0])
# retrievers_vendas = load_vectorstore(retrievers_vendas, name=names_vendas[0])
# retrievers_assinatura = load_vectorstore(retrievers_assinatura, name=names_assinatura[0])