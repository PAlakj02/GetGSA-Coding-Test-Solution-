# 🏛️ GetGSA Coding Test Solution  

This project provides a service to ingest **Company Profile** and **Past Performance** text, convert it into structured JSON, validate key fields, map **NAICS → SIN codes**, and generate a compliance checklist.  

It includes:  
- A **Flask API** (`/ingest`)  
- A lightweight **Web UI** for quick testing  
- Unit tests for validation, parsing, and mapping  

---

## 📂 Project Structure  

```
infotech/
│── run.py                # Application entry point
│── requirements.txt       # Python dependencies
│── README.md              # Documentation
│
│── app/
│   │── __init__.py        # App factory
│   │── api.py             # API routes (Blueprint)
│   │── parser.py          # Text parsing logic
│   │── validator.py       # Validation rules
│   │── mapper.py          # NAICS → SIN mapper
│   │── models.py          # Data models
│
│── static/
│   │── index.html         # Web UI
│
│── tests/
│   │── test_api.py        # API tests
│   │── test_parser.py     # Parser tests
│   │── test_validator.py  # Validator tests
```

---

## 🚀 Quick Start  

```bash
git clone <your-repo-url>
cd infotech
python -m venv .venv
source .venv/bin/activate   # or .\.venv\Scripts\activate on Windows
pip install -r requirements.txt
python run.py
```

Server will start at:  
👉 [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## 🌐 API Usage  

### Endpoint: `POST /ingest`  

#### Example Request  
```json
{
  "company_profile": "Acme Robotics LLC\nUEI: ABC123DEF456\nDUNS: 123456789\nNAICS: 541511, 541512\nPOC: Jane Smith, jane@acme.co, (415) 555-0100\nAddress: 444 West Lake Street, Suite 1700, Chicago, IL 60606\nSAM.gov: registered",
  "past_performance": "Customer: City of Palo Verde\nContract: Website modernization\nValue: $180,000\nPeriod: 07/2023 - 03/2024\nContact: John Roe, cio@pverde.gov"
}
```

#### Example Response  
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

Open in your browser:  
👉 [http://127.0.0.1:5000](http://127.0.0.1:5000)  

Features:  
- Paste **Company Profile** and **Past Performance** text  
- Click **🚀 Process Data**  
- View parsed JSON results instantly  

---

## 🧪 Running Tests  

Run unit tests with:  
```bash
pytest -v
```

Coverage includes:  
- Missing UEI detection  
- Invalid email validation  
- NAICS → SIN mapping  

---

## 📝 Notes  

- Default server host: `http://127.0.0.1:5000`  
- To allow external access, update `run.py`:  
  ```python
  app.run(host="0.0.0.0", port=5000, debug=True)
  ```
- This is a **development server**. For production, deploy with **Gunicorn** or another WSGI server.  

---

## ✅ Features  

- REST API with `/ingest`  
- Parsing of company & past performance text  
- Field validation (UEI, Email, DUNS, NAICS)  
- NAICS → SIN mapping  
- Compliance checklist generation  
- Request logging (audit trail)  
- Unit tests with pytest  
- Simple web interface  
