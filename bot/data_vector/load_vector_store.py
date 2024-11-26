from langchain.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
from langchain.tools.retriever import create_retriever_tool

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

retrievers_cobranca = load_vectorstore(retrievers_cobranca, name=names_cobranca[0])
retrievers_gestao = load_vectorstore(retrievers_gestao, name=names_gestao[0])
retrievers_vendas = load_vectorstore(retrievers_vendas, name=names_vendas[0])
retrievers_assinatura = load_vectorstore(retrievers_assinatura, name=names_assinatura[0])