import pytest
from fastapi import FastAPI
from fastapi.testclient import TestClient
from controller.main import app

client = TestClient(app)


def test_index():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Olá Mundo!"}


def test_create_event():
    response = client.post(
        "/events",
        json={
            "name": "Test Event",
            "start_timestamp": "2021-09-01T00:00:00",
            "end_timestamp": "2021-09-01T23:59:59",
            "all_day": False,
            "url": "https://example.com",
            "description": "Test description",
            "address": "Test address",
            "city_id": 1,
            "archived": False,
        },
    )

    [
        _,
        city_id,
        name,
        start_timestamp,
        end_timestamp,
        all_day,
        url,
        description,
        address,
        archived,
        _,
        _,
    ] = response.json()

    assert response.status_code == 200
    assert city_id == 1
    assert name == "Test Event"
    assert start_timestamp == "2021-09-01T03:00:00+00:00"
    assert end_timestamp == "2021-09-02T02:59:59+00:00"
    assert all_day == False
    assert url == "https://example.com"
    assert description == "Test description"
    assert address == "Test address"
    assert archived == False


# def test_get_events():
#     response = client.get("/events")
#     assert response.status_code == 200
#     assert response.json() == [{'id': 1, 'title': 'Test Event'}]
