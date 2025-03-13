"""
This module provides functions to send requests to local Ollama models.
It supports PDF and image queries. PDF queries use ollama.chat, while
image queries are sent via an HTTP POST to the local API.
"""

import ollama
import requests
import logging
import re
import json

logger = logging.getLogger("qa_app")

def send_request_pdf(model, payload):
    """
    Send a request to a local Ollama model for PDF queries.

    Args:
        model (str): The model name.
        payload (dict): Must contain a "prompt" key.

    Returns:
        dict: A dict with key "completion".
    """
    try:
        msg = {"role": "user", "content": payload["prompt"]}
        resp = ollama.chat(model=model, messages=[msg])
        cont = resp["message"]["content"]
        cont = re.sub(r'<think>.*?</think>', '', cont, flags=re.DOTALL)
        return {"completion": cont.strip()}
    except Exception as e:
        logger.error("Error running model %s: %s", model, e)
        return {"completion": f"Error occurred: {e}"}

def send_request_image(model, payload):
    """
    Send a request to the local Ollama API for image queries.

    Args:
        model (str): The model name.
        payload (dict): Contains "prompt" and "images" (list of base64 strings).

    Returns:
        dict: A dict with key "completion".
    """
    url = "http://localhost:11434/api/generate"
    data = {
        "model": model,
        "prompt": payload["prompt"],
        "images": payload.get("images", [])
    }
    headers = {"Content-Type": "application/json"}
    try:
        resp = requests.post(url, json=data, headers=headers)
        resp.raise_for_status()
        res_text = resp.text
        logger.info("Full response text: %s", res_text)
        parts = []
        for line in res_text.splitlines():
            line = line.strip()
            if line:
                try:
                    obj = json.loads(line)
                    parts.append(obj.get("response", ""))
                except Exception as e:
                    logger.error("Error parsing JSON line: %s", e)
        content = "".join(parts)
        return {"completion": content.strip()}
    except Exception as e:
        logger.error("Error in API request: %s", e)
        if resp is not None:
            logger.error("Response text: %s", resp.text)
        return {"completion": f"Error occurred: {e}"}
