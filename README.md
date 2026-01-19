# 📱 WhatsApp Chat Analyzer

A full-stack WhatsApp group chat analytics tool built using **React (ES6)** and **Python (FastAPI)**.

---

## 🚀 Features

- Upload exported WhatsApp group chat (`.txt`)
- Analyze **last 7 days** activity
- Day-wise visualization:
  - 🟦 Active users per day
  - 🟧 New users joined per day
- Identify users active on **≥ 4 days** in the last week
- Clean, colorful, responsive UI
- Efficient single-pass chat parsing

---

## 🧠 Tech Stack

### Frontend
- React (Vite)
- ES6+
- Recharts
- Plain CSS (No frameworks)

### Backend
- Python
- FastAPI
- Regex-based parsing

---

## 📊 Sample Output

- Bar chart showing daily activity
- List of highly active users

---

## ▶️ How to Run

### Backend
```bash
cd backend
python -m venv venv
venv\Scripts\activate   # Windows
pip install -r requirements.txt
uvicorn main:app --reload

## 2️⃣ Better Error Handling (Backend)

Update `/analyze` endpoint in `backend/main.py`:

```python
@app.post("/analyze", response_model=ChatAnalysisResponse)
async def analyze_chat(file: UploadFile = File(...)):
    if not file.filename.endswith(".txt"):
        return {"error": "Only .txt files are supported"}

    try:
        content = await file.read()
        chat_text = content.decode("utf-8")
    except Exception:
        return {"error": "Failed to read file"}

    messages_per_day, joins_per_day, user_active_days = parse_chat(chat_text)

    if not messages_per_day and not joins_per_day:
        return {"error": "No valid chat data found"}

    ...