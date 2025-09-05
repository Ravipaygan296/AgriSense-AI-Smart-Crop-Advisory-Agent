import os
import faiss
import pickle

class VectorDB:
    def __init__(self, index_path="data/vector.index", store_path="data/store.pkl"):
        self.index_path = index_path
        self.store_path = store_path
        self.index = None
        self.docs = []

        if os.path.exists(index_path) and os.path.exists(store_path):
            self.load()

    def build(self, embeddings, docs):
        self.index = faiss.IndexFlatL2(embeddings.shape[1])
        self.index.add(embeddings)
        self.docs = docs
        self.save()

    def query(self, vector, top_k=3):
        if self.index is None:
            raise ValueError("Index not built")
        distances, indices = self.index.search(vector, top_k)
        return [self.docs[i] for i in indices[0]]

    def save(self):
        faiss.write_index(self.index, self.index_path)
        with open(self.store_path, "wb") as f:
            pickle.dump(self.docs, f)

    def load(self):
        self.index = faiss.read_index(self.index_path)
        with open(self.store_path, "rb") as f:
            self.docs = pickle.load(f)

