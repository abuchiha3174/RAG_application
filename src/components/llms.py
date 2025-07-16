import os 
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from typing import Union, List
from langchain.schema import BaseMessage
load_dotenv()



def setup_OPENAIAPI_Key(key=None):
     if key:
        os.environ['OPENAI_API_KEY'] = key



def invoke_OPENAI(
    msg: Union[str, List[BaseMessage]] = "what is the weather today in Mumbai?",
    key: str = None,
    model_name: str = "gpt-4o",
    temperature: float = 0.0
):
    setup_OPENAIAPI_Key(key)
    llm = ChatOpenAI(model=model_name, temperature=temperature, verbose=True)
    result = llm.invoke(msg)
    print(result)
    return result.content