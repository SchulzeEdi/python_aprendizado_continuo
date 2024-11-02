from dotenv import load_dotenv
load_dotenv()

# from langchain_community.document_loaders import WebBaseLoader
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from langchain.schema import Document
from langchain.text_splitter import RecursiveCharacterTextSplitter


from langchain_community.vectorstores import Chroma

from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain.tools.retriever import create_retriever_tool
from langchain.embeddings import HuggingFaceEmbeddings

from langchain_core.tools import tool
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from typing import Literal

from langchain_core.prompts import ChatPromptTemplate
from pydantic import BaseModel, Field
from langchain_groq import ChatGroq
from typing import List

from IPython.display import Image, display
from typing_extensions import TypedDict

from langgraph.graph import END, StateGraph, START

import pprint

#URL DE COBRANCA
urls_cobranca = [
    "https://meucrediario.my.site.com/CentralAjudaMeuCrediario/s/article/Como-visualizar-clientes-que-est%C3%A3o-na-fila-para-cobran%C3%A7a",
    # "https://meucrediario.my.site.com/CentralAjudaMeuCrediario/s/article/Como-visualizar-quais-clientes-est%C3%A3o-com-a-cobran%C3%A7a-pausada",
    # "https://meucrediario.my.site.com/CentralAjudaMeuCrediario/s/article/Posso-alterar-o-texto-do-SMS-de-cobran%C3%A7a",
    # "https://meucrediario.my.site.com/CentralAjudaMeuCrediario/s/article/Solucionando-a-n%C3%A3o-reabilita%C3%A7%C3%A3o-autom%C3%A1tica-de-contratos-negativados-ap%C3%B3s-migra%C3%A7%C3%A3o-de-M%C3%B3dulo-ou-ERP",
    # "https://meucrediario.my.site.com/CentralAjudaMeuCrediario/s/article/Como-negativar-clientes-inadimplentes",
    # "https://meucrediario.my.site.com/CentralAjudaMeuCrediario/s/article/Ap%C3%B3s-reabilitar-o-cliente-quanto-tempo-leva-para-o-registro-ser-exclu%C3%ADdo",
    # "https://meucrediario.my.site.com/CentralAjudaMeuCrediario/s/article/Como-acontece-a-reabilita%C3%A7%C3%A3o-de-um-cliente",
    # "https://meucrediario.my.site.com/CentralAjudaMeuCrediario/s/article/Como-visualizar-clientes-reabilitados",
    # "https://meucrediario.my.site.com/CentralAjudaMeuCrediario/s/article/Como-saber-se-houve-algum-erro-de-reabilita%C3%A7%C3%A3o",
    # "https://meucrediario.my.site.com/CentralAjudaMeuCrediario/s/article/Como-visualizar-quantos-clientes-pagaram-ap%C3%B3s-a-cobran%C3%A7a",
    # "https://meucrediario.my.site.com/CentralAjudaMeuCrediario/s/article/Como-visualizar-contato-registrado",
    # "https://meucrediario.my.site.com/CentralAjudaMeuCrediario/s/article/Para-que-serve-e-como-funciona-o-relat%C3%B3rio-Situa%C3%A7%C3%A3o-do-capital",
    # "https://meucrediario.my.site.com/CentralAjudaMeuCrediario/s/article/Como-visualizar-quais-clientes-pagaram-ap%C3%B3s-a-cobran%C3%A7a",
    # "https://meucrediario.my.site.com/CentralAjudaMeuCrediario/s/article/Como-verificar-qual-r%C3%A9gua-est%C3%A1-aplicada-para-determinado-cliente",
    # "https://meucrediario.my.site.com/CentralAjudaMeuCrediario/s/article/Como-marcar-um-cliente-como-reabilitado",
    # "https://meucrediario.my.site.com/CentralAjudaMeuCrediario/s/article/Cliente-pagou-e-permanece-negativado",
    # "https://meucrediario.my.site.com/CentralAjudaMeuCrediario/s/article/Como-reabilitar-um-cliente-manualmente",
    # "https://meucrediario.my.site.com/CentralAjudaMeuCrediario/s/article/O-cliente-negativado-n%C3%A3o-quitou-todas-as-parcelas-em-atraso-devo-reabilit%C3%A1-lo",
    # "https://meucrediario.my.site.com/CentralAjudaMeuCrediario/s/article/Como-filtrar-quantas-negativa%C3%A7%C3%B5es-foram-realizadas-em-determinado-per%C3%ADodo",
]
names_cobranca = [
    "Cobranca"
]

