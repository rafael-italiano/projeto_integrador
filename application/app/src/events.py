from dataclasses import dataclass


@dataclass
class Event():

    title: str
    start_timestamp: int
    end_timestamp: int
    all_day: bool
    url: str
    description: str
    address: str
