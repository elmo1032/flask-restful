#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from app.db import db
from typing import Dict

class ItemModel(db.Model):
    """
    A model for an item in the database.
    """
    __tablename__ = 'items'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    price = db.Column(db.Numeric(10, 2))

    def to_dict(self) -> Dict[str, str]:
        """
        Convert the ItemModel object to a dictionary.
        """
        result = {}
        for col in self.__table__.columns:
            if col.name != 'id' and col.name != '_sa_instance_state':
                value = getattr(self, col.name)
                if isinstance(value, str):
                    result[col.name] = value
                else:
                    result[col.name] = str(value)
        return result
