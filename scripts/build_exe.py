import PyInstaller.__main__
import os

def build_exe():
    PyInstaller.__main__.run([
        'run_app.py',
        '--name=EduBuddy',
        '--onefile',
        '--clean',
        '--add-data=app.py;.',
        '--add-data=src;src',
        '--add-data=ui;ui',
        '--add-data=models;models',  # Assumes models are downloaded
        '--hidden-import=streamlit',
        '--hidden-import=sentence_transformers',
        '--hidden-import=faiss',
        '--hidden-import=pypdf',
        '--hidden-import=docx',
        '--hidden-import=sumy',
        '--hidden-import=easyocr',
        '--hidden-import=cv2',
        '--hidden-import=plotly',
        '--collect-all=streamlit',
        '--collect-all=sentence_transformers',
        '--collect-all=sumy',
        '--collect-all=easyocr',
        '--collect-all=plotly',
        '--exclude-module=langchain',
    ])

if __name__ == "__main__":
    if not os.path.exists("models"):
        print("Please run scripts/download_models.py first!")
    else:
        build_exe()
