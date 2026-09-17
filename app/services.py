from openai import OpenAI

from app.config import OPENAI_API_KEY, OPENAI_MODEL

client = OpenAI(api_key=OPENAI_API_KEY)


def chat_with_model(message: str) -> str:
    response = client.chat.completions.create(
        model=OPENAI_MODEL,
        messages=[{"role": "user", "content": message}],
    )
    content = response.choices[0].message.content
    if content is None:
        raise ValueError("Empty response from the AI provider.")
    return content
