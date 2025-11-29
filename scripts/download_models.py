import os
from sentence_transformers import SentenceTransformer
import nltk

def download_models():
    print("Downloading Sentence Transformer model...")
    model_path = os.path.join("models", "all-MiniLM-L6-v2")
    model = SentenceTransformer('all-MiniLM-L6-v2')
    model.save(model_path)
    print(f"Model saved to {model_path}")

    print("Downloading NLTK data...")
    nltk.download('punkt')
    print("NLTK data downloaded.")

if __name__ == "__main__":
    if not os.path.exists("models"):
        os.makedirs("models")
    download_models()
