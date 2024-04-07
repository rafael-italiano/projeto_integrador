CREATE TABLE event (
    id SERIAL PRIMARY KEY,
    start_timestamp BIGINT NOT NULL,
    end_timestamp VARCHAR NOT NULL,
    all_day BOOLEAN NOT NULL,
    url VARCHAR[100] NOT NULL,
    description VARCHAR NOT NULL UNIQUE
);