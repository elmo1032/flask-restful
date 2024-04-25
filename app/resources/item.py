#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import logging

# Importing required modules and libraries
from flask_restful import Resource, reqparse  # For creating API resources and parsing request arguments
from flask_jwt_extended import jwt_required  # For JWT authentication
from app.models.item import ItemModel  # Importing the ItemModel from the app/models/item.py
from app.util.logz import create_logger  # Importing the create_logger function from app/util/logz.py

# Creating a logger instance
logger = create_logger(__name__)

class ItemResource(Resource):
    @classmethod
    @jwt_required()
    def get(cls, name):
        """
        Get item by name
        """
        item = ItemModel.find_by_name(name)
        if item:
            return item.json()
        return {"message": "Item not found"}, 404

    @classmethod
    @jwt_required()
    def post(cls, name):
        """
        Create a new item
        """
        if ItemModel.find_by_name(name):
            return {"message": "An item with name '{}' already exists.".format(name)}, 400

        data = cls.parser.parse_args()
        item = ItemModel(name, **data)

        try:
            item.save_to_db()
        except Exception as e:
            logger.error(e)
            return {"message": "An error occurred while creating the item."}, 500

        return item.json(), 201

    @classmethod
    @jwt_required()
    def put(cls, name):
        """
        Update an existing item
        """
        data = cls.parser.parse_args()
        item = ItemModel.find_by_name(name)

        if not item:
            try:
                item = ItemModel(name, **data)
            except Exception as e:
                logger.error(e)
                return {"message": "An error occurred while creating the item."}, 500
        else:
            item.price = data["price"]

        item.save_to_db()

        return item.json()

    @classmethod
    @jwt_required()
    def delete(cls, name):
        """
        Delete an item
        """
        item = ItemModel.find_by_name(name)
        if not item:
            return {"message": "Item not found"}, 404
        item.delete_from_db()
        return {"message": "Item deleted"}

# Initializing the parser
cls = ItemResource
cls.parser = reqparse.RequestParser()
cls.parser.add_argument("price", type=float, required=True, help="This field cannot be left blank.")
