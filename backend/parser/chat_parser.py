import re
from collections import defaultdict
from datetime import datetime, timedelta

# Regex patterns
DATE_PATTERN = r"^(\d{1,2}/\d{1,2}/\d{2}),"
MESSAGE_PATTERN = r"- (.*?):"
JOIN_PATTERN = r"- (.*?) joined using this group's invite link"


def parse_chat(chat_text: str):
    """
    Parses WhatsApp chat text and extracts:
    - messages per day
    - joins per day
    - user activity per day
    """

    messages_per_day = defaultdict(set)   # date -> users who messaged
    joins_per_day = defaultdict(set)      # date -> users who joined
    user_active_days = defaultdict(set)   # user -> set of dates

    for line in chat_text.splitlines():

        # Skip empty or system lines
        if not line or "<Media omitted>" in line or "Messages and calls are end-to-end encrypted" in line:
            continue

        date_match = re.search(DATE_PATTERN, line)
        if not date_match:
            continue

        date_str = date_match.group(1)
        date_obj = datetime.strptime(date_str, "%m/%d/%y").date()

        # JOIN EVENT
        join_match = re.search(JOIN_PATTERN, line)
        if join_match:
            user = join_match.group(1).strip()
            joins_per_day[date_obj].add(user)
            continue

        # MESSAGE EVENT
        message_match = re.search(MESSAGE_PATTERN, line)
        if message_match:
            user = message_match.group(1).strip()
            messages_per_day[date_obj].add(user)
            user_active_days[user].add(date_obj)

    return messages_per_day, joins_per_day, user_active_days
