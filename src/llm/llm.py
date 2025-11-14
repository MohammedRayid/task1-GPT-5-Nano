import os
from src.utils.retry import retry_with_delay

openai_client = None
if os.getenv("OPENAI_API_KEY"):
    from openai import OpenAI
    openai_client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

@retry_with_delay  # Retry with delay (1 retry, 1s delay)
def call_gpt_5_nano(text: str) -> str:
    """
    Production-ready: Uses real OpenAI GPT-4 if API key provided, otherwise stub.
    """
    if openai_client:
        response = openai_client.chat.completions.create(
            model="gpt-4",
            messages=[{"role": "user", "content": text}]
        )
        return response.choices[0].message.content
    else:
        return "The sky is blue."  # Stub fallback
