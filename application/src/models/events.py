from dataclasses import dataclass
from datetime import datetime
from typing import Optional
from zoneinfo import ZoneInfo


@dataclass
class Event:
    name: str
    start_timestamp: str
    end_timestamp: str
    all_day: bool
    url: str
    description: str
    address: str
    city_id: int
    archived: bool
    # time_zone: Optional[str] = "America/Sao_Paulo"

    def __post_init__(self):

        self.format_dates()

    def format_dates(self):
        timezone = "America/Sao_Paulo"
        self.end_timestamp = datetime.fromisoformat(str(self.end_timestamp)).replace(
            tzinfo=ZoneInfo(timezone)
        )
        self.start_timestamp = datetime.fromisoformat(
            str(self.start_timestamp)
        ).replace(tzinfo=ZoneInfo(timezone))
