from langchain.llms import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

# Accessing the OPENAI KEY
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

# Simple LLM call Using LangChain
llm = OpenAI(model_name="text-davinci-003", openai_api_key=OPENAI_API_KEY)
question = "List top 5 ERP software in 2023 with short description."
print(question, llm(question))

