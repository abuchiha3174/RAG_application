from langchain_community.document_loaders import WebBaseLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
import re

def load_web_documents(urls: list[str], chunk_size: int = 500, chunk_overlap: int = 50):
    documents = []
    for url in urls:
        loader = WebBaseLoader(url)
        raw_docs = loader.load()
        splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
        documents.extend(splitter.split_documents(raw_docs))
    return documents


def extract_url_and_query(message: str):
    # Match first URL
    url_match = re.search(r"(https?://[^\s]+)", message)
    if url_match:
        url = url_match.group(0)
        query = message.replace(url, "").strip()
        return url, query
    return None, message.strip()