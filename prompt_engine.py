import os
from google import genai
import re
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("GENAI_API_KEY")

def generate_scene_code(prompt: str) -> str:
    """Generate the Manim Python code from the given prompt using Gemini."""

    client = genai.Client(api_key=api_key)  

    system_prompt = load_system_prompt("prompt.txt")

    response = client.models.generate_content(
    model="gemini-2.0-flash",
    contents=system_prompt
    )
    
    raw_code = response.text.strip()
    if raw_code.startswith("```"):
        raw_code = re.sub(r"^```(?:python)?\n?", "", raw_code)
        raw_code = re.sub(r"\n?```$", "", raw_code)

    return raw_code.strip()



def load_system_prompt(path="prompt.txt"):
    """Reads the system prompt from a file."""
    return Path(path).read_text(encoding="utf-8").strip()