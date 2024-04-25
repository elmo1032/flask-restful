#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
from sqlalchemy.ext.declarative import DeclarativeMeta

class Base(metaclass=DeclarativeMeta):
    pass

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)

def serialize(obj):
    if isinstance(obj, Base):
        return obj.__dict__
    elif isinstance(obj, datetime):
        return obj.isoformat()
    return obj

def main():
    user = User(name='John Doe', email='john.doe@example.com')
    user_dict = serialize(user)
    print(json.dumps(user_dict))

if __name__ == '__main__':
    main()
