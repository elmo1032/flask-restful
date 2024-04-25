#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# standard python imports

from flask_restful import Resource, reqparse  # Import Resource and reqparse from Flask-RESTful for creating API endpoints and parsing request data
from flask import jsonify  # Import jsonify from Flask to return JSON responses
from flask_jwt_extended import (  # Import create_access_token, jwt_required, current_user, and create_logger from Flask-JWT-Extended for handling authentication
    create_access_token, jwt_required, current_user, create_logger
)
from app.models.user import UserModel  # Import UserModel from app/models/user.py
from app.util.encoder import AlchemyEncoder  # Import AlchemyEncoder from app/util/encoder.py
import json  # Import json for encoding UserModel object to JSON

class User(Resource):
    def __init__(self):
        self.logger = create_logger()  # Initialize the logger

    parser = reqparse.RequestParser()  # Initialize reqparse for parsing request data
    parser.add_argument('username', type=str, required=True, help='This field cannot be left blank')
    parser.add_argument('password', type=str, required=True, help='This field cannot be left blank')

    def post(self):
        """
        Create a new user and return an access token.
        """
        data = User.parser.parse_args()  # Parse request data
        username = data['username']
        password = data['password']

        user = UserModel.query.filter_by(username=username).one_or_none()  # Query the database for a user with the given username
        if not user or not user.check_password(password):  # If the user doesn't exist or the password is incorrect, return a 401 status code with an error message
            return {'message': 'Wrong username or password.'}, 401

        # Create an access token using the user object and return it as a JSON response
        access_token = create_access_token(identity=json.dumps(user, cls=AlchemyEncoder))
        return jsonify(access_token=access_token)

    @jwt_required()  # Require a valid access token for this endpoint
    def get(self):
        """
        Return user information for the currently authenticated user.
        """
        # Retrieve the current user object using current_user and return it as a JSON response
        return jsonify(
            id=current_user.id,
            full_name=current_user.full_name,
            username=current_user.username,
        )

class UserRegister(Resource):
    def __init__(self):
        self.logger = create_logger()  # Initialize the logger

    parser = reqparse.RequestParser()  # Initialize reqparse for parsing request data
    parser.add_argument('username', type=str, required=True, help='This field cannot be left blank')
    parser.add_argument('password', type=str, required=True, help='This field cannot be left blank')

    def post(self):
        """
        Create a new user and return a success message.
        """
        data = UserRegister.parser.parse_args()  # Parse request data

        existing_user = UserModel.find_by_username(data['username'])  # Query the database for a user with the given username
        if existing_user:  # If a user with the given username already exists, return a 400 status code with an error message
            return {'message': 'UserModel has already been created, aborting.'}, 400

        user = UserModel(**data)  # Create a new UserModel object with the provided data
        user.save_to_db()  # Save the user object to the database

        return {'message': 'user has been created successfully.'}, 201  # Return a 201 status code with a success message
