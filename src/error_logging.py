from google import genai
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("GENAI_API_KEY")

if not api_key:
    raise ValueError("GENAI_API_KEY not found. Please check your .env file.")

def LogError(error: str) -> str:
    client = genai.Client(api_key=api_key)
    system_prompt = f"""
    You are a helpful assistant that helps to log the error in human-readable format.
    The error message is: {error}
    Please provide a  very short  explanation of the error, its possible causes, and how to fix it.
    dont give response in the form of markdown, just give the response in plain text.
    The response should be in the following format:
    1. Error: <error message>
    2. Possible Causes: <list of possible causes>
    3. Solution: <list of possible solutions>
    4. Additional Notes: <any additional notes or information>
    Please make sure to provide a clear and concise explanation.
    """
    
    try:
        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=system_prompt
        )
        return response.text.strip()
    except Exception as e:
        return f"Error during API request: {str(e)}"
