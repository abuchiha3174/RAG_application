import json
import sys
from langchain.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.runnables import RunnableSequence
from src.exception import CustomException
import logging

logging.basicConfig(level=logging.INFO)

EXTRACTION_PROMPT = """
You are a helpful assistant that listens carefully to what people ask and captures the key details they’re really looking for.

Given a query and some optional context, extract the most relevant pieces of information that would help someone understand or respond clearly. Focus on what the person is trying to do, talk about, or figure out.

Return your output as a JSON object with up to 10 meaningful fields. Use these standard fields when possible:

- intent: what the person wants to know, do, or solve
- domain: general topic or area of interest (e.g. travel, tech, health, education)
- task: specific request or action being described
- what: the main subject, item, or idea mentioned
- who: any person, group, or role involved
- where: any location, place, or environment (real or virtual)
- when: any time-related detail or urgency
- why: reason, motivation, or purpose behind the query
- tools: any methods, platforms, tools, or resources mentioned
- summary: a plain-language summary of what the query is about

If a field doesn't apply or isn’t mentioned, just omit it or set it to null.

Be concise, avoid assumptions, and use only the information provided.

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
        logging.info("🔍 Starting schema-based NER extraction.")
        logging.info(f"📥 User Query: {query}")
        if context:
            logging.info(f"📘 Context Provided: {context[:100]}...")

        try:
            response = self.chain.invoke({"query": query, "context": context})
            print("🤖 Thinking... extracting structured meaning from your input.")

            logging.info("📦 Raw LLM response received.")
            print(f"📦 Raw LLM response: {response.content[:200]}...")  # Optional preview

            parsed_response = json.loads(response.content.strip())
            logging.info("✅ Successfully parsed JSON response.")
            print("✅ Done! Here's what I found:")
            print(json.dumps(parsed_response, indent=2))

            return parsed_response

        except json.JSONDecodeError as decode_err:
            logging.error("❌ Failed to parse response into JSON.")
            print("⚠️ Sorry, I couldn't understand the response format.")
            raise CustomException(decode_err, sys)

        except Exception as e:
            logging.exception("❌ Unexpected error during schema extraction.")
            print("❗ Something went wrong while trying to extract information.")
            raise CustomException(e, sys)
