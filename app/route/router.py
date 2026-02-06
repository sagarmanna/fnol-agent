import re
from typing import Tuple, List
from app.validate.schema import ExtractedFields

KEYWORDS_INVESTIGATION = ["fraud", "inconsistent", "staged"]

def route_claim(f: ExtractedFields, missing_fields: List[str]) -> Tuple[str, str]:
    desc = (f.incidentDescription or "").lower()

    # 1) Investigation
    if any(k in desc for k in KEYWORDS_INVESTIGATION):
        return "Investigation Flag", "Description contains investigation keywords (fraud/inconsistent/staged)."

    # 2) Injury
    if (f.claimType or "").lower() == "injury":
        return "Specialist Queue", "Claim type is injury."

    # 3) Missing mandatory
    if len(missing_fields) > 0:
        return "Manual review", f"Missing/invalid mandatory fields: {', '.join(missing_fields)}"

    # 4) Fast track damage < 25000
    if f.estimatedDamage is not None and f.estimatedDamage < 25000:
        return "Fast-track", f"Estimated damage ({f.estimatedDamage}) is below 25,000."

    return "Standard Queue", "Does not meet fast-track / manual review / investigation / injury criteria."
