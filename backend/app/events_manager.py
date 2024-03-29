from events import Event


class EventsManager():
    
    def __init__(self):

        self.events = {}
        self.next_id = 1

    def get_events(self) -> list[Event]:

        return list(self.events.values())
    
    def add_event(self, event: Event) -> int:

        event_id = self.next_id 
        self.events[self.next_id] = event
        self.next_id += 1
        return event_id

    def update_events(self, id, event: Event) -> bool:

        if self.events.get(id):
            self.events[id] = event
            return True
        return False

    def delete_events(self, event_id) -> bool:
        
        if self.events.get(event_id):
            del self.events[event_id]
            return True
        
        return False