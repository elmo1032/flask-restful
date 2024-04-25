#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Import necessary modules
# Flask_restful is a lightweight framework for building RESTful APIs in Flask
from flask_restful import Resource, reqparse 

# Define a parser object to parse incoming request data
parser = reqparse.RequestParser()

# Add arguments to the parser object
# In this case, we're adding a 'name' argument that's required and a 'greeting' argument that's optional
parser.add_argument('name', type=str, required=True, help='Name parameter is required')
parser.add_argument('greeting', type=str, default='Hello', help='Greeting parameter is optional, default is "Hello"')

class HelloWorld(Resource):
    def get(self):
        # Get the arguments from the request data using the parser object
        args = parser.parse_args()

        # Extract the 'name' and 'greeting' arguments from the request data
        name = args['name']
        greeting = args['greeting']

        # Construct a greeting message using the 'name' and 'greeting' arguments
        greeting_message = f"{greeting}, {name}!"

        # Return the greeting message as a JSON response
        return {'message': greeting_message}
