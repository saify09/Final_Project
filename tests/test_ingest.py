import pytest
from src.ingest.chunker import chunk_text

def test_chunk_text_simple():
    text = "Hello world. This is a test."
    chunks = chunk_text(text, chunk_size=10, overlap=2)
    assert len(chunks) > 0
    assert "Hello" in chunks[0]

def test_chunk_text_overlap():
    text = "1234567890"
    chunks = chunk_text(text, chunk_size=5, overlap=2)
    # 12345, 45678, 7890
    assert len(chunks) == 3
    assert chunks[0] == "12345"
    assert chunks[1] == "45678"
    assert chunks[2] == "7890"
