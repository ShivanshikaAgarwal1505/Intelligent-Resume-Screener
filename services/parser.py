from pypdf import PdfReader

def extract_text(pdf_path):
    """
    Extract text from a PDF file.
    Returns empty string if extraction fails.
    """
    try:
        reader = PdfReader(pdf_path)
        text = ""
        for page in reader.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"
        return text.strip()
    except Exception as e:
        print(f"[PDF Parsing Error] {e}")
        return ""