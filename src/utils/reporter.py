from fpdf import FPDF
import tempfile

def generate_pdf_report(student_name: str, roll_no: str, quiz_history: list, analytics: dict = None) -> bytes:
    """
    Generates a PDF report and returns the bytes.
    """
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", 'B', 16)
    pdf.cell(0, 10, "EduBuddy Progress Report", ln=True, align='C')
    
    # Helper to sanitize text for Latin-1 (removes emojis/special chars)
    def sanitize(text):
        # Replace specific emojis with text equivalents first
        text = str(text).replace("🚀", " (Rising)").replace("📉", " (Dropping)").replace("⚖️", " (Stable)")
        return text.encode('latin-1', 'replace').decode('latin-1')

    pdf.set_font("Arial", size=12)
    pdf.ln(10)
    pdf.cell(0, 10, f"Student Name: {sanitize(student_name)}", ln=True)
    pdf.cell(0, 10, f"Roll Number: {sanitize(roll_no)}", ln=True)
    pdf.ln(10)
    
    # Analytics Section
    if analytics:
        pdf.set_font("Arial", 'B', 14)
        pdf.cell(0, 10, "Performance Analytics", ln=True)
        pdf.set_font("Arial", size=12)
        pdf.cell(0, 10, f"Average Score: {sanitize(analytics.get('average', 'N/A'))}", ln=True)
        pdf.cell(0, 10, f"Predicted Next Score: {sanitize(analytics.get('predicted_score', 'N/A'))}", ln=True)
        pdf.cell(0, 10, f"Trend: {sanitize(analytics.get('trend', 'N/A'))}", ln=True)
        pdf.ln(10)
    
    pdf.set_font("Arial", 'B', 14)
    pdf.cell(0, 10, "Quiz Performance History", ln=True)
    pdf.set_font("Arial", size=12)
    
    if not quiz_history:
        pdf.cell(0, 10, "No quizzes taken yet.", ln=True)
    else:
        for i, score in enumerate(quiz_history):
            pdf.cell(0, 10, f"Quiz {i+1}: Score {score}", ln=True)
            
    # Return as bytes
    return pdf.output(dest='S').encode('latin-1')
