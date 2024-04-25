#!/usr/bin/env python3
# This line specifies the interpreter that should be used to run this script.
# In this case, it's Python 3.

# -*- coding: utf-8 -*-
# This line specifies the encoding used in the script. In this case, it's UTF-8.

import logging
# This line imports the logging module, which is used for logging messages and errors.

from flask_restful import Resource, reqparse  # For creating API resources and parsing request arguments
# This line imports the Resource and reqparse classes from the flask_restful module.
# Resource is used to create API resources, and reqparse is used to parse request arguments.

from flask_jwt_extended import jwt_required  # For JWT authentication
# This line imports the jwt_required decorator from the flask_jwt_extended module.
# It's used to protect API endpoints that require JWT authentication.

from app.models.item import ItemModel  # Importing the ItemModel from the app/models/item.py
# This line imports the ItemModel class from the app/models/item.py module.
# The ItemModel class is used to represent an item in the database.

from app.util.logz import create_logger  # Importing the create_logger function from app/util/logz.py
# This line imports the create_logger function from the app/util/logz.py module.
# The create_logger function is used to create a logger object that can be used to log messages and errors.
