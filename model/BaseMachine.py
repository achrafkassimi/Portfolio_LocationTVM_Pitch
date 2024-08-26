#!/usr/bin/python3
"""
This module defines a base class for (T-V-M) models in our location_TVM clone
"""
# import uuid
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, DateTime, String
# from os import getenv

# time = "%Y-%m-%dT%H:%M:%S.%f"
Base = declarative_base()

class BaseMachine:
    """
        A base class for (T-V-M) models in our location_TVM clone
    """
    #  models.storage_t == "db"
    id = Column(String(60), primary_key=True)
    created_at = Column(DateTime, default=datetime.utcnow())
    updated_at = Column(DateTime, default=datetime.utcnow())