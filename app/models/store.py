#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from app.db import db # Import the database object from the app's db module

class StoreModel(db.Model):
    """
    Store model for storing store information in the database.
    This class represents a table in the database to store store information.
    """

    __tablename__ = 'stores' # The name of the table in the database
    id = db.Column(db.Integer, primary_key=True) # An auto-incrementing primary key for the table
    name = db.Column(db.String(80), nullable=False) # A non-nullable string column to store the store name

    def __repr__(self):
        """
        Provide a human-readable representation of the StoreModel object.
        This method is called when the object is represented as a string,
        such as in the console or in a debugger.
        """
        return f'<StoreModel id={self.id} name={self.name}>'
