from src.utils.pdf_extractor import extract_text_from_pdf
from src.moderation.moderation import moderate_text
from src.llm.llm import call_gpt_5_nano

def process_pdf_pipeline(pdf_bytes: bytes) -> dict:
    """
    Pipeline: Extract text -> Moderate -> If allowed, LLM -> Return result
    """
    text = extract_text_from_pdf(pdf_bytes)
    mod_result = moderate_text(text)
    if not mod_result["allowed"]:
        return {"allowed": False, "flag": mod_result["flag"]}
    response = call_gpt_5_nano(text)
    return {"allowed": True, "response": response}
