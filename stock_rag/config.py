import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    ELASTICSEARCH_HOST = os.getenv("ELASTICSEARCH_HOST", "localhost")
    ELASTICSEARCH_PORT = os.getenv("ELASTICSEARCH_PORT", "9200")
    MODEL_NAME = "gpt-4"
    EMBEDDING_MODEL = "text-embedding-ada-002"
    CHUNK_SIZE = 1000
    CHUNK_OVERLAP = 200
