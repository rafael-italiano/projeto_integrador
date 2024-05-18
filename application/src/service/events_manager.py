from models.events import Event
from repository.base_client import BaseRepository

class EventsManager():

    def __init__(self, database:BaseRepository):

        self.database=database

    def get_events(self) -> list[Event]:
        
        events=self.database.get("event")
        return events

    def add_event(self, event: Event) -> int:
        return self.database.insert(event)

    def update_event(self, id, event: Event) -> bool:

        if self.database.get(event, id):
            self.database.update(event, id)
            return True
        return False

    def remove_event(self, id) -> bool:

        event = self.database.get("event", id)
        if not event:
            return False
        self.database.delete("event", id)
        return True
