from fastapi import FastAPI
from pydantic import BaseModel

from app.services import chat_with_model

app = FastAPI()


class ChatRequest(BaseModel):
    message: str


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.post("/chat")
def chat(request: ChatRequest):
    response = chat_with_model(request.message)
    return {"message": response}