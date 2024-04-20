from app.src.events import Event
from app.src.postgres_client import PostgresClient
from app.src.base_client import BaseDatabaseClient

class EventsManager():

    def __init__(self, database:BaseDatabaseClient):
        self.database=database

    def get_events(self) -> list[Event]:
        events=self.database.get(events)
        return list(self.events.values())

    def add_event(self, event: Event) -> int:

        event_id = self.next_id
        self.events[self.next_id] = event
        self.next_id += 1
        return event_id

    def update_event(self, id, event: Event) -> bool:

        if self.events.get(id):
            self.events[id] = event
            return True
        return False

    def remove_event(self, event_id) -> bool:

        if self.events.get(event_id):
            self.deleted_events[event_id] = self.events.pop(event_id)
            return True
        return False
