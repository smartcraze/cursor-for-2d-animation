import os
from google import genai
import re
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("GENAI_API_KEY")

def generate_scene_code(prompt: str) -> str:
    """Generate the Manim Python code from the given prompt using Gemini."""
    try:
        client = genai.Client(api_key=api_key)

        system_prompt = f"""
        You are an expert Python animator working with Manim CE v0.19 or newer.
        Your task is to generate **clean, valid Manim scene code** based on the user's animation idea.

        🎯 The user's animation idea:
        {prompt}

        📌 Code Requirements:
        - Generate **a single Python class** that inherits from `Scene`. Name the class meaningfully.
        - Output **only valid Python code** – no markdown, no comments, and no explanations.
        - Import **all required modules** explicitly (e.g., `from manim import *`, `import numpy as np`, `import math`, etc.). Do not use `from manim import *` alone.
        - If using `Text`, use the parameter `font_size` instead of `scale`.
        - If scaling is needed, use the `.scale()` method **after** an object is created.
        - For dynamic animations, use `ValueTracker` and `always_redraw` where appropriate.
        - For graphs, use `Axes` with `ax.plot(...)` and `ax.get_axis_labels(...)`.
        - Avoid using `Tex` or `MathTex` unless LaTeX is supported – prefer `Text`.
        - The output must be a **self-contained, executable Manim script**.
        - Ensure the code is **ready to copy into a `.py` file** and can be run immediately with:
          `manim -pql script_name.py ClassName`
        
        🧠 Think like an engineer. The code must be clean, precise, and immediately executable.
        """
        
        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=system_prompt
        )
        
        raw_code = response.text.strip()

        if raw_code.startswith("```"):
            raw_code = re.sub(r"^```(?:python)?\n?", "", raw_code)
            raw_code = re.sub(r"\n?```$", "", raw_code)

        return raw_code.strip()

    except Exception as e:
        return f"Error generating scene code: {str(e)}"
