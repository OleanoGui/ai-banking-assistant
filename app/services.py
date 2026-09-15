from openai import OpenAI

from app.config import OPENAI_API_KEY, OPENAI_MODEL

client = OpenAI(api_key=OPENAI_API_KEY)


def chat_with_model(message: str) -> str:
    response = client.chat.completions.create(
        model=OPENAI_MODEL,
        messages=[{"role": "user", "content": message}],
    )
    return response.choices[0].message.content
