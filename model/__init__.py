#!/usr/bin/python3
"""
create a unique FileStorage instance for your application
"""
from os import getenv
from model.engine.db_storage import DBStorage


storage = DBStorage()
storage.reload()
