#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Import the database object from the app's db module
from app.db import db

# Define a new class StoreModel that inherits from db.Model
class StoreModel(db.Model):

    # Set the name of the table in the database
    __tablename__ = 'stores'

    # Define a column for the id, which is the primary key
    id = db.Column(db.Integer, primary_key=True)

    # Define a column for the store name, with a maximum length of 80 characters
    name = db.Column(db.String(80))
