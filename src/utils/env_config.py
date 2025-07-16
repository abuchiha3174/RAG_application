import os
from dotenv import load_dotenv

class EnvConfig:
    def __init__(self):
        load_dotenv()
        os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY") 
        os.environ["LANGSMITH_API_KEY"] = os.getenv("LANGSMITH_API_KEY")
        os.environ["LANGSMITH_TRACING"] = "true"
        os.environ["HF_API_TOKEN"] = os.getenv("HF_API_TOKEN")
        os.environ["COHERE_API_KEY"] = os.getenv("COHERE_API_KEY")
        os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

        # Optional logging
        print("[EnvConfig] Environment variables set.")