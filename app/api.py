from fastapi import FastAPI, UploadFile, File
import tempfile, os, json

from app.extract.pdf_reader import extract_text_from_pdf
from app.extract.parser import parse_fnol
from app.validate.rules import find_missing_fields
from app.route.router import route_claim

app = FastAPI()

@app.post("/process-claim")
async def process_claim(file: UploadFile = File(...)):
    suffix = os.path.splitext(file.filename)[1].lower()
    if suffix not in [".pdf", ".txt"]:
        return {"error": "Only PDF or TXT supported"}

    with tempfile.NamedTemporaryFile(delete=False, suffix=suffix) as tmp:
        tmp.write(await file.read())
        tmp_path = tmp.name

    try:
        if suffix == ".pdf":
            text = extract_text_from_pdf(tmp_path)
        else:
            text = open(tmp_path, "r", encoding="utf-8", errors="ignore").read()

        extracted = parse_fnol(text)
        missing = find_missing_fields(extracted)
        route, reasoning = route_claim(extracted, missing)

        return {
            "extractedFields": extracted.model_dump(),
            "missingFields": missing,
            "recommendedRoute": route,
            "reasoning": reasoning
        }
    finally:
        os.remove(tmp_path)
