import os
os.environ.pop("SSL_CERT_FILE", None)

from langchain_community.chat_models import ChatOpenAI
from langchain.schema import HumanMessage
from dotenv import load_dotenv
load_dotenv()

llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0.7, openai_api_key=os.getenv("OPENAI_API_KEY"))

def simple_prompt_response(prompt: str):
    response = llm([HumanMessage(content=prompt)])
    return response.content
