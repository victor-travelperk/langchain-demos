#!/usr/bin/env python3

import os
from dotenv import load_dotenv
from langchain import LLMChain, PromptTemplate
from langchain.llms import OpenAI

# Load environment variables from .env file
load_dotenv()

# Access environment variables

def get_prompt_template():
    template = """Question: Tell me the origin story of the following marvel character {character}

    Answer:"""

    # Prepare prompt information
    return PromptTemplate(template=template, input_variables=["character"])

def get_model():
    api_key = os.getenv("OPENAI_API_KEY")
    model = "text-davinci-003"
    temperature = 0
    # Choose a model
    return OpenAI(model_name=model, openai_api_key=api_key, temperature=temperature)


llm_chain = LLMChain(
    prompt=get_prompt_template(),
    llm=get_model(),
)

questions = [
    {'character': 'Ironman'},
    {'character': 'Morbius'},
    {'character': 'The green goblin'},
    {'character': 'Luke Cage'},
]

res = llm_chain.generate(questions)
print(res)