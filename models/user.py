#!/usr/bin/python3
"""This file is for User Class"""
from models.base_model import BaseModel


class User(BaseModel):
    """This creates a User Class"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""
