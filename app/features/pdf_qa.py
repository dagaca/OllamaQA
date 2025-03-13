"""
This module handles PDF text extraction and querying using
the deepseek model. It provides functions to extract text
from a PDF and to answer questions based on its content.
"""

import logging
from PyPDF2 import PdfReader
from app.api_client import send_request_pdf

logger = logging.getLogger("qa_app")

def extract_text_from_pdf(pdf_file):
    """
    Extract text from a PDF file.
    
    Args:
        pdf_file: Uploaded PDF file.
    
    Returns:
        str: Extracted text.
    """
    try:
        reader = PdfReader(pdf_file.name)
        text = ""
        for page in reader.pages:
            extracted = page.extract_text()
            if extracted:
                text += extracted + "\n"
        logger.info("PDF text extraction succeeded.")
        return text
    except Exception as e:
        logger.error("PDF extraction error: %s", e)
        return ""

def answer_pdf(pdf_file, question):
    """
    Answer a question using PDF content and the deepseek model.
    
    Args:
        pdf_file: Uploaded PDF file.
        question (str): Question about the PDF.
    
    Returns:
        str: Model's answer.
    """
    try:
        text = extract_text_from_pdf(pdf_file)
        if not text:
            return "PDF text extraction failed."
        prompt = ("PDF content:\n" + text + "\n\nQuestion: " +
                  question + "\nAnswer:")
        payload = {"prompt": prompt}
        model = "deepseek-r1:1.5b"
        logger.info("Sending prompt to deepseek model.")
        response = send_request_pdf(model, payload)
        answer = response.get("completion", "No answer received.")
        logger.info("Deepseek model response received.")
        return answer
    except Exception as e:
        logger.error("Error in answer_pdf: %s", e)
        return f"Error occurred: {e}"
