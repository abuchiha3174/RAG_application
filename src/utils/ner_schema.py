import json
import sys
from langchain.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.runnables import RunnableSequence
from src.exception import CustomException

EXTRACTION_PROMPT = """
Extract up to 10 relevant fields from the query as JSON.
Use standard fields if present: domain, method, framework, task, language, 
dataset, tool, role, location, time, etc.
If none apply, replace with the most relevant fields based on the query.
Omit or set null if irrelevant.
Query: {query}
Context:
{context}
"""


class SchemaNER:
    def __init__(self, model_name="gpt-3.5-turbo", temperature=0):
        self.prompt = PromptTemplate.from_template(EXTRACTION_PROMPT)
        self.llm = ChatOpenAI(model=model_name, temperature=temperature)
        self.chain = self.prompt | self.llm 
    
    
    # Fill user input into a prompt asking for domain, method, and framework
    # Send the prompt to the LLM and get the response
    # The response is a JSON-like string with the extracted fields  

    def extract(self, query: str, context: str = "") -> dict:
        try:
            response = self.chain.invoke({"query": query, "context": context})
            print(f"📦 Raw LLM response: {response}")
            parsed_response = json.loads(response.content.strip())
            print(f"✅ Parsed JSON: {parsed_response}")
            return parsed_response
        except Exception as e:
            raise CustomException(e, sys)
