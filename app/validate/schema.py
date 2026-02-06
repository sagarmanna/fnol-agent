from pydantic import BaseModel
from typing import Optional, List, Dict, Any

class ExtractedFields(BaseModel):
    policyNumber: Optional[str] = None
    policyholderName: Optional[str] = None
    effectiveDates: Optional[str] = None

    incidentDate: Optional[str] = None
    incidentTime: Optional[str] = None
    incidentLocation: Optional[str] = None
    incidentDescription: Optional[str] = None

    claimant: Optional[str] = None
    thirdParties: List[str] = []
    contactDetails: Dict[str, Any] = {}

    assetType: Optional[str] = None
    assetId: Optional[str] = None
    estimatedDamage: Optional[float] = None

    claimType: Optional[str] = None
    attachments: Optional[str] = None
    initialEstimate: Optional[float] = None
