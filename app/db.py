#!/usr/bin/env python3  # specifies the interpreter to use for this script
# -*- coding: utf-8 -*-  # specifies the encoding of the script

# Import the SQLAlchemy class from the flask_sqlalchemy library
from flask_sqlalchemy import SQLAlchemy

# Create an instance of the SQLAlchemy class
# This creates a new SQLAlchemy object that will be used to interact with the database
db = SQLAlchemy()

# The db object can be used to define database models, query the database, and perform other database-related tasks
# By creating the db object here, it can be easily reused throughout the application to interact with the database
