import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("Gemini API key not found. Make sure .env file contains GEMINI_API_KEY.")
genai.configure(api_key=api_key)

def generate_reply(email_text):
    prompt = f"""
You are an expert personal assistant. Read the following email and write a polite and professional reply:

Email: "{email_text}"

Reply:
"""
    try:
        model = genai.GenerativeModel('models/gemini-1.5-flash')
        response = model.generate_content(prompt)
        reply = response.text.strip()
        return reply
    except Exception as e:
        return f"Error: {e}"

# 🧪 Test the function
if __name__ == "__main__":
    email = input("Paste the email you received:\n")
    print("\n--- AI Generated Reply ---")
    print(generate_reply(email))
