import psycopg2

from app.src.events import Event
from app.src.base_client import BaseDatabaseClient

class PostgresClient(BaseDatabaseClient):

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

    def connect(self):
        
        conn = psycopg2.connect("dbname=test user=postgres")

    def insert(self):
        pass

    def delete(self):
        pass

    def update(self):
        pass



        
    
    


