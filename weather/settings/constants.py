"""Constants used throughout the codebase."""
from datetime import datetime, timedelta
from typing import ClassVar, NewType
from zoneinfo import ZoneInfo

from pytz import timezone
IST_DATETIME = datetime.now(ZoneInfo("Asia/Kolkata"))

IST_TZ = timezone("Asia/Kolkata")
