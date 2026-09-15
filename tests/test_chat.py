from fastapi.testclient import TestClient

from app.main import app
import app.services as services

client = TestClient(app)


def test_chat_endpoint_returns_model_response(monkeypatch):
    def fake_chat_with_model(message: str) -> str:
        assert message == "Olá, como você está?"
        return "Estou bem, obrigado!"

    monkeypatch.setattr("app.main.chat_with_model", fake_chat_with_model)

    response = client.post("/chat", json={"message": "Olá, como você está?"})

    assert response.status_code == 200
    assert response.json() == {"message": "Estou bem, obrigado!"}


def test_chat_with_model_uses_openai_client(monkeypatch):
    class FakeMessage:
        content = "Resposta do modelo"

    class FakeChoice:
        message = FakeMessage()

    class FakeCompletion:
        choices = [FakeChoice()]

    def fake_create(**kwargs):
        assert kwargs["model"] == "gpt-4o-mini"
        assert kwargs["messages"] == [{"role": "user", "content": "Teste de mensagem"}]
        return FakeCompletion()

    monkeypatch.setattr(services.client.chat.completions, "create", fake_create)

    assert services.chat_with_model("Teste de mensagem") == "Resposta do modelo"
