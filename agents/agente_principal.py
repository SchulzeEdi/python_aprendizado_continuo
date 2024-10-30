from langchain_core.messages import HumanMessage, SystemMessage
from langgraph.prebuilt import create_react_agent, AgentExecutor
from langchain.memory import ConversationSummaryMemory
# from langgraph.checkpoint.memory import MemorySaver
from langchain_groq import ChatGroq
from dotenv import load_dotenv
from agente_programador import coder_tool
from agente_revisor import reviewer_tool
from agente_qa import tester_tool
import os

load_dotenv()

class AgentePrincipal:
  def __init__(self):
    self.model = ChatGroq(
      model= "mixtral-8x7b-32768",
      temperature=0.0,
      max_retries=2,
    )

    self.memory = ConversationSummaryMemory(llm=self.model, summary_filter=self.filter_useful_info)

    self.agent = create_react_agent(
      llm=self.model,
      tools=[coder_tool, reviewer_tool, tester_tool],
      prompt="Você é um agente de atendimento, do qual vai direcionar para o agente correto conforme o questionamento do usuário, você deve atender apenas o usuário caso ele peça algo relacionado a criar teste de código fonte, \
      codificar algo, ou revisar um código fonte. Caso contrário você deve ignorar a mensagem do usuário e falar que tem apenas conhecimento sobre código fonte, quando for algo relacionado ao assunto programação você deve passar \
      para os outros agentes, que contém conhecimento na área de programação.",
      verbose=True,
    )

    self.executor = AgentExecutor(agent=self.agent, tools=[coder_tool, reviewer_tool, tester_tool], memory=self.memory)


# from langchain_community.tools.tavily_search import TavilySearchResults
# search = TavilySearchResults(
#         max_results=2
#     )
#     tools = [search]