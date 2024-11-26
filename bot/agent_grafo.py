from dotenv import load_dotenv
from typing import List
from typing_extensions import TypedDict
from langgraph.graph import StateGraph, START, END
from bot.retrieve.retrieve_modulos import retrieve_cobranca, retrieve_gestao, retrieve_assinatura, retrieve_vendas, generate, generate_random, route_question

load_dotenv()

class GraphState(TypedDict):
    question: str
    generation: str
    Cobranca: str
    Gestao: str
    Assinatura: str
    Vendas: str
    Aleatorios: str
    documents: List[str]
    memory: List[str]

workflow = StateGraph(GraphState)
workflow.add_node("generate", generate)
workflow.add_node("generate_random", generate_random)
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
        "Aleatorios": "generate_random",
    }
)

workflow.add_edge("retrieve_cobranca", "generate")
workflow.add_edge("retrieve_gestao", "generate")
workflow.add_edge("retrieve_assinatura", "generate")
workflow.add_edge("retrieve_vendas", "generate")
workflow.add_edge("generate_random", END)

app = workflow.compile()

def send_question(question):
    result = app.invoke(input = {
        "question": question
    })
    return result["generation"]