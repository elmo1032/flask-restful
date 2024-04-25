#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from app.db import db  # Importing the db object from the app.db module

class ItemModel(db.Model):
    """
    A model for an item in the database.
    This class represents a table in the database, with columns for 'id', 'name', and 'price'.
    """
    __tablename__ = 'items'  # The name of the table in the database

    id = db.Column(db.Integer, primary_key=True)  # The 'id' column, which is the primary key and an integer
    name = db.Column(db.String(80))  # The 'name' column, which is a string with a maximum length of 80 characters
    price = db.Column(db.Numeric(10, 2))  # The 'price' column, which is a numeric value with 10 digits in total and 2 digits after the decimal point

    def to_dict(self) -> Dict[str, str]:
        """
        Convert the ItemModel object to a dictionary.
        This method returns a dictionary representation of the ItemModel object,
        excluding the 'id' and '_sa_instance_state' columns.
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
