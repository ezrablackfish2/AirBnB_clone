#!/usr/bin/python3
""" this is the class of user User class."""
from models.base_model import BaseModel


class User(BaseModel):
    """User Class.

    Attributes:
        email (str): user email.
        password (str): user password.
        first_name (str): first name.
        last_name (str):  last name.
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
