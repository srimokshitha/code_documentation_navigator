import requests

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL = "llama3"

def generate(prompt):
    response = requests.post(
        OLLAMA_URL,
        json={
            "model": MODEL,
            "prompt": prompt,
            "stream": False
        }
    )

    if response.status_code == 200:
        return response.json()["response"]
    else:
        return "Error connecting to Ollama. Make sure it is running."


def ask_question(codebase, question, mode="Normal"):
    # limit code size for speed
    limited_code = codebase[:3000]

    if mode == "Explain Like I'm 5":
        question = "Explain this in very simple words: " + question
    elif mode == "Technical Deep Dive":
        question = "Give detailed technical explanation: " + question

    prompt = f"""
You are an AI code assistant.

Project code:
{limited_code}

User question:
{question}
"""

    return generate(prompt)


def summarize_project(codebase):
    # limit size for speed
    limited_code = codebase[:3000]

    prompt = f"""
Summarize this project in 5 clear bullet points:

{limited_code}
"""

    return generate(prompt)
