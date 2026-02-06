# Autonomous Insurance Claims Processing Agent

📌 Problem Statement

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

---

## 📂 Project Structure

app/
extract/
validate/
route/
samples/
main.py
requirements.txt


---

## ⚙️ Steps to Run

### 1. Clone Repository

git clone https://github.com/sagarmanna/fnol-agent.git
cd fnol-agent


### 2. Create Virtual Environment

Windows:
python -m venv .venv
..venv\Scripts\activate


Mac/Linux:
python3 -m venv .venv
source .venv/bin/activate


### 3. Install Dependencies

pip install -r requirements.txt


### 4. Run the Agent

Example:

python main.py --file .\samples\fnol_fasttrack.txt


Other test cases:

python main.py --file .\samples\fnol_injury.txt
python main.py --file .\samples\fnol_investigation.txt
python main.py --file .\samples\fnol_missing.txt


---

## 🧾 Sample Output

```json
{
  "extractedFields": {...},
  "missingFields": [],
  "recommendedRoute": "Fast-track",
  "reasoning": "Estimated damage (12000.0) is below 25,000."
}
