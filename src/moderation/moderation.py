def moderate_text(text: str) -> dict:
    """
    Mock moderation: Flag if contains forbidden words.
    Returns: {"allowed": bool, "flag": str or None}
    """
    forbidden = ["bad", "harmful", "violence"]  # Stub, extend as needed
    text_lower = text.lower()
    for word in forbidden:
        if word in text_lower:
            return {"allowed": False, "flag": "inappropriate"}
    return {"allowed": True, "flag": None}
