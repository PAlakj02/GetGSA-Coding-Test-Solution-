

```markdown
# 🏛️ GetGSA Coding Test Solution  

This project implements a service that ingests **Company Profile** and **Past Performance** text, parses them into structured JSON, validates fields, maps **NAICS → SIN codes**, and produces a compliance checklist.  

It exposes a **Flask API** (`/ingest`) and includes a simple **one-page web UI** to test the functionality.  

---

## 📂 Project Structure  

```

infotech/
│── run.py                # Entry point to start the server
│── requirements.txt       # Python dependencies
│── README.md              # Project documentation
│── app/
│   │── **init**.py        # App factory
│   │── api.py             # API routes (Blueprint)
│   │── parser.py          # Text parsing logic
│   │── validator.py       # Validation logic
│   │── mapper.py          # NAICS → SIN mapper
│   │── models.py          # Data models
│── static/
│   │── index.html         # Web UI
│── tests/
│── test\_api.py        # API unit tests
│── test\_parser.py     # Parser unit tests
│── test\_validator.py  # Validator unit tests

````

---

## 🚀 Getting Started  

### 1. Clone Repository  
```bash
git clone <your-repo-url>
cd infotech
````

### 2. Create Virtual Environment

```bash
python -m venv .venv
.\.venv\Scripts\activate      # Windows PowerShell
# or
source .venv/bin/activate     # Linux/Mac
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Server

```bash
python run.py
```

Server will start at:
👉 [http://127.0.0.1:5000/](http://127.0.0.1:5000/)

---

## 🌐 API Usage

### Endpoint: `POST /ingest`

**Request Body (JSON):**

```json
{
  "company_profile": "Acme Robotics LLC\nUEI: ABC123DEF456\nDUNS: 123456789\nNAICS: 541511, 541512\nPOC: Jane Smith, jane@acme.co, (415) 555-0100\nAddress: 444 West Lake Street, Suite 1700, Chicago, IL 60606\nSAM.gov: registered",
  "past_performance": "Customer: City of Palo Verde\nContract: Website modernization\nValue: $180,000\nPeriod: 07/2023 - 03/2024\nContact: John Roe, cio@pverde.gov"
}
```

**Response (JSON):**

```json
{
  "request_id": "a1a527c1-a9c7-408a-afbe-a98de4c8e0e3",
  "parsed": {
    "company_name": "Acme Robotics LLC",
    "uei": "ABC123DEF456",
    "duns": "123456789",
    "naics": ["541511", "541512"],
    "poc_name": "Jane Smith",
    "poc_email": "jane@acme.co",
    "poc_phone": "(415) 555-0100",
    "address": "444 West Lake Street, Suite 1700, Chicago, IL 60606",
    "sam_registered": true,
    "past_performance": {
      "customer": "City of Palo Verde",
      "contract": "Website modernization",
      "value": "$180,000",
      "period": "07/2023 - 03/2024",
      "contact": "John Roe, cio@pverde.gov"
    }
  },
  "issues": [],
  "recommended_sins": ["54151S"],
  "checklist": {
    "has_uei": true,
    "has_valid_email": true,
    "has_naics": true,
    "has_past_performance": true,
    "has_duns": true,
    "sam_registered": true,
    "required_ok": true
  }
}
```

---

## 🖥️ Web UI

Open in browser:
👉 [http://127.0.0.1:5000/](http://127.0.0.1:5000/)

* Paste **Company Profile** and **Past Performance** into the textareas.
* Click **🚀 Process Data**.
* Parsed JSON will display below.

---

## 🧪 Running Tests

Tests are written with **pytest**. Run:

```bash
pytest -v
```

Covers:

* Missing UEI detection
* Invalid email detection
* NAICS → SIN mapping

---

## 📝 Notes

* By default, the server runs on `http://127.0.0.1:5000`.
* To allow external connections, change in `run.py`:

  ```python
  app.run(host="0.0.0.0", port=5000, debug=True)
  ```
* This is a **development server**. For production, use Gunicorn or another WSGI server.

---

## ✅ Features Checklist

* API with `/ingest`
* Parsing of company & past performance text
* Field validation (UEI, email, DUNS, NAICS)
* NAICS → SIN mapping (deduplicated)
* Compliance checklist
* Request logging (audit trail)
* Unit tests (pytest)
* Simple UI (bonus)


```
