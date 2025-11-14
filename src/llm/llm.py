from src.utils.retry import retry_with_delay

@retry_with_delay  # Retry with delay (1 retry, 1s delay)
def call_gpt_5_nano(text: str) -> str:
    """
    Stub for GPT-5-Nano: Always return a fixed response.
    In production, this would call OpenAI or similar.
    """
    # Simulate potential failure for testing retry, but remove for minimal
    # raise Exception("Mock failure")
    return "The sky is blue."  # Mock response based on sample
