#!/usr/bin/env python3  # specifies the interpreter to use for this script
# -*- coding: utf-8 -*-  # specifies the encoding of the script

import os

# Import the SQLAlchemy class from the flask_sqlalchemy library
from flask_sqlalchemy import SQLAlchemy

# Define the database URI based on the environment variable
# This allows the database to be easily configured for different environments (e.g. development, production)
database_uri = os.getenv('DATABASE_URI', 'sqlite:///app.db')

# Create an instance of the SQLAlchemy class
# This creates a new SQLAlchemy object that will be used to interact with the database
db = SQLAlchemy()

# The db object can be used to define database models, query the database, and perform other database-related tasks
# By creating the db object here, it can be easily reused throughout the application to interact with the database

# Set the database URI for the SQLAlchemy object
db.init_app(app, database_uri)

# Define a sample model for the database
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username
