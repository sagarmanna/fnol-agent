# Autonomous Insurance Claims Processing Agent

## 📌 Overview

This project implements a lightweight rule-based agent for processing First Notice of Loss (FNOL) documents.

The agent:

- Extracts key fields from FNOL documents (TXT/PDF)
- Identifies missing or inconsistent fields
- Classifies and routes claims based on defined rules
- Provides structured JSON output with reasoning

The solution follows the requirements specified in the assignment brief.

---

## 🧠 Features

### 1️⃣ Field Extraction

Extracted Information:

**Policy Information**
- Policy Number
- Policyholder Name
- Effective Dates

**Incident Information**
- Date of Loss
- Time
- Location
- Description

**Asset Details**
- Asset Type
- Asset ID (VIN)
- Estimated Damage
- Initial Estimate

**Other Fields**
- Claim Type
- Attachments
- Contact Details

---

### 2️⃣ Validation

The agent detects:
- Missing mandatory fields
- Invalid values (e.g., missing policy number)
- Incomplete claim submissions

If mandatory fields are missing → claim is routed to **Manual Review**.

---

### 3️⃣ Routing Rules

The routing logic is implemented as follows:

- Estimated Damage < 25,000 → **Fast-track**
- Missing mandatory fields → **Manual Review**
- Description contains keywords ("fraud", "inconsistent", "staged") → **Investigation Flag**
- Claim Type = injury → **Specialist Queue**
- Otherwise → **Standard Queue**



