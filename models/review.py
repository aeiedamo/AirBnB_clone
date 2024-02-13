#!/usr/bin/python3
"""this creates a Review class"""
from models.base_model import BaseModel


class Review(BaseModel):
    """this defines a BaseModel class"""

    place_id = ""
    user_id = ""
    text = ""
