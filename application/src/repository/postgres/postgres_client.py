import psycopg2

from models.events import Event
from repository.base_client import BaseRepository
from dataclasses import asdict

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
                event.name,
                event.start_timestamp,
                event.end_timestamp,
                event.all_day,
                event.url,
                event.description,
                event.address,
                city.name,
                event.archived
            FROM
                event
            JOIN city ON event.city_id = city.id;
        """
        with psycopg2.connect(**self.params) as conn:
            with conn.cursor() as cursor:
                cursor.execute(sql)
                event_array = cursor.fetchall()
                event = []
                for array in event_array:
                    event.append(Event(
                        name= array[0],
                        start_timestamp= array[1],
                        end_timestamp= array[2],
                        all_day= array[3],
                        url= array[4],
                        description= array[5],
                        address = array[6],
                        city_id = array[7],
                        archived= array[8]
                    ))
                return event

    def insert(self, data, table="event"):
        data = asdict(data)
        columns = ", ".join(data.keys())
        values_placeholder = ", ".join(["%s"] * len(data))
        sql = f"""
        INSERT INTO {table} ({columns})
        VALUES ({values_placeholder})
        RETURNING *
        """
        with psycopg2.connect(**self.params) as conn:
            with conn.cursor() as cursor:
                cursor.execute(sql, tuple(data.values()))
                return cursor.fetchone()

    def delete(self, table, id):
        
        with psycopg2.connect(**self.params) as conn:
            pass

    def update(self):
        
        with psycopg2.connect(**self.params) as conn:
            pass