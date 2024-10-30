from .llm import build_llm
from functools import partial

llm_map = {
  "groq": partial(build_llm, model_name="mixtral-8x7b-32768")
}