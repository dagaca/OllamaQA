"""
This module launches the Gradio interface for PDF and image queries.
It sets up logging and creates two tabs: PDF Q&A and Image Q&A.
"""

import gradio as gr
from app.features.pdf_qa import answer_pdf
from app.features.image_qa import answer_image
from config.log_config import setup_logging

logger = setup_logging()
logger.info("Application started.")

def build_pdf_interface():
    """
    Build the Gradio interface for PDF queries.

    Returns:
        gr.Interface: The PDF Q&A interface.
    """
    pdf_int = gr.Interface(
        fn=answer_pdf,
        inputs=[
            gr.File(label="Upload PDF"),
            gr.Textbox(
                label="Question",
                placeholder="Enter PDF question..."
            )
        ],
        outputs=gr.Textbox(label="Answer"),
        title="PDF Q&A"
    )
    return pdf_int

def build_image_interface():
    """
    Build the Gradio interface for image queries.

    Returns:
        gr.Interface: The Image Q&A interface.
    """
    img_int = gr.Interface(
        fn=answer_image,
        inputs=[
            gr.Image(type="numpy", label="Upload Image"),
            gr.Textbox(
                label="Question",
                placeholder="Enter image question..."
            )
        ],
        outputs=gr.Textbox(label="Answer"),
        title="Image Q&A"
    )
    return img_int

def build_tabbed_interface(pdf_int, img_int):
    """
    Build the tabbed Gradio interface.

    Args:
        pdf_int (gr.Interface): PDF Q&A interface.
        img_int (gr.Interface): Image Q&A interface.

    Returns:
        gr.TabbedInterface: The tabbed interface.
    """
    tabs = gr.TabbedInterface(
        [pdf_int, img_int],
        ["PDF Q&A", "Image Q&A"]
    )
    return tabs

def main():
    """
    Main function to launch the Gradio demo.
    """
    pdf_int = build_pdf_interface()
    img_int = build_image_interface()
    demo = build_tabbed_interface(pdf_int, img_int)
    demo.launch()

if __name__ == "__main__":
    main()
