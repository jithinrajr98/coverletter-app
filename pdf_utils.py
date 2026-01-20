import pdfplumber
from fpdf import FPDF
import os

# Get the directory where this module is located
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FONTS_DIR = os.path.join(BASE_DIR, "fonts")


def extract_text_from_pdf(uploaded_file) -> str:
    """Extract text from an uploaded PDF file.

    Args:
        uploaded_file: Streamlit UploadedFile object

    Returns:
        Extracted text as string
    """
    text = ""
    with pdfplumber.open(uploaded_file) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"
    return text.strip()


def create_cover_letter_pdf(text: str, applicant_name: str, language: str = "en") -> bytes:
    """Create a PDF from cover letter text.

    Args:
        text: Cover letter content
        applicant_name: Name of the applicant for filename
        language: 'en' for English, 'fr' for French

    Returns:
        PDF file as bytes
    """
    pdf = FPDF()
    pdf.add_page()

    # Add Unicode font for French accents
    pdf.add_font("DejaVu", "", os.path.join(FONTS_DIR, "DejaVuSans.ttf"))
    pdf.add_font("DejaVu", "B", os.path.join(FONTS_DIR, "DejaVuSans-Bold.ttf"))

    pdf.set_font("DejaVu", size=11)

    # Set margins
    pdf.set_left_margin(25)
    pdf.set_right_margin(25)

    # Write content with proper line handling
    pdf.multi_cell(0, 6, text)

    # Return PDF as bytes
    return bytes(pdf.output())
