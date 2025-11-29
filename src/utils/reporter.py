from fpdf import FPDF
import tempfile

def generate_pdf_report(student_name: str, roll_no: str, quiz_history: list) -> bytes:
    """
    Generates a PDF report and returns the bytes.
    """
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", 'B', 16)
    pdf.cell(0, 10, "EduBuddy Progress Report", ln=True, align='C')
    
    pdf.set_font("Arial", size=12)
    pdf.ln(10)
    pdf.cell(0, 10, f"Student Name: {student_name}", ln=True)
    pdf.cell(0, 10, f"Roll Number: {roll_no}", ln=True)
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
