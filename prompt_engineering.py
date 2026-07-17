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

good_prompt = """
    #ROLE:
    You are a customer support assistant at laptop/mobile device company.
    #TASK:
    Classify the following user complaint into one of the categories.
    #CONSTRAINTS:
    You have to classify issue in one of the categories Billing,technical,return or other.
    #OUTPUT FORMAT:
    The output should be a single word, one of the categories mentioned above.
    #EXAMPLE:
    For instance the user need refund for the laptop, the output should be "return".
    #FALLBACK:
    If the complaint does not fit into any of the categories, output "other".

    I am not happy with the laptop, I dont like it, I want refund.
"""

print(llm_answer(good_prompt))