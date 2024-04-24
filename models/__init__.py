#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""
import os

my_env = os.environ["HBNB_TYPE_STORAGE"]
if (my_env == "db"):
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
else:
    from models.engine.file_storage import FileStorage
    storage = FileStorage()
storage.reload()
