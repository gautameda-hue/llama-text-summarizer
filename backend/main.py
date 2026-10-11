
from fastapi import FastAPI, Form, HTTPException
import requests

app = FastAPI(title="AI Text Summarizer API")


@app.get("/")
def home():
    return {"message": "Text Summarizer API is running!"}


@app.post("/summarize/")
def summarize(text: str = Form(...)):
    if not text.strip():
        raise HTTPException(
            status_code=400,
            detail="Please enter some text."
        )

    try:
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": "llama3.2",
                "prompt": (
                    "Summarize the following text clearly. "
                    "Keep the most important information:\n\n"
                    + text
                ),
                "stream": False,
            },
            timeout=180,
        )

        response.raise_for_status()
        result = response.json()

        return {"summary": result.get("response", "").strip()}

    except requests.RequestException as exc:
        raise HTTPException(
            status_code=503,
            detail="Could not connect to Ollama. Make sure Ollama is running."
        ) from exc
