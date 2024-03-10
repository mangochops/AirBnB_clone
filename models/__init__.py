#!/usr/bin/python3
"""__init__ magic method for models directory"""
from models.engine.file_storage import FileStorage

"""Create an instance of FileStorage for managing data"""
storage = FileStorage()

"""Reload data from storage to ensure consistency"""
storage.reload()
