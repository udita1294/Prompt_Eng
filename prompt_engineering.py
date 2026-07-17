import os
from pathlib import Path
from dotenv import load_dotenv
from groq import Groq

load_dotenv()
my_api_key = os.getenv("GROQ_API_KEY")
if not my_api_key:
    raise ValueError("GROQ_API_KEY not found.")

client = Groq(api_key=my_api_key)
model = "llama-3.3-70b-versatile"

def llm_answer(prompt):
    message = {
        "role": "user",
        "content": prompt
    }
    messages = [message]
    response = client.chat.completions.create(model=model, messages=messages)
    ans =  response.choices[0].message.content
    return ans

bad_prompt = """
    This is a user complaint, my laptop is not working.classify this.
"""

print(llm_answer(bad_prompt))