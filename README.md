# Human Validator

A next-gen validator system to detect AI overreliance by analyzing human cognitive signatures: emotional nuance, flawed logic, behavioral timing, and originality.

## 🔧 Features
- Multi-layer cognitive signature analysis
- Time anomaly + revision tracking
- React dashboard to visualize scores and red flags
- FastAPI backend with live scoring

---

## 🔁 Quick Start

### 1. Backend (FastAPI)
```bash
cd backend
pip install -r requirements.txt
uvicorn api_server:app --reload
```

### 2. Frontend (React + Vite)
```bash
cd frontend
npm install
npm run dev
```

Then open [http://localhost:5173](http://localhost:5173).

---

## 📁 File Structure

```
human-validator/
├── backend/
│   ├── api_server.py
│   ├── human_validator.py
│   └── requirements.txt
├── frontend/
│   ├── src/
│   │   ├── App.jsx
│   │   └── main.jsx
│   ├── package.json
│   └── vite.config.js
├── README.md
└── deployment-guide.md
```

---

## 📦 Tech Stack
- **Frontend**: React + Vite + Tailwind UI
- **Backend**: FastAPI + Python 3.11
- **Hosting**: Vercel (frontend), Render (backend)

---

Need help deploying or customizing? Ping Lumina. 🌟

