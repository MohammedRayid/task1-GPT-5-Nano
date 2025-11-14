import os
from openai import OpenAI
from src.utils.retry import retry_with_delay

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

@retry_with_delay  # Retry with delay (1 retry, 1s delay)
def call_gpt_5_nano(text: str) -> str:
    """
    Production-ready OpenAI integration.
    """
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "user", "content": text}]
    )
    return response.choices[0].message.content
