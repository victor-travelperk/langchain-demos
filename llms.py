import os
from langchain.llms import OpenAI

def get_model():
    api_key = os.getenv("OPENAI_API_KEY")
    model = "text-davinci-003"
    temperature = 0
    return OpenAI(model_name=model, openai_api_key=api_key, temperature=temperature)