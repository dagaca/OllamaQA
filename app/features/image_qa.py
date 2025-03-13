"""
This module handles image processing and queries to the LLaVA model.
It converts a numpy image to a base64 JPEG string and sends queries.
"""

import logging
from PIL import Image
import io
import base64
from app.api_client import send_request_image

logger = logging.getLogger("qa_app")

def process_image(image):
    """
    Convert a numpy image to a base64 JPEG string.
    
    Args:
        image: Numpy array image.
    
    Returns:
        str: Base64 encoded JPEG image.
    """
    try:
        img = Image.fromarray(image.astype("uint8"), "RGB")
        buf = io.BytesIO()
        img.save(buf, format="JPEG")
        b64 = base64.b64encode(buf.getvalue()).decode("utf-8")
        logger.info(f"Base64 (first 100): {b64[:100]}")
        logger.info("Image processed to base64 string.")
        return b64
    except Exception as e:
        logger.error("Image processing error: %s", e)
        return ""

def answer_image(image, question):
    """
    Answer a question using image content and the LLaVA model.
    
    Args:
        image: Numpy array image.
        question (str): Question about the image.
    
    Returns:
        str: Model's answer.
    """
    b64 = process_image(image)
    if not b64:
        return "Image processing failed."
    payload = {"prompt": question, "images": [b64]}
    model = "llava"
    logger.info("Sending prompt to llava model.")
    resp = send_request_image(model, payload)
    answer = resp.get("completion", "No answer received.")
    logger.info("Llava model response received.")
    return answer