#URL DE GESTAO
urls_gestao = [
    "https://meucrediario.my.site.com/CentralAjudaMeuCrediario/s/article/Como-ver-o-detalhamento-de-uma-an%C3%A1lise-de-cr%C3%A9dito",
    # "https://meucrediario.my.site.com/CentralAjudaMeuCrediario/s/article/O-que-fazer-se-um-contrato-estiver-com-as-dados-diferentes-do-meu-sistema-frente-de-caixa",
    # "https://meucrediario.my.site.com/CentralAjudaMeuCrediario/s/article/Como-fazer-a-confer%C3%AAncia-dos-lotes-enviados-pelo-ERP-frente-de-caixa",
    # "https://meucrediario.my.site.com/CentralAjudaMeuCrediario/s/article/A-import%C3%A2ncia-do-seu-ERP-frente-de-caixa-e-o-envio-dos-lotes-movimenta%C3%A7%C3%B5es-da-sua-loja",
    # "https://meucrediario.my.site.com/CentralAjudaMeuCrediario/s/article/Inadimpl%C3%AAncia-por-Safra",
    # "https://meucrediario.my.site.com/CentralAjudaMeuCrediario/s/article/O-que-fazer-se-identificar-uma-inconsist%C3%AAncia-nos-lotes-recebidos-do-ERP",
    # "https://meucrediario.my.site.com/CentralAjudaMeuCrediario/s/article/O-que-%C3%A9-Score-Base-e-Score-Proposta",
    # "https://meucrediario.my.site.com/CentralAjudaMeuCrediario/s/article/Resumo-da-loja-Quantidade-de-clientes-novos-por-m%C3%AAs",
    # "https://meucrediario.my.site.com/CentralAjudaMeuCrediario/s/article/Relat%C3%B3rios-de-Gest%C3%A3o"
]
names_gestao = [
    "Gestao", 
]

#URL DE ASSINATURA
urls_assinatura = [
    "https://meucrediario.my.site.com/CentralAjudaMeuCrediario/s/article/Posso-enviar-o-comprovante-de-pagamento-para-ter-a-libera%C3%A7%C3%A3o-do-meu-saldo",
    # "https://meucrediario.my.site.com/CentralAjudaMeuCrediario/s/article/D%C3%A9bito-de-mensalidade-do-Meu-Credi%C3%A1rio",
    # "https://meucrediario.my.site.com/CentralAjudaMeuCrediario/s/article/Como-funciona-a-emiss%C3%A3o-da-nota-fiscal",
    # "https://meucrediario.my.site.com/CentralAjudaMeuCrediario/s/article/Como-assinar-o-Meu-Credi%C3%A1rio",
    # "https://meucrediario.my.site.com/CentralAjudaMeuCrediario/s/article/Quando-minha-nota-fiscal-de-servi%C3%A7o-%C3%A9-emitida",
    # "https://meucrediario.my.site.com/CentralAjudaMeuCrediario/s/article/Como-bloquear-um-usu%C3%A1rio-no-sistema",
    # "https://meucrediario.my.site.com/CentralAjudaMeuCrediario/s/article/Por-que-n%C3%A3o-estou-vendo-todos-os-bot%C3%B5es",
    # "https://meucrediario.my.site.com/CentralAjudaMeuCrediario/s/article/Utiliza%C3%A7%C3%A3o-das-an%C3%A1lises-e-negativa%C3%A7%C3%B5es",
    # "https://meucrediario.my.site.com/CentralAjudaMeuCrediario/s/article/O-que-acontece-se-a-minha-mensalidade-n%C3%A3o-for-paga",
    # "https://meucrediario.my.site.com/CentralAjudaMeuCrediario/s/article/Como-verificar-o-extrato-de-consumos-dentro-da-plataforma"
]
names_assinatura = [
    "Assinatura"
]

