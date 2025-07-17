from fastapi import FastAPI, Query, Depends, HTTPException, Header
import ollama
import os
from dotenv import load_dotenv

load_dotenv()

API_KEYS_CREDITS = {os.getenv("API_KEY"): 9}

app = FastAPI()


def verify_api_key(x_api_key: str = Header(None)):
    credits = API_KEYS_CREDITS.get(x_api_key, 0)
    if credits <= 0:
        raise HTTPException(status_code=401, detail="Invalid Api Key , or no credits")

    return x_api_key


@app.post("/generate")
def generate(prompt: str = "", x_api_key: str = Depends(verify_api_key)):
    API_KEYS_CREDITS[x_api_key] -= 1
    response = ollama.chat(
        model="mistral", messages=[{"role": "user", "content": prompt}]
    )
    return {"response": response["message"]["content"]}
