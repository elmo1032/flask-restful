#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Importing required modules and libraries
from flask_restful import Resource, reqparse  # For creating API resources and parsing request arguments
from flask_jwt_extended import jwt_required  # For JWT authentication
from app.models.item import ItemModel  # Importing the ItemModel from the app/models/item.py
from app.util.logz import create_logger  # Importing the create_logger function from app/util/logz.py

class Item(Resource):
    # Initializing the parser for this resource with required fields and their types
    parser = reqparse.RequestParser() 
    parser.add_argument('price', type=float, required=True, help='This field cannot be left blank')
    parser.add_argument('store_id', type=int, required=True, help='Must enter the store id')

    def __init__(self):
        # Creating a logger instance for this resource
        self.logger = create_logger()

    @jwt_required()  # Requires JWT authentication
    def get(self, name):
        # Finding the item by name and returning its JSON representation
        item = ItemModel.find_by_name(name)
        self.logger.info(f'returning item: {item.json()}')
        if item:
            return item.json()
        return {'message': 'Item not found'}, 404

    @jwt_required()
    def post(self, name):
        # Logging the parsed arguments
        self.logger.info(f'parsed args: {Item.parser.parse_args()}')

        # Checking if an item with the same name already exists
        if ItemModel.find_by_name(name):
            return {'message': "An item with name '{}' already exists.".format(name)}, 400

        # Parsing the request arguments and creating a new ItemModel instance
        data = Item.parser.parse_args()
        item = ItemModel(name, data['price'], data['store_id'])

        # Saving the item to the database and handling any exceptions
        try:
            item.save_to_db()
        except:
            return {"message": "An error occurred inserting the item."}, 500

        # Returning the JSON representation of the created item along with a 201 status code
        return item.json(), 201

    @jwt_required()
    def delete(self, name):
        # Finding the item by name and deleting it from the database
        item = ItemModel.find_by_name(name)
        if item:
            item.delete_from_db()

            # Returning a success message
            return {'message': 'item has been deleted'}

    @jwt_required()
    def put(self, name):
        # Parsing the request arguments
        data = Item.parser.parse_args()

        # Finding the item by name and updating it with the new price
        item = ItemModel.find_by_name(name)
        if item is None:
            item = ItemModel(name, data['price'])
        else:
            item.price = data['price']

        # Saving the updated item to the database
        item.save_to_db()

        # Returning the JSON representation of the updated item
        return item.json()

class ItemList(Resource):
    @jwt_required()
    def get(self):
        # Fetching all items from the database and returning their JSON representations
        return {
            'items': [item.json() for item in ItemModel.query.all()]}  # More pythonic
        ##return {'items': list(map(lambda x: x
