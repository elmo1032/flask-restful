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
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    price = db.Column(db.Float(precision=2))

    # Defining a foreign key relationship with the StoreModel class
    store_id = db.Column(db.Integer, db.ForeignKey('stores.id'))
    store = db.relationship('StoreModel')

    # Initializing the ItemModel class with the given name, price, and store_id
    def __init__(self, name, price, store_id):
        self.name = name
        self.price = price
        self.store_id = store_id

    # Defining a method to convert the ItemModel object to a JSON object
    def json(self):
        return {'name': self.name, 'price': self.price, 'store_id': self.store_id}

    # Defining a class method to find an ItemModel object by name
    @classmethod
    def find_by_name(cls, name):
        # Executing a SELECT query to find the first ItemModel object with the given name
        return cls.query.filter_by(name=name).first()  # simple TOP 1 select

    # Defining a method to save the ItemModel object to the database
    def save_to_db(self):  # Upserting data
        # Adding the ItemModel object to the database session and committing the changes
        db.session.add(self)
        db.session.commit()  # B
