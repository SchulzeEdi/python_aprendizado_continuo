from dotenv import load_dotenv
load_dotenv()

from langchain.tools.retriever import create_retriever_tool
from langchain.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma

from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from typing import Literal

from langchain_core.prompts import ChatPromptTemplate
from pydantic import BaseModel, Field
from langchain_groq import ChatGroq
from typing import List

from typing_extensions import TypedDict

from langgraph.graph import END, StateGraph, START


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
        persist_directory="./data",
        embedding_function= HuggingFaceEmbeddings()
    )
    retriever_tool = create_retriever_tool(vectorstore.as_retriever(search_kwargs={"k": 3}), f"retrieve_{name}_posts", f"Ferramenta para buscar informações sobre {name}")
    retrievers.update({name: retriever_tool})
    return retrievers

retrievers_cobranca = load_vectorstore(retrievers_cobranca, name=names_cobranca[0])
retrievers_gestao = load_vectorstore(retrievers_gestao, name=names_gestao[0])
retrievers_vendas = load_vectorstore(retrievers_vendas, name=names_vendas[0])
retrievers_assinatura = load_vectorstore(retrievers_assinatura, name=names_assinatura[0])

llm = ChatGroq(model_name="mixtral-8x7b-32768")

prompt = """
Você é um assistente do Meu Crediário do qual vai realizar o suporte de atendimento ao cliente sobre alguns módulos do sistema da empresa.

Para responder as dúvidas você tem um contexto personalizado:

{context}

Segue a pergunta do usuário:
"{question}"
"""
prompt = PromptTemplate.from_template(prompt)

rag_chain = prompt | llm | StrOutputParser()

class GraphState(TypedDict):
    question: str
    generation: str
    Cobranca: str
    Gestao: str
    Assinatura: str
    Vendas: str
    Aleatorios: str
    documents: List[str]

class RouteQuery(BaseModel):
    path: Literal["Cobranca", "Gestao", "Assinatura", "Vendas", "Aleatorios"] = Field(
        ...,
        description="Você deve decidir qual módulo o usuário está com dúvida, sobre gestão, cobrança, assinatura, vendas, ou se deve ir para perguntas aleatórias"
    )

class RouteRAG(BaseModel):
    path: Literal["Cobranca", "Gestao", "Assinatura", "Vendas", "Aleatorios"] = Field(
        ...,
        description="Você deve decidir qual módulo usar para responder a pergunta do usuário ou se deve ir para perguntas aleatorias."
    )

structured_llm_router = llm.with_structured_output(RouteQuery)

system = """Você é um especialista em encaminhar o usuário para o local correto.
Existem quatro possibilidades:
Cobranca quando o usuário está com dúvida sobre cobrança.
Gestão quando o usuário está com dúvida sobre gestão.
Assinatura quando o usuário está com dúvida sobre assinatura.
Vendas quando o usuário está com dúvida sobre vendas.
"""

route_prompt = ChatPromptTemplate.from_messages(
    [
        ("system", system),
        ("human", "{question}"),
    ]
)

question_router = route_prompt | structured_llm_router 

structured_llm_router = llm.with_structured_output(RouteRAG)

system = """Você precisa decidir qual módulo usar para responder a pergunta do usuário:

Cobranca, Gestao, Assinatura, Vendas, Aleatorios
"""

RAG_prompt = ChatPromptTemplate.from_messages(
    [
        ("system", system),
        ("human", "{question}"),
    ]
)

RAG_router = RAG_prompt | structured_llm_router

def route_question(state):
    print("-"*8)
    print("Começando roteamento")
    question = state["question"]
    source = question_router.invoke({"question": question})

    if source.path == "Cobranca":
        print("Cobranca")
        return "Cobranca"
    elif source.path == "Gestao":
        print("Gestão")
        return "Gestao"
    elif source.path == "Assinatura":
        print("Assinatura")
        return "Assinatura"
    elif source.path == "Vendas":
        print("Vendas")
        return "Vendas"
    elif source.path == "Aleatorios":
        print("Aleatorios")
        return "Aleatorios"
   
def generate(state):
    print("Gerando resposta")
    print("-"*8)
    question = state["question"]
    documents = state["documents"]
    generation = rag_chain.invoke({"context": documents, "question": question})
    return {"documents": documents, "question": question, "generation": generation}

def generate_question(state):
    print("Gerando resposta")
    print("-"*8)
    question = state["question"]
    generation = rag_chain.invoke({"question": question})
    return {"question": question, "generation": generation}

def retrieve_cobranca(state):
    question = state["question"]
    collection = RAG_router.invoke({"question":question}).path
    print(f"Realizando a busca vetorial no banco de {collection}")

    documents = retrievers_cobranca.get(collection).invoke(question)
    return {"documents" : documents, "question": question}

def retrieve_gestao(state):
    question = state["question"]
    collection = RAG_router.invoke({"question":question}).path
    print(f"Realizando a busca vetorial no banco de {collection}")

    documents = retrievers_gestao.get(collection).invoke(question)
    print(documents)
    return {"documents": documents, "question": question}

def retrieve_assinatura(state):
    question = state["question"]
    collection = RAG_router.invoke({"question":question}).path
    print(f"Realizando a busca vetorial no banco de {collection}")

    documents = retrievers_assinatura.get(collection).invoke(question)
    return {"documents": documents, "question": question}

def retrieve_vendas(state):
    question = state['question']
    collection = RAG_router.invoke({"question":question}).path
    print(f"Realizando a busca vetorial no banco de {collection}")

    documents = retrievers_vendas.get(collection).invoke(question)
    return {"documents": documents, "question": question}

workflow = StateGraph(GraphState)
workflow.add_node("generate", generate)
workflow.add_node("generate_question", generate_question)
workflow.add_node("retrieve_cobranca", retrieve_cobranca)
workflow.add_node("retrieve_gestao", retrieve_gestao)
workflow.add_node("retrieve_assinatura", retrieve_assinatura)
workflow.add_node("retrieve_vendas", retrieve_vendas)

workflow.add_conditional_edges(
    START,
    route_question,
    {
        "Cobranca": "retrieve_cobranca",
        "Gestao": "retrieve_gestao",
        "Assinatura": "retrieve_assinatura",
        "Vendas": "retrieve_vendas",
        "Aleatorios": "generate_question",
    }
)
workflow.add_edge("retrieve_cobranca", "generate")
workflow.add_edge("retrieve_gestao", "generate")
workflow.add_edge("retrieve_assinatura", "generate")
workflow.add_edge("retrieve_vendas", "generate")
workflow.add_edge("generate_question", "generate")

app = workflow.compile()

image_data = app.get_graph().draw_mermaid_png()

with open("grafo_ia.png", "wb") as f:
    f.write(image_data)

def send_question(question):
    result = app.invoke(input = {
        "question": question
    })
    print(result["generation"])
    return result["generation"]