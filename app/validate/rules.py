from typing import List
from app.validate.schema import ExtractedFields
from datetime import datetime

MANDATORY_FIELDS = [
    "policyNumber",
    "policyholderName",
    "incidentDate",
    "incidentLocation",
    "incidentDescription",
    "claimType",
    "attachments",
    "initialEstimate",
]

def find_missing_fields(f: ExtractedFields) -> List[str]:
    missing = []
    for field in MANDATORY_FIELDS:
        val = getattr(f, field, None)
        if val is None or val == "" or val == [] or val == {}:
            missing.append(field)

    # basic inconsistencies
    if f.estimatedDamage is not None and f.estimatedDamage < 0:
        missing.append("inconsistent: estimatedDamage < 0")

    # date in future check (best effort if parseable)
    if f.incidentDate:
        try:
            d = datetime.strptime(f.incidentDate.strip(), "%m/%d/%Y")
            if d.date() > datetime.today().date():
                missing.append("inconsistent: incidentDate in future")
        except:
            pass

    return missing
