from fastapi import FastAPI, HTTPException
import requests
from pydantic import BaseModel
import os
from dotenv import load_dotenv

# Load .env from Google Drive
env_path = "/content/drive/My Drive/Colab Notebooks/Fine Tuning LLMs/Exercise 2/.env"
load_dotenv(env_path)

# Get API Key
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# Debugging step (optional, check if API key is loaded)
print("API Key Loaded:", GROQ_API_KEY is not None)

# FastAPI app instance
app = FastAPI()

# Request model
class TranslationRequest(BaseModel):
    text: str
    target_language: str

# Groq API URL
GROQ_API_URL = "https://api.groq.com/openai/v1/chat/completions"


@app.post("/translate/")
def translate_text(request: TranslationRequest):
    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "model": "llama-3.3-70b-versatile",  # Update if needed
        "messages": [
            {"role": "user",
             "content": f"Translate this to {request.target_language}: {request.text}"}
        ]
    }

    response = requests.post(GROQ_API_URL, headers=headers, json=data)

    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code,
                            detail=response.json())

    # Extract only the translated text
    translated_text = response.json()["choices"][0]["message"]["content"]

    return {"translated_text": translated_text}
