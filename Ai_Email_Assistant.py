# Set your Gemini API key
import google.generativeai as genai
genai.configure(api_key='AIzaSyDL6GzVhNhfH-BSM6cumRcmebO6fofvDNI')

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
