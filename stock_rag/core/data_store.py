from elasticsearch import Elasticsearch
from langchain_openai import OpenAIEmbeddings
from langchain_elasticsearch import ElasticsearchStore
from config import Config

class DataStore:
    def __init__(self):
        self.es_client = Elasticsearch([f"http://{Config.ELASTICSEARCH_HOST}:{Config.ELASTICSEARCH_PORT}"])
        self.embeddings = OpenAIEmbeddings(model=Config.EMBEDDING_MODEL)
        self.vector_store = ElasticsearchStore(
            es_connection=self.es_client,
            index_name="stock_articles",
            embedding=self.embeddings
        )

    def add_documents(self, documents):
        return self.vector_store.add_documents(documents)

    def similarity_search(self, query, k=3):
        return self.vector_store.similarity_search(query, k=k)
