#!/usr/bin/python3
"""file to initiate the package"""
from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
