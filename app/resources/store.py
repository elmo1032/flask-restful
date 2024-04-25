#!/usr/bin/env python3

import json
from flask import request
from flask_restful import Resource
from flask_jwt_extended import jwt_required

from app.models.store import StoreModel
from app.util.logz import create_logger


class Store(Resource):
    """
    A class representing a Flask RESTful resource for managing stores.
    """

    def __init__(self):
        """
        Initialize the Store resource.
        """
        self.logger = create_logger()

    def get(self, name):
        """
        Handle GET requests to retrieve a store by name.

        :param name: The name of the store to retrieve
        :return: A JSON object representing the store or an error message
        """
        store = StoreModel.find_by_name(name)
        if store:
            return json.dumps(store.json())
        return {'message': 'Store not found'}, 404

    @jwt_required()
    def post(self, name):
        """
        Handle POST requests to create a new store.

        :param name: The name of the new store
        :return: A JSON object representing the new store or an error message
        """
        if StoreModel.find_by_name(name):
            return {'message': f"A store with name '{name}' already exists."}, 400

        store = StoreModel(name)
        try:
            store.save_to_db()
        except Exception as e:
            self.logger.error(f"Error creating store: {str(e)}")
            return {"message": "An error occurred creating the store."}, 500

        return json.dumps(store.json()), 201

    def delete(self, name):
        """
        Handle DELETE requests to delete a store by name.

        :param name: The name of the store to delete
        :return: A success message or an error message
        """
        store = StoreModel.find_by_name(name)
        if not store:
            return {'message': 'Store not found'}, 404

        try:
            store.delete_from_db()
        except Exception as e:
            self.logger.error(f"Error deleting store: {str(e)}")
            return {"message": "An error occurred deleting the store."}, 500

        return {'message': f"Store '{name}' deleted."}

    def put(self, name):
        """
        Handle PUT requests to update a store by name.

        :param name: The name of the store to update
        :return: A JSON object representing the updated store or an error message
        """
        data = request.get_json()
        if not data or 'name' not in data:
            return {'message': 'Invalid request body'}, 400

        store = StoreModel.find_by_name(name)
        if not store:
            return {'message': 'Store not found'}, 404

        store.name = data['name']
        try:
            store.save_to_db()
        except Exception as e:
            self.logger.error(f"Error updating store: {str(e)}")
            return {"message": "An error occurred updating the store."}, 500

        return json.dumps(store.json())
