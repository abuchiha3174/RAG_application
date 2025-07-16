import json
from flask import Flask,request,render_template
import logging
import os
import sys
from src.components.vector_db import create_or_check_index
from src.components.llms import invoke_OPENAI
from src.utils.env_config import EnvConfig
from src.components.prompt_builder import PromptBuilder
from src.utils.ner_schema import SchemaNER
from src.components.data_ingestion import DataIngestionLoader
from src.exception import CustomException
from src.utils.web_loader import extract_url_and_query

from src.components.embeddings_creation import EmbeddingBuilder
from urllib.parse import urlparse

EnvConfig()
ner = SchemaNER()
pb = PromptBuilder(
    system_template = """You are a helpful assistant. 
        Use the provided context if available to answer the user's question accurately.

        {context_section}
        """,
    user_template="{question}"
)
builder = EmbeddingBuilder()


logging.basicConfig(level=logging.INFO)
application=Flask(__name__)

app=application

@app.route("/", methods=["GET", "POST"])
def index():
    pinecone_status = create_or_check_index("nas-paper")
    user_message = None
    bot_response = None
    extracted_fields = None
    prompt_text = None
    error_message = None
    parsed_response = None 

    if request.method == "POST":
        try:
            user_message = request.form.get("message")
            uploaded_file = request.files.get("file")
            url_candidate, possible_query = extract_url_and_query(user_message.strip())
            context = ""
            
            def is_url(text):
                try:
                    result = urlparse(text)
                    print(f"URL parsed as: {result}")
                    return all([result.scheme in ("http", "https"), result.netloc])
                except Exception as e:
                    print(f"URL check failed: {e}")
                    return False

            # 🔍 First, try file
            if uploaded_file and uploaded_file.filename != "":
                upload_dir = "uploads"
                os.makedirs(upload_dir, exist_ok=True)
                file_path = os.path.join(upload_dir, uploaded_file.filename)
                uploaded_file.save(file_path)

                loader = DataIngestionLoader(file_path)
                docs = loader.load()
                context = "\n".join([doc.page_content for doc in docs])

            # 🔍 Otherwise, check if message is a URL
            elif url_candidate and is_url(url_candidate):
                print("✅ Detected URL with possible query")
                loader = DataIngestionLoader(url_candidate)
                docs = loader.load()
                context = "\n".join([doc.page_content for doc in docs])
                user_message = possible_query or url_candidate

            # 💬 Run NER on original user message (always)
            fields = ner.extract(query=user_message, context=context)
            parsed_response = fields
            extracted_fields = fields

            # Add context and question to prompt fields
            parsed_response["question"] = user_message
            parsed_response["context_section"] = context

            prompt_messages = pb.get_prompt(**parsed_response)
            prompt_text = "\n".join([f"{msg.type.upper()}: {msg.content}" for msg in prompt_messages])

            bot_response = invoke_OPENAI(prompt_messages)

        except Exception as e:
            logging.error("❌ Exception occurred:", exc_info=True)
            error_message = str(CustomException(e, sys))
            
            
    return render_template(
        "index.html",
        pinecone_status=pinecone_status,
        user_message=user_message,
        bot_response=bot_response,
        extracted_fields=extracted_fields,
        prompt_text=prompt_text,
        extracted_json=parsed_response,
        error_message=error_message
    )





if __name__=="__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)        


