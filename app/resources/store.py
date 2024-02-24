#!/usr/bin/env python3
#
# A Python script for a Flask RESTful resource to manage stores in a database.
#
# Standard Python imports

from flask_restful import Resource  # Import the Resource class from Flask-RESTful
from app.models.store import StoreModel  # Import the StoreModel class from the stores model
from flask_jwt_extended import jwt_required  # Import the jwt_required decorator
from app.util.logz import create_logger  # Import the create_logger function

class Store(Resource):
    """
    A class representing a Flask RESTful resource for managing stores.
    """

    def __init__(self):
        """
        Initialize the Store resource.
        """
        self.logger = create_logger()  # Create a logger instance

    def get(self, name):
        """
        Handle GET requests to retrieve a store by name.

        :param name: The name of the store to retrieve
        :return: A JSON object representing the store or an error message
        """
        store = StoreModel.find_by_name(name)  # Find the store by name
        if store:
            return store.json()  # Return the store as a JSON object
        return {'message': 'Store not found'}, 404  # Return a 404 error if the store is not found

    @jwt_required()  # Require a JWT token for this endpoint
    def post(self, name):
        """
        Handle POST requests to create a new store.

        :param name: The name of the new store
        :return: A JSON object representing the new store or an error message
        """
        if StoreModel.find_by_name(name):  # Check if a store with the same name already exists
            return {'message': "A store with name '{}' already exists.".format(name)}, 400

        store = StoreModel(name)  # Create a new store instance
        try:
            store.save_to_db()  # Save the new store to the database
        except:
            return {"message": "An error occurred creating the store."}, 500  # Return a 500 error if there's an issue saving
