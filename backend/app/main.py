import json

from fastapi import FastAPI

from events_manager import EventsManager
from events import Event

app = FastAPI()

events_manager = EventsManager()


@app.get('/')
def index():

    return {'message': 'Olá Mundo!'}

@app.get('/events')
def get_events():

    return events_manager.get_events()

@app.post('/events')
def create_event(event: dict):

    new_event = Event(
        title=event['title'],
        start_timestamp=event['start_timestamp'],
        end_timestamp=event['end_timestamp'],
        all_day=event['all_day'],
        url=event['url'],
        description=event['description']
    )
    event_id = events_manager.add_event(new_event)
    return event_id

@app.put('/events/{id}')
def update_event(id: int, event: dict):

    new_event = Event(
        title=event['title'],
        start_timestamp=event['start_timestamp'],
        end_timestamp=event['end_timestamp'],
        all_day=event['all_day'],
        url=event['url'],
        description=event['description']
    )
    return events_manager.update_event(id, new_event)

@app.delete('/events/{id}')
def delete_event(id: int):

    return events_manager.remove_event(id)