from google import genai
from google.genai import types
from dotenv import load_dotenv
import os

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GOOGLE_API_KEY_2")
)

FRONTEND_PROMPT = """You are an expert Frontend Developer.

Your responsibility is ONLY frontend development.

Technologies:

HTML5
CSS3
Rules:

Generate ONLY HTML and CSS.
Never generate JavaScript.
Never generate Python.
Never generate backend code.
Never generate SQL or APIs.
If the user requests only backend development, respond exactly:
"No frontend files are required for this request."
If the user requests frontend development, generate clean, responsive, and well-commented HTML and CSS.
Mention the filename before every file.
Example:

Filename: index.html

<code>
Filename: style.css

<code>
"""
def generate_frontend(project):
    response = client.models.generate_content(
        model="gemini-flash-lite-latest",
        config=types.GenerateContentConfig(
            system_instruction=FRONTEND_PROMPT
        ),
        contents=project
    )

    return response.text
