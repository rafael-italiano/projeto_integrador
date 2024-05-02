import os

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from repository.postgres.postgres_client import PostgresClient
from service.events_manager import EventsManager
from models.events import Event

app = FastAPI()
origins = [
    "http://localhost:8081",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



events_manager = EventsManager(
    PostgresClient(
        database=os.environ.get("POSTGRES_DB", "event_management"),
        host=os.environ.get("POSTGRES_HOST", "localhost"),
        port=os.environ.get("POSTGRES_PORT", 5432),
        user=os.environ.get("POSTGRES_USER", "postgres"),
        password=os.environ.get("POSTGRES_PASSWORD", "password"),
    )
)


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
        description=event['description'],
        address = event['address']
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
        description=event['description'],
        address = event['address']
    )
    return events_manager.update_event(id, new_event)

@app.delete('/events/{id}')
def delete_event(id: int):

    return events_manager.remove_event(id)
