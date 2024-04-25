import psycopg2

from models.events import Event
from repository.base_client import BaseRepository

class PostgresClient(BaseRepository):

    def __init__ (self, database, host, port, user, password):

        self.params = {
            'database': database,
            'user': user,
            'password': password,
            'host': host,
            'port': port
        }

    def get(self, table, id=None):
        sql = f"""
            SELECT
                name,
                start_timestamp,
                end_timestamp,
                all_day,
                url,
                description,
                address
            FROM
                {table};
        """
        with psycopg2.connect(**self.params) as conn:
            with conn.cursor() as cursor:
                cursor.execute(sql)
                event_array = cursor.fetchall()
                event = []
                for array in event_array:
                    event.append(Event(
                        title= array[0],
                        start_timestamp= array[1],
                        end_timestamp= array[2],
                        all_day= array[3],
                        url= array[4],
                        description= array[5],
                        address = array[6]
                    ))
                return event

    def insert(self, table, data):

        pass

    def delete(self, table, id):
        
        with psycopg2.connect(**self.params) as conn:
            pass

    def update(self):
        
        with psycopg2.connect(**self.params) as conn:
            pass