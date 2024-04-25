#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# standard python imports

from app.db import db # Import the database object from the app's db module

class StoreModel(db.Model): # Define a new class StoreModel that inherits from db.Model
    __tablename__ = 'stores' # Set the name of the table in the database

    # Define a column for the id, which is the primary key
    id = db.Column(db.Integer, primary_key=True)

    # Define a column for the store name, with a maximum length of 80 characters
    name = db.Column(db.String(80))

    # Define a relationship to the ItemModel class, with the 'items' as the relationship name
    items = db.relationship('ItemModel', lazy='dynamic')

    def __init__(self, name): # Define the constructor for the StoreModel class
        """
        Initialize a new StoreModel instance with a given name.

        :param name: The name of the store.
        """
        self.name = name # Set the name attribute to the input value

    def json(self): # Define a method to convert the StoreModel object to a JSON-serializable dictionary
        """
        Convert the StoreModel object to a JSON-serializable dictionary.

        :return: A dictionary containing the store's name and a list of its items in JSON format.
        """
        return {
            'name': self.name,
            'items': [item.json() for item in self.items.all()] # Convert each item to a JSON-serializable dictionary
        }

    @classmethod # Decorate the method as a class method
    def find_by_name(cls, name): # Define a class method to find a StoreModel object by its name
        """
        Find a StoreModel object in the database by its name.

        :param name: The name of the store to find.
        :return: The first StoreModel object with the given name, or None if no such object exists.
        """
        return cls.query.filter_by(name=name).first() # Query the database for the first StoreModel object with the given name

    def save_to_db(self): # Define a method to save the StoreModel object to the database
        """
        Save the StoreModel object to the database.
        """
        db.session.add(self) # Add the object to the database session
        db.session.commit() # Commit the changes to the database

    def delete_from_db(self): # Define a method to delete the StoreModel object from the database
        """
        Delete the StoreModel object from the database.
        """
        db.session.delete(self) # Delete the object from the database session
        db.session.commit() # Commit the changes to the database
