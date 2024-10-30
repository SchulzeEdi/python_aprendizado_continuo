from langchain.tools import Tool
from langchain_groq import ChatGroq

class AgenteQa:
    def __init__(self):
        self.model = ChatGroq(
            model= "mixtral-8x7b-32768",
            temperature=0.0,
            max_retries=2,
        )

    def test_code(self, code):
        prompt = f"Crie testes para o seguinte código: {code}"
        return self.model.invoke(prompt)

tester_tool = Tool(
    name="CodeTester",
    func=AgenteQa().test_code,
    description="Gera e executa testes para o código fornecido."
)