#URL DE VENDAS
urls_vendas = [
    "https://meucrediario.my.site.com/CentralAjudaMeuCrediario/s/article/Por-que-solicitar-os-documentos-originais-para-abertura-do-credi%C3%A1rio",
    # "https://meucrediario.my.site.com/CentralAjudaMeuCrediario/s/article/Como-cadastrar-um-cliente",
    # "https://meucrediario.my.site.com/CentralAjudaMeuCrediario/s/article/Como-desbloquear-um-cliente",
    # "https://meucrediario.my.site.com/CentralAjudaMeuCrediario/s/article/Existe-um-percentual-limite-para-trabalhar-a-cobran%C3%A7a-de-juros",
    # "https://meucrediario.my.site.com/CentralAjudaMeuCrediario/s/article/Como-configurar-os-juros-por-parcela-em-minha-loja",
    # "https://meucrediario.my.site.com/CentralAjudaMeuCrediario/s/article/Como-fazer-um-acordo-no-sistema",
    # "https://meucrediario.my.site.com/CentralAjudaMeuCrediario/s/article/Como-cancelar-um-acordo",
    # "https://meucrediario.my.site.com/CentralAjudaMeuCrediario/s/article/Como-alterar-a-data-de-recebimento",
    # "https://meucrediario.my.site.com/CentralAjudaMeuCrediario/s/article/Como-fazer-um-recebimento-com-Desconto-Manual",
    # "https://meucrediario.my.site.com/CentralAjudaMeuCrediario/s/article/Como-fazer-um-recebimento-com-Desconto-Autom%C3%A1tico"
]
names_vendas = [
    "Vendas"
]

#URL DE PERGUNTAS FREQUENTES
urls_perguntas_frequentes = [
    "https://meucrediario.my.site.com/CentralAjudaMeuCrediario/s/article/O-que-acontece-com-meus-clientes-negativados-se-eu-cancelar-a-assinatura",
    # "https://meucrediario.my.site.com/CentralAjudaMeuCrediario/s/article/Posso-negativar-os-clientes-que-j%C3%A1-estavam-em-atraso-quando-implantei-o-sistema",
    # "https://meucrediario.my.site.com/CentralAjudaMeuCrediario/s/article/A-negativa%C3%A7%C3%A3o-%C3%A9-feita-em-que-%C3%B3rg%C3%A3o",
    # "https://meucrediario.my.site.com/CentralAjudaMeuCrediario/s/article/Posso-negativar-o-cliente-pelo-Meu-Credi%C3%A1rio",
    # "https://meucrediario.my.site.com/CentralAjudaMeuCrediario/s/article/Como-criar-um-atalho-do-Meu-Credi%C3%A1rio-na-%C3%A1rea-de-trabalho",
    # "https://meucrediario.my.site.com/CentralAjudaMeuCrediario/s/article/Introdu%C3%A7%C3%A3o-ao-Meu-Credi%C3%A1rio",
    # "https://meucrediario.my.site.com/CentralAjudaMeuCrediario/s/article/Como-fa%C3%A7o-para-solicitar-um-atendimento-de-suporte-do-Meu-Credi%C3%A1rio",
    # "https://meucrediario.my.site.com/CentralAjudaMeuCrediario/s/article/Qual-loja-consultou-meu-CPF",
    # "https://meucrediario.my.site.com/CentralAjudaMeuCrediario/s/article/Como-cancelar-a-plataforma",
    # "https://meucrediario.my.site.com/CentralAjudaMeuCrediario/s/article/Como-fazer-um-print-captura-de-tela-em-meu-computador"

]
names_perguntas_frequentes = [
    "Perguntas frequentes", "Perguntas frequentes", "Perguntas frequentes", "Perguntas frequentes", "Perguntas frequentes", "Perguntas frequentes", "Perguntas frequentes", "Perguntas frequentes", "Perguntas frequentes", "Perguntas frequentes"
]


