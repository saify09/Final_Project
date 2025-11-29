import faiss
import numpy as np
import pickle
import os
from typing import List, Dict, Tuple

class VectorStore:
    def __init__(self, dimension: int = 384):
        self.dimension = dimension
        self.index = faiss.IndexFlatL2(dimension)
        self.metadata: List[Dict] = []

    def add_embeddings(self, embeddings: np.ndarray, metadata: List[Dict]):
        """
        Adds embeddings and corresponding metadata to the index.
        """
        if len(embeddings) != len(metadata):
            raise ValueError("Number of embeddings and metadata items must match.")
        
        self.index.add(np.array(embeddings).astype('float32'))
        self.metadata.extend(metadata)

    def search(self, query_embedding: np.ndarray, k: int = 5) -> List[Tuple[Dict, float]]:
        """
        Searches the index for the k nearest neighbors.
        Returns a list of (metadata, distance) tuples.
        """
        query_embedding = np.array([query_embedding]).astype('float32')
        distances, indices = self.index.search(query_embedding, k)
        
        results = []
        for i, idx in enumerate(indices[0]):
            if idx != -1 and idx < len(self.metadata):
                results.append((self.metadata[idx], float(distances[0][i])))
        
        return results

    def save(self, directory: str):
        """
        Saves the index and metadata to disk.
        """
        if not os.path.exists(directory):
            os.makedirs(directory)
            
        faiss.write_index(self.index, os.path.join(directory, "index.faiss"))
        with open(os.path.join(directory, "metadata.pkl"), "wb") as f:
            pickle.dump(self.metadata, f)

    def load(self, directory: str):
        """
        Loads the index and metadata from disk.
        """
        index_path = os.path.join(directory, "index.faiss")
        metadata_path = os.path.join(directory, "metadata.pkl")
        
        if os.path.exists(index_path) and os.path.exists(metadata_path):
            self.index = faiss.read_index(index_path)
            with open(metadata_path, "rb") as f:
                self.metadata = pickle.load(f)
            return True
        return False
