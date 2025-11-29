# EduBuddy - AI-Powered Offline Learning Companion
## Certification Presentation Notes (A to Z)

### 1. PROJECT OVERVIEW
*   **Project Name**: EduBuddy
*   **Tagline**: Your AI-Powered Offline Learning Companion.
*   **Problem Statement**: Students often struggle with organizing study materials, finding specific answers in large documents, and studying offline without internet access.
*   **Solution**: A local, privacy-focused AI application that ingests documents (PDF, Video, Images), allows you to "chat" with them, generates quizzes for practice, and tracks your learning progress—all without needing the cloud.

### 2. CORE ARCHITECTURE & TECH STACK
*   **Frontend**: **Streamlit** (Python). Chosen for rapid prototyping and interactive data apps.
*   **Language**: **Python 3.10+**. The standard for AI/ML development.
*   **AI Models (Local)**:
    *   **LLM**: `MBZUAI/LaMini-Flan-T5-77M` (Text Generation). Small, fast, offline-capable.
    *   **Embeddings**: `sentence-transformers/all-MiniLM-L6-v2`. Converts text to numbers for search.
*   **Vector Database**: **FAISS** (Facebook AI Similarity Search). Stores embeddings for fast retrieval.
*   **Computer Vision**:
    *   **EasyOCR**: Extracts text from Images and Video frames.
    *   **OpenCV**: Processes video files to capture frames.
*   **Analytics**: **Linear Regression** (NumPy) for predicting future quiz scores.
*   **Visualization**: **Plotly** for interactive progress charts.

### 3. PROJECT STRUCTURE (The "Code Map")
*   **`app.py`**: The **Main Entry Point**. It orchestrates the UI, manages Session State (memory), and calls all other modules.
*   **`src/`**: The "Brain" of the application.
    *   **`ingest/`**: Handles file processing.
        *   `text_parser.py`: Reads PDF, DOCX, TXT.
        *   `image_parser.py`: Uses EasyOCR for images.
        *   `video_parser.py`: Extracts frames and reads text from videos.
        *   `chunker.py`: Splits large text into smaller pieces (chunks) for the AI.
    *   **`embed/`**: Handles memory.
        *   `embedder.py`: Converts text chunks into vector embeddings.
        *   `indexer.py`: Manages the FAISS database (save/load/search).
    *   **`rag/`**: Retrieval Augmented Generation (The AI Logic).
        *   `retriever.py`: Finds the most relevant chunks for a user question.
        *   `generator.py`: Uses the LLM to write an answer based on those chunks.
        *   `pipeline.py`: Connects Retriever + Generator.
    *   **`utils/`**: Helpers.
        *   `quiz_generator.py`: Creates MCQs from text.
        *   `analytics.py`: Predicts future scores.
        *   `summarizer.py`: Summarizes long documents.
*   **`ui/`**: The "Face" of the application.
    *   `styles.py`: Contains the CSS for the Premium Light/Dark themes.
    *   `components.py`: Reusable UI widgets (cards, sidebar).

### 4. DATA FLOW (How it Works)
**Scenario 1: Ingestion (Upload)**
1.  User uploads a file (e.g., `notes.pdf`).
2.  `text_parser.py` extracts the raw text.
3.  `chunker.py` splits it into 1000-character chunks (with overlap).
4.  `embedder.py` converts chunks into vectors.
5.  `indexer.py` saves these vectors into FAISS.

**Scenario 2: RAG (Chatting)**
1.  User asks: "What is photosynthesis?"
2.  `retriever.py` searches FAISS for chunks similar to "photosynthesis".
3.  It retrieves the top 3 most relevant chunks (Context).
4.  `generator.py` takes the Question + Context and feeds it to the LLM.
5.  LLM generates the answer: "Photosynthesis is..."

### 5. KEY FEATURES
1.  **Multi-Format Ingestion**: Supports PDFs, Word docs, Text files, Images (OCR), and Videos.
2.  **RAG Chatbot**: Accurate answers based *only* on your documents (no hallucinations).
3.  **Quiz Mode**:
    *   Auto-generates questions from your content.
    *   **Instant Feedback**: Green for Correct, Red for Wrong.
4.  **Progress Tracking**:
    *   Visualizes quiz history.
    *   **Forecasting**: Uses Linear Regression to predict your next score.
5.  **Premium UI**:
    *   **Glassmorphism**: Modern, translucent design.
    *   **Dual Theme**: Fully supported Light and Dark modes.

### 6. CHALLENGES & SOLUTIONS
*   **Challenge**: "App not opening" on Cloud.
    *   **Solution**: Identified missing system dependencies (`libgl1` for OpenCV) and added `packages.txt`.
*   **Challenge**: Invisible text in Dark Mode.
    *   **Solution**: Refactored CSS to use Streamlit's native variables (`var(--text-color)`), ensuring perfect contrast in both modes.
*   **Challenge**: Processing large videos.
    *   **Solution**: Implemented frame skipping (process 1 frame every 2 seconds) to balance speed and accuracy.

### 7. FUTURE SCOPE
*   **Voice Interface**: Add Speech-to-Text for asking questions verbally.
*   **Cloud Sync**: Optional Google Drive integration for backup.
*   **More Models**: Support for Llama-2 or Mistral for smarter reasoning.

### 8. CONCLUSION
EduBuddy successfully demonstrates the power of **Local AI**. It solves the connectivity gap, ensures data privacy, and provides a comprehensive learning ecosystem for students.
