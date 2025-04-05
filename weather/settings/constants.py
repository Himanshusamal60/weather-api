"""Constants used throughout the codebase."""
from datetime import datetime
from zoneinfo import ZoneInfo

IST_DATETIME = datetime.now(ZoneInfo("Asia/Kolkata"))

SUCCESS_STATUS_CODE = 200
REQUEST_TIMEOUT = 10
