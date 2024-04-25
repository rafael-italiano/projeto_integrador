import psycopg2

from models.events import Event
from repository.base_client import BaseRepository

class PostgresClient(BaseRepository):

    events = {
            1: Event(
                title= "sample",
                start_timestamp= "2024-12-12T09:00:00",
                end_timestamp= "2024-12-12T12:00:00",
                all_day= False,
                url= "https://www.google.com",
                description= "Event 1 Description",
                address = "cidade"
            )
        }

    def get(self, table, id=None):

        if id:
            return self.events[id]
        
        return list(self.events.values())

    
    def _connect(self):
        
        conn = psycopg2.connect("dbname=test user=postgres")

    def insert(self, table):

        event_id = self.next_id
        self.events[self.next_id] = event
        self.next_id += 1

    def delete(self, table, id):
        pass

    def update(self):
        pass



        
    
    


