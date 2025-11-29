import os
from transformers import pipeline

class Generator:
    def __init__(self, model_name: str = "MBZUAI/LaMini-Flan-T5-77M"):
        self.model_name = model_name
        self.pipe = None
        self._load_model()

    def _load_model(self):
        """
        Loads the local LLM using Transformers pipeline.
        """
        try:
            print(f"Loading model {self.model_name}...")
            # Use text2text-generation for T5 models
            self.pipe = pipeline("text2text-generation", model=self.model_name, max_length=512)
            print(f"Model {self.model_name} loaded successfully.")
        except Exception as e:
            print(f"Failed to load model: {e}")
            self.pipe = None

    def generate_answer(self, query: str, context_chunks: list) -> str:
        """
        Generates an answer based on the query and retrieved context.
        """
        context_text = "\n\n".join([c['text'] for c in context_chunks])
        
        if self.pipe:
            # Prompt engineering for T5
            prompt = f"Answer the following question based on the context below:\n\nContext:\n{context_text}\n\nQuestion: {query}\n\nAnswer:"
            
            # Truncate context if too long (simple heuristic, T5 has 512 limit usually)
            if len(prompt) > 2000:
                prompt = prompt[:2000]
            
            output = self.pipe(prompt, max_length=256, do_sample=False)
            return output[0]['generated_text']
        else:
            return f"**LLM not loaded.**\n\nContext:\n{context_text}"
