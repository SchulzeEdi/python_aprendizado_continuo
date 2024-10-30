from langchain_groq import ChatGroq

def build_llm(model_name):
  return ChatGroq(
    model= model_name,
    temperature=0.0,
    max_retries=2,
  )