import os
import sys
import logging
from urllib.parse import urlparse
from langchain_community.document_loaders import (
    TextLoader,
    PyPDFLoader,
    CSVLoader,
    JSONLoader,
    UnstructuredWordDocumentLoader,
    UnstructuredHTMLLoader,
    WebBaseLoader
)
from src.exception import CustomException

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

class DataIngestionLoader:
    def __init__(self, source: str):
        self.source = source
        try:
            self.loader = self._select_loader()
            logging.info(f"✅ Loader selected for source: {self.source}")
        except Exception as e:
            error_msg = CustomException(e, sys)
            logging.error("❌ Loader initialization failed:\n" + str(error_msg))
            raise error_msg

    def _select_loader(self):
        if self._is_url(self.source):
            return self._load_web()

        ext = os.path.splitext(self.source)[1].lower()

        loader_map = {
            ".txt": self._load_txt,
            ".pdf": self._load_pdf,
            ".csv": self._load_csv,
            ".json": self._load_json,
            ".docx": self._load_docx,
            ".doc": self._load_docx,
            ".html": self._load_html
        }

        if ext not in loader_map:
            raise CustomException(Exception("Unsupported file type"), f"Unsupported file type: {ext}")

        return loader_map[ext]()

    def _is_url(self, input_str: str) -> bool:
        try:
            result = urlparse(input_str)
            return all([result.scheme in ("http", "https"), result.netloc])
        except Exception:
            return False

    # Modular loader functions
    def _load_txt(self):
        return TextLoader(self.source)

    def _load_pdf(self):
        return PyPDFLoader(self.source)

    def _load_csv(self):
        return CSVLoader(self.source)

    def _load_json(self):
        return JSONLoader(self.source)

    def _load_docx(self):
        return UnstructuredWordDocumentLoader(self.source)

    def _load_html(self):
        return UnstructuredHTMLLoader(self.source)

    def _load_web(self):
        return WebBaseLoader(self.source)

    def load(self):
        try:
            docs = self.loader.load()
            logging.info(f"📥 Loaded {len(docs)} document(s) from: {self.source}")

            if docs and hasattr(docs[0], 'page_content'):
                preview = docs[0].page_content[:300].replace("\n", " ").strip()
                logging.debug(f"📝 First document preview: {preview}")

            return docs
        except Exception as e:
            error_msg = CustomException(e, sys)
            logging.error("❌ Failed to load documents:\n" + str(error_msg))
            raise error_msg

