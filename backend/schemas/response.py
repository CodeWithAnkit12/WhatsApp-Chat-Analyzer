from pydantic import BaseModel
from typing import List, Dict


class DayStats(BaseModel):
    date: str
    active_users: int
    new_users: int


class ChatAnalysisResponse(BaseModel):
    last_7_days_stats: List[DayStats]
    active_4_days_users: List[str]
