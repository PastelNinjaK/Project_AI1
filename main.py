import dotenv import load_dotenv
from pydantic import BaseModel
from langchain_openai import ChatOpenAI
from langchain_openai import ChatAnthropic

load_dotenv()


# llm2 = ChatOpenAI(model = "gpt-4o-min")
llm = ChatAnthropic(model = "Claude-3-5-sonnet-20241022")