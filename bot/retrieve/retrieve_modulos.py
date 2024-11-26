from bot.data_vector.load_vector_store import retrievers_cobranca, retrievers_gestao, retrievers_assinatura, retrievers_vendas
from router.router import RAG_router
from router.router import question_router

from llm.llm import llm

from langchain_core.output_parsers import StrOutputParser 

from langchain_core.prompts import PromptTemplate

promptTemplate = """
Você é um assistente do Meu Crediário do qual vai realizar o suporte de atendimento ao cliente sobre alguns módulos do sistema da empresa.

Para responder as dúvidas você tem um contexto personalizado:

{context}

Segue a pergunta do usuário:
"{question}"
"""

promptTemplate = PromptTemplate.from_template(promptTemplate)

rag_chain = promptTemplate | llm | StrOutputParser()


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
    
    response = {"documents": documents, "question": question, "generation": generation}
    return response

def generate_random(state):
    print("Gerando resposta")
    print("-"*8)
    question = state["question"]

    generation = rag_chain.invoke({"context": '', "question": question})
    response = {"question": question, "generation": generation}
    return response

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