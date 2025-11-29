import pytest
from unittest.mock import MagicMock
from src.rag.retriever import Retriever

def test_retriever_retrieve():
    mock_embedder = MagicMock()
    mock_embedder.embed_text.return_value = [0.1, 0.2]
    
    mock_store = MagicMock()
    mock_store.search.return_value = [({'text': 'chunk1', 'source': 'doc1'}, 0.5)]
    
    retriever = Retriever(mock_embedder, mock_store)
    results = retriever.retrieve("query")
    
    assert len(results) == 1
    assert results[0]['text'] == 'chunk1'
    assert results[0]['score'] == 0.5
