CREATE TABLE city (
    id SERIAL PRIMARY KEY,
    name VARCHAR(30) NOT NULL,
    state_name VARCHAR(30) NOT NULL
);

CREATE TABLE event (
    id SERIAL PRIMARY KEY,
    city_id INT NOT NULL,
    name VARCHAR(255) NOT NULL,
    start_timestamp TIMESTAMPTZ NOT NULL,
    end_timestamp TIMESTAMPTZ NOT NULL,
    all_day BOOLEAN NOT NULL,
    url VARCHAR(100) NOT NULL,
    description VARCHAR NOT NULL,
    address VARCHAR NOT NULL,
    archived BOOLEAN NOT NULL,
    created_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT fk_city FOREIGN KEY(city_id) REFERENCES city(id)
);

INSERT INTO city ("name", "state_name") VALUES
    ('Caraguatatuba', 'São Paulo'),
    ('São Sebastião', 'São Paulo'),
    ('Ubatuba', 'São Paulo'),
    ('São Bernardo do Campo', 'São Paulo'),
    ('Mogi das Cruzes', 'São Paulo'),
    ('Santos', 'São Paulo');

INSERT INTO event (city_id, name, start_timestamp, end_timestamp, all_day, url, description, address, archived, created_at, updated_at) 
VALUES 
    (1, 'DUMMY1','2024-04-25 08:00:00', '2024-04-25 17:00:00', false, 'google.com', 'Event description 1', '123 Main St', false, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
    (2,'DUMMY2', '2024-04-26 09:00:00', '2024-04-26 16:00:00', true, 'google.com', 'Event description 2', '456 Elm St', false, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
    (3,'DUMMY3', '2024-04-27 10:00:00', '2024-04-27 18:00:00', false, 'google.com', 'Event description 3', '789 Oak St', true, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP);
