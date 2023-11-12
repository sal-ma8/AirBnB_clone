#!/usr/bin/python3
"""Defines the User class."""
from models.base_model import BaseModel


class User(BaseModel):
    """ def for this class.

    Attributes:
        email (str): this is the e mail.
        password (str): this is the pass for users.
        first_name (str): this is the f mame od users.
        last_name (str): this is the second name od users.
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
