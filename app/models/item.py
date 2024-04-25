#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# standard python imports

# Importing the db object from the app.db module, which is a SQLAlchemy database
# session used to interact with the database
from app.db import db

# Defining the ItemModel class that inherits from db.Model
class ItemModel(db.Model):
    # Specifying the name of the table in the database
    __tablename__ = 'items'

    # Defining the columns of the table
    id = db.Column(db.Integer, primary_key=True)  # Primary key column for the items table
                                                 # This column will automatically
                                                 # increment and is unique for each row

    # Column to store the name of the item
    # This column can store up to 80 characters of text
    name = db.Column(db.String(80))

    # Column to store the price of the item
    # This column will store floating point numbers with a precision of 2 decimal places
    price = db.Column(db.Float(precision=2))

    # Defining a method to serialize the ItemModel object to a dictionary
    def serialize(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

