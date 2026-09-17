from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

from app.services import chat_with_model

app = FastAPI()


class ChatRequest(BaseModel):
    message: str = Field(..., min_length=1, max_length=1000)


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.post("/chat")
def chat(request: ChatRequest):
    try:
        response = chat_with_model(request.message)
    except Exception:
        raise HTTPException(
            status_code=502,
            detail="Error processing the message with the AI provider.",
        )

    return {"message": response}

@app.post("/chat/summary")
def chat_summary(request: ChatRequest):
    summary = f"Summary: {request.message[:80]}..."
    return {"summary": summary}