driver = webdriver.Chrome()

docs_cobranca = []
for url in urls_cobranca:
    driver.get(url)
    time.sleep(5)
    content = driver.find_element(By.TAG_NAME, "body").text
    docs_cobranca.append(Document(page_content=content))

docs_gestao = []
for url in urls_gestao:
    driver.get(url)
    time.sleep(5)
    content = driver.find_element(By.TAG_NAME, "body").text
    docs_gestao.append(Document(page_content=content))

docs_assinatura = []
for url in urls_assinatura:
    driver.get(url)
    time.sleep(5)
    content = driver.find_element(By.TAG_NAME, "body").text
    docs_cobranca.append(Document(page_content=content))

docs_vendas = []
for url in urls_vendas:
    driver.get(url)
    time.sleep(5)
    content = driver.find_element(By.TAG_NAME, "body").text
    docs_vendas.append(Document(page_content=content))

driver.quit()

text_splitter = RecursiveCharacterTextSplitter.from_tiktoken_encoder(chunk_size=500, chunk_overlap=200)

docs_list_cobranca = [text_splitter.split_documents([doc]) for doc in docs_cobranca]
docs_list_gestao = [text_splitter.split_documents([doc]) for doc in docs_gestao]
docs_list_assinatura = [text_splitter.split_documents([doc]) for doc in docs_assinatura]
docs_list_vendas = [text_splitter.split_documents([doc]) for doc in docs_vendas]

docs_list_cobranca = [chunk for sublist in docs_list_cobranca for chunk in sublist]
docs_list_gestao = [chunk for sublist in docs_list_gestao for chunk in sublist]
docs_list_assinatura = [chunk for sublist in docs_list_assinatura for chunk in sublist]
docs_list_vendas = [chunk for sublist in docs_list_vendas for chunk in sublist]


retrievers_cobranca = {}
retrievers_gestao = {}
retrievers_assinatura = {}
retrievers_vendas = {}
retrievers_perguntas_frequentes = {}

# def load_vectorstore(retrievers, name):
#     vectorstore = Chroma(
#         collection_name=name,
#         persist_directory="./data",
#     ).as_retriever()
#     print(vectorstore)
#     retrievers.update({name: vectorstore})
#     return retrievers

def create_retrievers_system(retrievers, names, docs_list):
    for doc, name in zip(docs_list, names):
        split = text_splitter.split_documents([doc])
        vectorstore = Chroma.from_documents(
            documents=split,
            collection_name=name,
            embedding= HuggingFaceEmbeddings(),
            persist_directory="./data"
        )
        retriever_tool = create_retriever_tool(vectorstore.as_retriever(search_kwargs={"k": 3}), f"retrieve_{name}_posts", f"Ferramenta para buscar informações sobre {name}")
        retrievers.update({name: retriever_tool})
    return retrievers

retrievers_cobranca = create_retrievers_system(retrievers_cobranca, names_cobranca, docs_list_cobranca)
retrievers_gestao = create_retrievers_system(retrievers_gestao, names_gestao, docs_list_gestao)
retrievers_vendas = create_retrievers_system(retrievers_vendas, names_vendas, docs_list_vendas)
retrievers_assinatura = create_retrievers_system(retrievers_assinatura, names_assinatura, docs_list_assinatura)

