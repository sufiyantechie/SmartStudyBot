import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load .env
load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Use working model
model = genai.GenerativeModel("models/gemini-1.5-flash")

def ask_gpt(question):
    try:
        response = model.generate_content(question)
        return response.text.strip()
    except Exception as e:
        return f"Error: {str(e)}"
 
