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
    (1, 'Emerson Ceará em Caraguatatuba - Se Acalme','2024-07-06 20:00:00', '2024-07-06 21:00:00', false, 'https://bileto.sympla.com.br/event/91771/d/244030/s/1663595', 'Quando a lenda Emerson Ceará conta uma história, você precisa estar lá para ouvir!', 'Av. Goiás, 187 - Indaiá, Caraguatatuba - SP, 11665-120', false, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
    (1,'Diego Besou em Caraguatatuba | PRONTO! SOCORRO!', '2024-07-21 20:00:00', '2024-07-06 21:00:00', false, 'https://bileto.sympla.com.br/event/91777/d/244057/s/1663669', 'O enfermeiro Diego Besou apresenta Pronto! Socoorro!, um espetáculo como você nunca viu sobre a área da saúde. Afinal, as coisas que acontecem em um pronto-socorro até Deus duvida!', 'Av. Goiás, 187 - Indaiá, Caraguatatuba - SP, 11665-120', false, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
    (3,'Retiro Ubatuba com Juju Priyah - Rompendo seus limites', '2024-06-07 16:00:00', '2024-06-09 15:00:00', false, 'https://www.sympla.com.br/evento/retiro-ubatuba-com-juju-priyah-rompendo-seus-limites/2447536', 'Rompendo limites com Juju Priyah!', 'Rua Paulo Verzoline, 193 Praia do Itamambuca', true, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP);
