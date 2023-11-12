#!/usr/bin/python3
"""Defines the Place class."""
from models.base_model import BaseModel


class Place(BaseModel):
    """Represent a place.
    
    Attributes:
    there are 6 attributes for this class in this file

    """

    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    longitude = 0.0
    amenity_ids = []
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
