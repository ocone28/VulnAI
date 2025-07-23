# Funzione per chiamare LLM

from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("API_KEY")


client = Groq(api_key=api_key)

def query_llm(prompt, model="llama-3.3-70b-versatile", temperature=0.3):
    response = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": prompt}],
        temperature=temperature,
    )

    return response.choices[0].message.content
