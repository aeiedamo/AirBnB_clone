#!/usr/bin/python3
"""this files includes files in this directory to convert them as a package"""
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
