import pypdf
from typing import List, Dict, Any

def parse_pdf(file_path: str) -> str:
    """
    Extracts text from a PDF file.
    """
    text = ""
    try:
        reader = pypdf.PdfReader(file_path)
        for page in reader.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"
    except Exception as e:
        print(f"Error reading PDF {file_path}: {e}")
        return ""
    return text
