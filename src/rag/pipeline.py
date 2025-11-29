from typing import Dict
from .retriever import Retriever
from .generator import Generator

class RAGPipeline:
    def __init__(self, retriever: Retriever, generator: Generator):
        self.retriever = retriever
        self.generator = generator

    def answer(self, query: str) -> Dict[str, str]:
        """
        End-to-end QA pipeline.
        """
        # 1. Retrieve
        context_chunks = self.retriever.retrieve(query)
        
        # 2. Generate
        answer = self.generator.generate_answer(query, context_chunks)
        
        return {
            "query": query,
            "answer": answer,
            "source_documents": context_chunks
        }
