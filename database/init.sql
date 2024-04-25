CREATE TABLE city (
    id SERIAL PRIMARY KEY,
    name VARCHAR(30) NOT NULL,
    state_name VARCHAR(30) NOT NULL
);

CREATE TABLE event (
    id SERIAL PRIMARY KEY,
    city_id INT NOT NULL,
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