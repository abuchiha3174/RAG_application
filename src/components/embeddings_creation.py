from langchain_openai import OpenAIEmbeddings
from langchain_community.embeddings import (
    HuggingFaceInferenceAPIEmbeddings,
    CohereEmbeddings
)
from typing import Literal
import os
from dotenv import load_dotenv

load_dotenv()

class EmbeddingBuilder:
    def __init__(self):
        self.hf_key = os.getenv("HF_API_TOKEN")
        self.cohere_key = os.getenv("COHERE_API_KEY")
        self.openai_key = os.getenv("OPENAI_API_KEY")
        self.embeddings = None

    def hf_embeddings(self, model_name: str = "sentence-transformers/all-MiniLM-L6-v2"):
        # Uses Hugging Face Inference API (cloud-hosted, with API key)
        self.embeddings = HuggingFaceInferenceAPIEmbeddings(
            api_key=self.hf_key,
            model_name=model_name
        )
        return self.embeddings

    def openAI_embeddings(self):
        self.embeddings = OpenAIEmbeddings(api_key=self.openai_key)
        return self.embeddings
        
    def cohere_embeddings(self):
        self.embeddings = CohereEmbeddings(cohere_api_key=self.cohere_key)
        return self.embeddings