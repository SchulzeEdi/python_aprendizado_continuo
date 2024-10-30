from langchain_core.messages import HumanMessage, SystemMessage
from langgraph.prebuilt import create_react_agent
from langgraph.checkpoint.memory import MemorySaver

#Este agente é o revisor de código, vai revisar todos os códigos do programador e passar logo em seguida para o qa tester.
def revisor_codigo(code_text):
  agent_executor = create_react_agent(llm, tools, checkpointer=memory)
  pass

#Este agente é o gerador de códigos do sistema, vai programar todas as demandas que o enviarem e passar para o revisor.
def gerador_de_codigo(input_text):
  agent_executor = create_react_agent(llm, tools, checkpointer=memory)
  return f"""você deve programar um código fonte na linguagem python, este código vai ser revisado, então você deve programar
  da melshor forma possível, este código deve estar documentado, o que foi solicitado é o seguinte: {input_text}"""

#Este agente é o qa tester, do qual vai criar testes para o código fonte e testar ele conforme criou suas funções.
def qa_tester_codigo(code_text):
  agent_executor = create_react_agent(llm, tools, checkpointer=memory)
  pass