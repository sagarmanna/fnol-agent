# Autonomous Insurance Claims Processing Agent

## 📌 Problem Statement

Build a lightweight agent that:

- Extracts key fields from FNOL (First Notice of Loss) documents
- Identifies missing or inconsistent fields
- Classifies and routes claims
- Provides reasoning for routing decisions

---

## 🧠 Approach

The solution is designed using a modular architecture:

### 1️⃣ Extraction Layer
- TXT/PDF input handling
- Regex-based field extraction
- Structured data mapping using Pydantic models

### 2️⃣ Validation Layer
- Mandatory field checks
- Missing field detection
- Data normalization

### 3️⃣ Routing Engine
Rule-based routing logic:

- Damage < 25,000 → Fast-track
- Missing mandatory fields → Manual Review
- Description contains fraud keywords → Investigation Flag
- Claim type = injury → Specialist Queue
- Otherwise → Standard Queue

Each decision includes clear reasoning.

