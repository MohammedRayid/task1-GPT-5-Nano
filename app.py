from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
from src.pipeline import process_pdf_pipeline

app = FastAPI(title="GPT-5-Nano + Moderation Pipeline")

@app.post("/process")
async def process_pdf(file: UploadFile = File(...)):
    """
    Accept PDF file upload, process through pipeline, return JSON result.
    """
    if file.content_type != "application/pdf":
        return JSONResponse({"error": "Only PDF files allowed"}, status_code=400)
    
    pdf_bytes = await file.read()
    try:
        result = process_pdf_pipeline(pdf_bytes)
        return JSONResponse(result)
    except Exception as e:
        return JSONResponse({"error": str(e)}, status_code=500)
