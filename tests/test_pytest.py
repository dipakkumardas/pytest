# Create , Update , Read , Delete

# Request
# Faker
# pyTest

import pytest
import requests


def test_get_req():
    response = requests.get("https://restful-booker.herokuapp.com/booking")
    assert response.status_code == 200
    assert len(response.json()) > 0


def test_post_create_token():
    payload = {
        "username": "admin",
        "password": "password123"
    }

    headers = {
        "Content-Type": "application/json",
    }
    response = requests.post("https://restful-booker.herokuapp.com/auth", headers=headers, json=payload)
    assert response.status_code == 200
    print(response.text)
    print(response.json()["token"])


def test_create_booking():
    payload_create_booking = {
        "firstname": "pramod",
        "lastname": "Brown",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2023-08-15",
            "checkout": "2023-08-17"
        },
        "additionalneeds": "Breakfast"
    }

    headers = {
        "Content-Type": "application/json",
    }
    response = requests.post("https://restful-booker.herokuapp.com/booking", headers=headers, json=payload_create_booking)
    print(response.json())
    bookingid = response.json()["bookingid"]
    print(bookingid)
    print(response.status_code)
    assert response.status_code == 200

#
# def test_patch_req():
#     response = requests.get("https://restful-booker.herokuapp.com/booking")
#     print(response.text)
#     print(response.json())
#     print(response.status_code)
#     assert response.status_code == 200
#
#
# def test_delete_req():
#     response = requests.get("https://restful-booker.herokuapp.com/booking")
#     print(response.text)
#     print(response.json())
#     print(response.status_code)
#     assert response.status_code == 200
