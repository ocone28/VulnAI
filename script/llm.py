# Funzione per chiamare LLM

from groq import Groq
from script.config import GROQ_API_KEY

client = Groq(api_key=GROQ_API_KEY)

def query_llm(prompt, model="llama-3.3-70b-versatile", temperature=0.3):
    response = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": prompt}],
        temperature=temperature,
    )

    return response.choices[0].message.content
