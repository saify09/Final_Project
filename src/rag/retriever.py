from typing import List, Dict, Tuple
from ..embed.embedder import Embedder
from ..embed.indexer import VectorStore

class Retriever:
    def __init__(self, embedder: Embedder, vector_store: VectorStore):
        self.embedder = embedder
        self.vector_store = vector_store

    def retrieve(self, query: str, k: int = 3) -> List[Dict]:
        """
        Retrieves top k relevant chunks for a given query.
        """
        query_embedding = self.embedder.embed_text(query)
        results = self.vector_store.search(query_embedding, k)
        
        # Flatten results to just return metadata (which contains text)
        retrieved_chunks = []
        for metadata, score in results:
            chunk_data = metadata.copy()
            chunk_data['score'] = score
            retrieved_chunks.append(chunk_data)
            
        return retrieved_chunks