# retrievers_cobranca = load_vectorstore(retrievers_cobranca, name=names_cobranca[0])
# retrievers_gestao = load_vectorstore(retrievers_gestao, name=names_gestao[0])
# retrievers_vendas = load_vectorstore(retrievers_vendas, name=names_vendas[0])
# retrievers_assinatura = load_vectorstore(retrievers_assinatura, name=names_assinatura[0])

# retrievers_perguntas_frequentes = create_retrievers_system(retrievers_perguntas_frequentes, names_perguntas_frequentes)


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
    documents: List[str]

class RouteQuery(BaseModel):
    path: Literal["Cobranca", "Gestao", "Assinatura", "Vendas"] = Field(
        ...,
        description="Você deve decidir qual módulo o usuário está com dúvida, sobre gestão, cobrança, assinatura, vendas."
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
    
class RouteRAG(BaseModel):
    path: Literal["Cobranca", "Gestao", "Assinatura", "Vendas"] = Field(
        ...,
        description="Você deve decidir qual módulo usar para responder a pergunta do usuário."
    )


structured_llm_router = llm.with_structured_output(RouteRAG)

system = """Você precisa decidir qual módulo usar para responder a pergunta do usuário:

Cobranca, Gestao, Assinatura, Vendas
"""

RAG_prompt = ChatPromptTemplate.from_messages(
    [
        ("system", system),
        ("human", "{question}"),
    ]
)

RAG_router = RAG_prompt | structured_llm_router

def generate(state):
    print("Gerando resposta")
    print("-"*8)
    question = state["question"]
    documents = state["documents"]
    print(documents)
    generation = rag_chain.invoke({"context": documents, "question": question})
    return {"documents": documents, "question": question, "generation": generation}

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

#Retrieve do módulo de perguntas frequentes
# def retrieve_perguntas_frequentes(state):
#     question = state['Perguntas frequentes']
#     collection = RAG_router.invoke({"question":question}).path
#     print(f"Realizando a busca vetorial no banco de {collection}")

#     documents = retrievers_perguntas_frequentes.get(collection).invoke(question)
#     return {"documents": documents, "question": question}

workflow = StateGraph(GraphState)
# workflow.add_node("retrieve", retrieve)
workflow.add_node("generate", generate)
workflow.add_node("retrieve_cobranca", retrieve_cobranca)
workflow.add_node("retrieve_gestao", retrieve_gestao)
workflow.add_node("retrieve_assinatura", retrieve_assinatura)
workflow.add_node("retrieve_vendas", retrieve_vendas)
# workflow.add_node("retrieve_perguntas_frequentes", retrieve_perguntas_frequentes)

workflow.add_conditional_edges(
    START,
    route_question,
    {
        "Cobranca": "retrieve_cobranca",
        "Gestao": "retrieve_gestao",
        "Assinatura": "retrieve_assinatura",
        "Vendas": "retrieve_vendas",
    }
)
workflow.add_edge("retrieve_cobranca", "generate")
workflow.add_edge("retrieve_gestao", "generate")
workflow.add_edge("retrieve_assinatura", "generate")
workflow.add_edge("retrieve_vendas", "generate")

app = workflow.compile()

# display(Image(app.get_graph().draw_mermaid_png()))

image_data = app.get_graph().draw_mermaid_png()

with open("grafo_ia.png", "wb") as f:
    f.write(image_data)

def send_question(question):
    result = app.invoke(input = {
        "question": question
    })
    print(result.get("generation"))
    
# send_question("Bom dia, como visualizo clientes que estão na fila de cobrança? No módulo de cobrança")
# send_question("Bom dia, como que eu envio comprovante de pagamento para ter a liberação do meu saldo? No módulo de assinatura")
send_question("Bom dia, como que eu olho o detalhamento de uma análise de crédito? No módulo de gestão")
# send_question("Bom dia, como que eu cadastro um cliente? No Módulo de vendas?")