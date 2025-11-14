# GPT-5-Nano + Moderation Pipeline

Minimal runnable service implementing a pipeline to process PDFs: extract text → moderate for inappropriate content → if allowed, generate response via GPT-5-Nano (stub).

## Approach

- **Modular Structure**: Code separated into `/src/moderation`, `/src/llm`, `/src/utils` for maintainability.
- **Stubs**: Moderation checks for forbidden words; LLM returns a mock response.
- **Robustness**: Retry mechanism (1 retry with 1s delay) for LLM calls.
- **Service**: FastAPI-based HTTP service accepting PDF uploads via POST `/process`.

## Setup

1. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

2. (Optional for production testing) Set OpenAI API key:
   ```
   export OPENAI_API_KEY=your_api_key_here
   ```

3. Run the service:
   ```
   uvicorn app:app --reload
   ```

   Service will be available at `http://localhost:8000`.

## Demo

Upload `prompt.pdf` (containing "What color is the sky?") to `/process`:

### Example Request
```bash
curl -X POST "http://localhost:8000/process" \
  -H "accept: application/json" \
  -H "Content-Type: multipart/form-data" \
  -F "file=@prompt.pdf"
```

### Example Response
```json
{
  "allowed": true,
  "response": "The sky is blue."
}
```

If PDF contains flagged words (e.g., "bad"), returns:
```json
{
  "allowed": false,
  "flag": "inappropriate"
}
```

## Tech Stack

- Python 3.x
- FastAPI (web framework)
- PyPDF2 (PDF text extraction)
- Uvicorn (ASGI server)
