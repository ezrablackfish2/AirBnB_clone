#!/usr/bin/python3
"""Defines the Place class."""
from models.base_model import BaseModel


class Place(BaseModel):
    """Represent a place.

    Attributes:
        city_id (str): the identification of the city.
        user_id (str): The identification of the user.
        name (str): The place name.
        description (str):  place description.
        number_rooms (int): room numbers.
        number_bathrooms (int): bathrom numbers.
        max_guest (int): max number of guests .
        price_by_night (int): night price of one place.
        latitude (float): place latitude.
        longitude (float): place longitude.
        amenity_ids (list): identification amenity.
    """

    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
