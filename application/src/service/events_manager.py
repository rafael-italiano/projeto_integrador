from models.events import Event
from repository.base_client import BaseRepository

class EventsManager():

    def __init__(self, database:BaseRepository):

        self.database=database

    def get_events(self) -> list[Event]:

        events=self.database.get(events)

        return list(self.events.values())

    def add_event(self, event: Event) -> int:

        self.database.insert(event)

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
