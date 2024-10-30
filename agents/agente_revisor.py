from langchain.tools import Tool
from langchain_groq import ChatGroq

class AgenteRevisor:
    def __init__(self):
        self.model = self.model = ChatGroq(
            model= "mixtral-8x7b-32768",
            temperature=0.0,
            max_retries=2,
        )

    def review_code(self, code):
        prompt = f"Revise o seguinte código e sugira melhorias: {code}"
        return self.model.invoke(prompt)

reviewer_tool = Tool(
    name="CodeReviewer",
    func=AgenteRevisor().review_code,
    description="Revisa o código fornecido e sugere melhorias."
)
