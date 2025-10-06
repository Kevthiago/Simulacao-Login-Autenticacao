# groq_chat.py
from groq import Groq
from dotenv import load_dotenv
import os

# Carrega variáveis do .env
load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
os.environ["GROQ_API_KEY"] = GROQ_API_KEY

client = Groq()

def gerar_texto_groq(prompt: str) -> str:
    """
    Envia um prompt para o modelo Groq e retorna a resposta.
    """
    completion = client.chat.completions.create(
        model="openai/gpt-oss-20b",
        messages=[{"role": "user", "content": prompt}],
        temperature=1,
        max_completion_tokens=8192,
        top_p=1,
        reasoning_effort="medium",
        stream=False,
    )
    return completion.choices[0].message.content.strip()
