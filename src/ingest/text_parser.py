import docx
import os
from .pdf_parser import parse_pdf
from .image_parser import parse_image
from .video_parser import parse_video

def parse_docx(file_path: str) -> str:
    """
    Extracts text from a DOCX file.
    """
    text = ""
    try:
        doc = docx.Document(file_path)
        for para in doc.paragraphs:
            text += para.text + "\n"
    except Exception as e:
        print(f"Error reading DOCX {file_path}: {e}")
        return ""
    return text

def parse_text_file(file_path: str) -> str:
    """
    Extracts text from .txt or .md files.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return f.read()
    except Exception as e:
        print(f"Error reading text file {file_path}: {e}")
        return ""

def parse_file(file_path: str) -> str:
    """
    Dispatcher for file parsing based on extension.
    """
    ext = os.path.splitext(file_path)[1].lower()
    if ext == '.pdf':
        return parse_pdf(file_path)
    elif ext == '.docx':
        return parse_docx(file_path)
    elif ext in ['.txt', '.md', '.py']:
        return parse_text_file(file_path)
    elif ext in ['.png', '.jpg', '.jpeg', '.bmp', '.tiff']:
        return parse_image(file_path)
    elif ext in ['.mp4', '.avi', '.mov', '.mkv']:
        return parse_video(file_path)
    else:
        print(f"Unsupported file type: {ext}")
        return ""
