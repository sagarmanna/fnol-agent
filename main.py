import json
import argparse
from pathlib import Path

from app.extract.parser import parse_fnol
from app.validate.rules import find_missing_fields
from app.route.router import route_claim


def read_input_file(path: Path) -> str:
    if path.suffix.lower() == ".pdf":
        from app.extract.pdf_reader import extract_text_from_pdf
        return extract_text_from_pdf(str(path))
    elif path.suffix.lower() == ".txt":
        return path.read_text(encoding="utf-8")
    else:
        raise ValueError("Only PDF and TXT files are supported")


def process_file(file_path: str) -> dict:
    path = Path(file_path)

    if not path.exists():
        raise FileNotFoundError(f"File not found: {path}")

    text = read_input_file(path)

    extracted = parse_fnol(text)
    missing = find_missing_fields(extracted)
    route, reasoning = route_claim(extracted, missing)

    return {
        "extractedFields": extracted.model_dump(),
        "missingFields": missing,
        "recommendedRoute": route,
        "reasoning": reasoning
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--file", required=True)
    args = parser.parse_args()

    result = process_file(args.file)
    print(json.dumps(result, indent=2))
