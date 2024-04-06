CREATE TABLE event (
    id SERIAL PRIMARY KEY,
    start_timestamp BIGINT NOT NULL,
    end_timestamp VARCHAR NOT NULL,
    all_day BOOLEAN NOT NULL,
    url VARCHAR[100] NOT NULL,
    end_timestamp VARCHAR NOT NULL UNIQUE
);

title: str
    start_timestamp: int
    end_timestamp: int
    all_day: bool
    url: str
    description: str


    www.