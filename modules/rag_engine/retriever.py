from utils.db_utils import VectorDB
from langchain.embeddings import OpenAIEmbeddings
import numpy as np

class Retriever:
    def __init__(self):
        self.embeddings = OpenAIEmbeddings()
        self.db = VectorDB()

    def build_index(self, documents):
        vectors = []
        texts = []
        for doc in documents:
            vector = self.embeddings.embed_query(doc.page_content if hasattr(doc, "page_content") else doc["content"])
            vectors.append(vector)
            texts.append(doc.page_content if hasattr(doc, "page_content") else doc["content"])
        vectors = np.array(vectors).astype("float32")
        self.db.build(vectors, texts)

    def search(self, query, top_k=3):
        query_vector = np.array([self.embeddings.embed_query(query)]).astype("float32")
        results = self.db.query(query_vector, top_k=top_k)
        return results

