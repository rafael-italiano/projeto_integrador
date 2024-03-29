from dataclasses import dataclass


@dataclass
class Event():

    title: str
    start_timestamp: int
    end_timestamp: int
    allDay: bool
    url: str
    description: str