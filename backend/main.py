from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from datetime import date

from parser.chat_parser import parse_chat
from utils.date_utils import get_last_7_days
from schemas.response import ChatAnalysisResponse, DayStats

app = FastAPI(title="WhatsApp Chat Analyzer")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def health_check():
    return {"status": "Backend running successfully 🚀"}


@app.post("/analyze", response_model=ChatAnalysisResponse)
async def analyze_chat(file: UploadFile = File(...)):
    content = await file.read()
    chat_text = content.decode("utf-8")

    messages_per_day, joins_per_day, user_active_days = parse_chat(chat_text)

    today = max(
        list(messages_per_day.keys()) + list(joins_per_day.keys())
    )

    last_7_days = get_last_7_days(today)

    stats = []
    for day in last_7_days:
        stats.append(
            DayStats(
                date=day.strftime("%Y-%m-%d"),
                active_users=len(messages_per_day.get(day, [])),
                new_users=len(joins_per_day.get(day, [])),
            )
        )

    active_4_days_users = [
        user
        for user, days in user_active_days.items()
        if len(set(last_7_days).intersection(days)) >= 4
    ]

    return ChatAnalysisResponse(
        last_7_days_stats=stats,
        active_4_days_users=active_4_days_users
    )
