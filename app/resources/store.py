#!/usr/bin/env python3

import json
from flask import request
from flask_restful import Resource
from flask_jwt_extended import jwt_required

# Import the custom logger from app.util.logz
from app.models.store import StoreModel
from app.util.logz import create_logger


class Store(Resource):
    """
    A class representing a Flask RESTful resource for managing stores.
    """

    def __init__(self):
        """
        Initialize the Store resource and create a logger instance.
        """
        self.logger = create_logger()

    def get(self, name):
        """
        Handle GET requests to retrieve a store by name.

        :param name: The name of the store to retrieve
        :return: A JSON object representing the store or an error message
        """
        store = StoreModel.find_by_name(name)  # Find the store by name
        if store:
            return json.dumps(store.json())  # Return the store as a JSON object if found
        return {'message': 'Store not found'}, 404  # Return a 404 error if the store is not found

    @jwt_required()  # Require a JWT token for this endpoint
    def post(self, name):
        """
        Handle POST requests to create a new store.

        :param name: The name of the new store
        :return: A JSON object representing the new store or an error message
        """
        if StoreModel.find_by_name(name):  # Check if a store with the same name already exists
            return {'message': f"A store with name '{name}' already exists."}, 400

        store = StoreModel(name)  # Create a new store instance
        try:
            store.save_to_db()  # Save the new store to the database
        except Exception as e:
            self.logger.error(f"Error creating store: {str(e)}")  # Log any exceptions during the save operation
            return {"message": "An error occurred creating the store."}, 500

        return json.dumps(store.json()), 201  # Return the new store as a JSON object with a 201 status code

    def delete(self, name):
        """
        Handle DELETE requests to delete a store by name.

        :param name: The name of the store to delete
        :return: A success message or an error message
        """
        store = StoreModel.find_by_name(name)  # Find the store by name
        if not store:
            return {'message': 'Store not found'}, 404  # Return a 404 error if the store is not found

        try:
            store.delete_from_db()  # Delete the store from the database
        except Exception as e:
            self.logger.error(f"Error deleting store: {str(e)}")  # Log any exceptions during the delete operation
            return {"message": "An error occurred deleting the store."}, 500

        return {'message': f"Store '{name}' deleted."}  # Return a success message

    def put(self, name):
        """
        Handle PUT requests to update a store by name.

        :param name: The name of the store to update
        :return: A JSON object representing the updated store or an error message
        """
        data = request.get_json()  # Get the request data as JSON
        if not data or 'name' not in data:  # Check if the request data is valid
            return {'message': 'Invalid request body'}, 400

        store = StoreModel.find_by_name(name)  # Find the store by name
        if not store:
            return {'message': 'Store not found'}, 404  # Return a 404 error if the store is not found

        store.name = data['name']  # Update the store name
        try:
            store.save_to_db()  # Save the updated store to the database
        except Exception as e:
            self.logger.error(f"Error updating store: {str(e)}")  # Log any exceptions during the save operation
            return {"message": "An error occurred updating the store."}, 500

        return json.dumps(store.json())  # Return the updated store as a JSON object

