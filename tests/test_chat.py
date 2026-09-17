from fastapi.testclient import TestClient

from app.main import app
import app.services as services

client = TestClient(app)


def test_chat_endpoint_returns_model_response(monkeypatch):
    def fake_chat_with_model(message: str) -> str:
        assert message == "Hi, how are you?"
        return "I'm good, thank you!"

    monkeypatch.setattr("app.main.chat_with_model", fake_chat_with_model)

    response = client.post("/chat", json={"message": "Hi, how are you?"})

    assert response.status_code == 200
    assert response.json() == {"message": "I'm good, thank you!"}


def test_chat_with_model_uses_openai_client(monkeypatch):
    class FakeMessage:
        content = "Model response"

    class FakeChoice:
        message = FakeMessage()

    class FakeCompletion:
        choices = [FakeChoice()]

    def fake_create(**kwargs):
        assert kwargs["model"] == "gpt-4o-mini"
        assert kwargs["messages"] == [{"role": "user", "content": "Test message"}]
        return FakeCompletion()

    monkeypatch.setattr(services.client.chat.completions, "create", fake_create)

    assert services.chat_with_model("Test message") == "Model response"


def test_chat_endpoint_returns_502_when_llm_fails(monkeypatch):
    def fake_chat_with_model(message: str) -> str:
        raise RuntimeError("OpenAI unavailable")

    monkeypatch.setattr("app.main.chat_with_model", fake_chat_with_model)

    response = client.post("/chat", json={"message": "Hello"})

    assert response.status_code == 502
    assert response.json() == {"detail": "Error processing the message with the AI provider."}


def test_chat_rejects_empty_message():
    # We validate input before calling the AI provider.
    # A blank message is not useful for the model and should be rejected.
    response = client.post("/chat", json={"message": ""})

    assert response.status_code == 422


def test_chat_rejects_too_long_message():
    # Large messages increase cost and risk of failures.
    # We keep a practical limit to protect the API and the model.
    long_message = "a" * 1001

    response = client.post("/chat", json={"message": long_message})

    assert response.status_code == 422

def test_chat_summary_returns_summary():
    response = client.post(
        "/chat/summary",
        json={"message": "I need a summary about personal finance."},
    )

    assert response.status_code == 200
    assert "summary" in response.json()