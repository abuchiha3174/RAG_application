from dotenv import load_dotenv
import os
import sys
from pinecone import Pinecone
from src.exception import CustomException
import logging

# loading environment variables
load_dotenv()
pinecone_key = os.getenv("PINECONE_KEY")
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# Initialize a Pinecone client with your API key
pc = Pinecone(api_key=pinecone_key)

index_name = "nas-paper"

def create_or_check_index(index_name):
    try:
        logging.info("Checking Pinecone index status...")
        indexes = pc.list_indexes()
        # logging.info(f"All indexes: {indexes}")
        # print("All indexes:", indexes)
        if pc.has_index(index_name):
            msg = f"Index '{index_name}' already exists."
            logging.info(msg)
            return msg
        else:
            pc.create_index_for_model(
                name=index_name,
                cloud="aws",
                region="us-east-1",
                embed={
                    "model": "llama-text-embed-v2",
                    "field_map": {"text": "chunk_text"}
                }
            )
            msg = f"Index '{index_name}' created."
            logging.info(msg)
            return msg

    except Exception as e:
        error_msg = CustomException(e, sys)
        logging.error("❌ Exception Occurred:\n" + str(error_msg))
        
        # Try parsing response body if it's HTTPError
        if hasattr(e, 'response') and hasattr(e.response, 'text'):
            try:
                error_json = json.loads(e.response.text)
                pretty_error = json.dumps(error_json, indent=2)
                return f"<pre>{str(error_msg)}\n\n{pretty_error}</pre>"
            except:
                return f"<pre>{str(error_msg)}</pre>"
        return f"<pre>{str(error_msg)}</pre>"
    


