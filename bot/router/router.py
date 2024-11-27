from langchain_groq import ChatGroq
from pydantic import BaseModel, Field
from typing import Literal
from langchain_core.prompts import ChatPromptTemplate

from dotenv import load_dotenv
load_dotenv()

llm = ChatGroq(model_name="mixtral-8x7b-32768")

class RouteRAG(BaseModel):
    path: Literal["Cobranca", "Gestao", "Assinatura", "Vendas", "Aleatorios"] = Field(
        ...,
        description="""Você deve decidir qual módulo usar para responder a pergunta do usuário ou se deve ir para perguntas aleatorias. 
        Além de perguntar para o usuário caso você não tenha certeza de qual módulo é, qual módulo ele está com dúvida.
        """
    )

class RouteQuery(BaseModel):
    path: Literal["Cobranca", "Gestao", "Assinatura", "Vendas", "Aleatorios"] = Field(
        ...,
        description="Você deve decidir qual módulo o usuário está com dúvida, sobre gestão, cobrança, assinatura, vendas, ou se deve ir para perguntas aleatórias, ou perguntar qual módulo ele está com dúvida, caso não tenha certeza"
    )

structured_llm_router_query = llm.with_structured_output(RouteQuery)
structured_llm_router_rag = llm.with_structured_output(RouteRAG)

system_rag_prompt = """Você precisa decidir qual módulo usar para responder a pergunta do usuário:

Cobranca, Gestao, Assinatura, Vendas, Aleatorios.

Caso você tenha dúvidas de qual decidir pergunte ao cliente qual módulo ele está com dúvida.
"""

system_route_prompt = """Você é um especialista em encaminhar o usuário para o local correto.
Caso você não saiba para qual encaminhar, pergunte ao cliente qual módulo ele está com dúvida.

Existem cinco possibilidades:
Cobranca quando o usuário está com dúvida sobre cobrança.
Gestão quando o usuário está com dúvida sobre gestão.
Assinatura quando o usuário está com dúvida sobre assinatura.
Vendas quando o usuário está com dúvida sobre vendas.
Aleatorios que é quando o usuário não pergunta nada sobre o sistema.
"""

route_prompt = ChatPromptTemplate.from_messages(
    [
        ("system", system_route_prompt),
        ("human", "{question}"),
    ]
)

RAG_prompt = ChatPromptTemplate.from_messages(
    [
        ("system", system_rag_prompt),
        ("human", "{question}"),
    ]
)

# Questao de roteamento via query
question_router = route_prompt | structured_llm_router_query

# Questao de roteamento via RAG
RAG_router = RAG_prompt | structured_llm_router_rag