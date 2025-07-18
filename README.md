# Ollama LLM API

This is a FastAPI-based backend project that integrates with the Ollama LLM (e.g., Mistral, Llama3) for generating AI-powered responses via HTTP endpoints.

## 🔧 Features

- FastAPI server
- `/generate` endpoint for prompt-based chat
- Integration with Ollama models (e.g., mistral)
- Easily customizable for any local or remote LLM

## 🚀 Running the Project

1. **Create a virtual environment**:

```bash
python -m venv venv
source venv/bin/activate  # For Windows: venv\Scripts\activate
```

2. **Install dependencies**:
   pip install fastapi uvicorn ollama

3. **Run the API server**:
   uvicorn main:app --reload

4. **Send a POST request**:
   curl -X POST "http://localhost:8000/generate?prompt=Hello"
