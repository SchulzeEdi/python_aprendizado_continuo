from langchain.tools import Tool
from langchain_groq import ChatGroq

class AgenteProgramador:
    def __init__(self):
        self.model = ChatGroq(
            model= "mixtral-8x7b-32768",
            temperature=0.0,
            max_retries=2,
        )

    def generate_code(self, request):
        prompt = f"Escreva o código para o seguinte pedido: {request}"
        return self.model.invoke(prompt)

coder_tool = Tool(
    name="CodeGenerator",
    func=AgenteProgramador().generate_code,
    description="Gera código baseado em uma solicitação específica de programação."
)