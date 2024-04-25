#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
from sqlalchemy.ext.declarative import DeclarativeMeta
from datetime import datetime
from typing import Any

class Base(metaclass=DeclarativeMeta):
    """
    The base class for all models in the application.
    This class is used to enable the Declarative Meta class which allows for
    the creation of SQLAlchemy models in a more Pythonic and declarative way.
    """
    pass

class User(Base):
    """
    The User model for the application.
    This model represents a user in the database and maps to the 'users' table.
    """
    __tablename__ = 'users'  # The name of the table in the database.

    id = Column(Integer, primary_key=True)  # The user's unique identifier.
    name = Column(String)  # The user's name.
    email = Column(String)  # The user's email address.
    created_at = Column(DateTime)  # The date and time the user was created.

def serialize(obj: Any) -> dict:
    """
    A function to serialize an object into a dictionary.
    This function is used to convert SQLAlchemy models into dictionaries
    that can be easily serialized and sent over the network.
    """
    if isinstance(obj, Base):
        result = {c.name: getattr(obj, c.name) for c in obj.__table__.columns}
        result['__tablename__'] = obj.__tablename__
        return result
    elif isinstance(obj, datetime):
        return obj.isoformat()
    else:
        raise TypeError(f"Type {type(obj)} not serializable")
