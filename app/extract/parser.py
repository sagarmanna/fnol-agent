import re
from app.validate.schema import ExtractedFields


def _find_after_label(text: str, label: str) -> str | None:
    pattern = rf"{re.escape(label)}\s*:\s*(.+)"
    m = re.search(pattern, text, re.IGNORECASE)
    if m:
        return m.group(1).strip()
    return None


def parse_fnol(text: str) -> ExtractedFields:
    f = ExtractedFields()

    # POLICY INFO
    f.policyNumber = _find_after_label(text, "POLICY NUMBER")
    f.policyholderName = _find_after_label(text, "NAME OF INSURED")
    f.effectiveDates = _find_after_label(text, "EFFECTIVE DATES")

    # INCIDENT INFO
    f.incidentDate = _find_after_label(text, "DATE OF LOSS")
    f.incidentTime = _find_after_label(text, "TIME")

    street = _find_after_label(text, "STREET")
    city = _find_after_label(text, "CITY, STATE, ZIP")
    if street or city:
        f.incidentLocation = ", ".join([x for x in [street, city] if x])

    # DESCRIPTION
    f.incidentDescription = _find_after_label(text, "DESCRIPTION OF ACCIDENT")

    # CONTACT DETAILS
    phone = _find_after_label(text, "PRIMARY PHONE")
    email = _find_after_label(text, "PRIMARY E-MAIL ADDRESS")

    if phone:
        f.contactDetails["phone"] = phone
    if email:
        f.contactDetails["email"] = email.strip()

    # VEHICLE INFO
    vin = _find_after_label(text, "VIN")
    if vin:
        f.assetId = vin
        f.assetType = "vehicle"

    # ESTIMATE
    dmg = _find_after_label(text, "ESTIMATE AMOUNT")
    if dmg:
        num = re.sub(r"[^\d.]", "", dmg)
        if num:
            f.estimatedDamage = float(num)
            f.initialEstimate = float(num)

    # ATTACHMENTS
    if re.search(r"attachment|attached|photos|documents", text, re.IGNORECASE):
        f.attachments = "mentioned"

    # CLAIM TYPE
    explicit_claim_type = _find_after_label(text, "CLAIM TYPE")

    if explicit_claim_type:
        if "injury" in explicit_claim_type.lower():
            f.claimType = "injury"
        else:
            f.claimType = "vehicle/property"
    else:
        if re.search(r"\binjur", text, re.IGNORECASE):
            f.claimType = "injury"
        else:
            f.claimType = "vehicle/property"

    return f
