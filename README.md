# OllamaQA

OllamaQA is an interactive Gradio application designed to perform question-answering tasks using local AI models (Ollama) based on PDF documents and images. The application extracts text from PDFs and analyzes image content to answer user queries.

## 🎥 Demo Video and Animated Usage Examples

To effectively demonstrate the project's use cases and capabilities, a detailed demo video along with animated examples has been prepared. This video plays a crucial role in visually illustrating the practical application of the system and clearly showcases the real-time, accurate responses provided by artificial intelligence.

### 📑 PDF Question-Answering Module:
This module illustrates how users can upload PDF documents and receive clear and precise answers to their content-related questions from the AI.

**Example Scenarios:**
- A user uploads a CV document and queries about the individual's educational background; the AI model returns a concise, accurate summary.
- A user inquires about the job title of the document owner, and the AI quickly provides the correct title.
- A user requests a comma-separated list of skills from the CV, and the model accurately delivers these skills as requested.

### 🖼 Image Question-Answering Module:
In this module, users upload images and ask questions related to the visual content. The AI's ability to accurately interpret and describe image details is clearly demonstrated.

**Example Scenarios:**
- A user uploads an image of an indoor parking garage and asks about the scene; the AI provides a clear description of the environment and objects.
- A user uploads a nature landscape photo and requests details about the scene; the AI model accurately describes the setting in detail.
- A user uploads an image of a car and asks for identification; the AI quickly identifies and describes the car.

This video effectively showcases the application's real-time performance and highlights the quality of AI-driven interactions. You can watch the demo video here: 


https://github.com/user-attachments/assets/429aa37b-9315-4c38-aac9-73cdcd7dca55



## 🚀 Key Features

- **PDF Question-Answer Module**
  - Extract text from PDF files using PyPDF2.
  - Answer questions with the local Deepseek model.

- **Image Question-Answer Module**
  - Convert uploaded images to base64 format using Pillow.
  - Analyze images and answer questions using the local LLaVA model.

- **Local Model Usage and Data Privacy**
  - Models and operations run locally via Ollama.
  - Ensures data privacy with no external data transfer.

- **Advanced Logging and Configuration**
  - Comprehensive logging with RotatingFileHandler.
  - Configuration flexibility via environment variables (.env).

## 🛠️ Technologies Used

- **Python 3.8+**
- **Ollama** (Deepseek-r1:1.5b, LLaVA)
- **Gradio** (Interactive UI)
- **PyPDF2** (PDF text extraction)
- **Pillow (PIL)** (Image processing)
- **Requests** (API requests)
- **python-dotenv** (Environment variable management)

## 📂 Project Structure

```
OllamaQA/
├── app/
│   ├── api_client.py            # API calls (PDF and image)
│   └── features/
│       ├── pdf_qa.py            # PDF Q&A functions
│       └── image_qa.py          # Image Q&A functions
├── config/
│   └── log_config.py            # Logging configuration
├── logs/                        # Log files
├── .env                         # Environment variables
├── main.py                      # Gradio app launcher
└── requirements.txt             # Dependencies
```

## ⚙️ Installation

```bash
# Clone repository
git clone https://github.com/dagaca/OllamaQA.git
cd OllamaQA

# Create virtual environment
python -m venv venv

# Activate virtual environment
# Windows
venv\Scripts\activate

# Linux/Mac
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

## ▶️ Launching the Application

```bash
python main.py
# Application will be available at http://localhost:7860 by default.
```

## 🖥️ Usage

- **PDF Q&A:** Upload PDF documents and ask questions related to their content.
- **Image Q&A:** Upload images and ask questions about the image content.

---

## 📄 License

This project is licensed under the MIT License.
