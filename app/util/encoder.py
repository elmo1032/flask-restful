#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
from sqlalchemy.ext.declarative import DeclarativeMeta
from datetime import datetime
from typing import Any

class Base(metaclass=DeclarativeMeta):
    pass

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)
    created_at = Column(DateTime)

def serialize(obj: Any) -> dict:
    if isinstance(obj, Base):
        result = {c.name: getattr(obj, c.name) for c in obj.__table__.columns}
        result['__tablename__'] = obj.__tablename__
        return result
    elif isinstance(obj, datetime):
        return obj.isoformat()
    else:
        raise TypeError(f"Type {type(obj)} not serializable")

