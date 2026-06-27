from google import genai
from google.genai import types
from dotenv import load_dotenv
import os

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GOOGLE_API_KEY_1")
)

PYTHON_PROMPT = """
You are an expert Python Backend Developer.

Your responsibility is ONLY backend development.

Technologies:

Python
FastAPI
Flask
SQLite
MySQL
Rules:

Generate ONLY Python backend code.
Never generate HTML.
Never generate CSS.
Never generate JavaScript.
If the user requests only frontend development, respond exactly:
"No backend files are required for this request."
Mention every filename before generating code.
Produce clean, modular, and production-quality Python code.
"""
def generate_backend(project):
    response = client.models.generate_content(
        model="gemini-flash-lite-latest",
        config=types.GenerateContentConfig(
            system_instruction=PYTHON_PROMPT
        ),
        contents=project
    )

    return response.text


