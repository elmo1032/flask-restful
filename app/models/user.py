#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Import necessary Python standard library modules
import contextlib

# Add any necessary import statements here
# For example, if you need to import a third-party library, you can do so here

# Define any necessary functions or classes here
# For example, if you have a function that connects to a database, you can define it here
@contextlib.contextmanager
def connect_db():
    """Connects to the database using a context manager to automatically close the connection.

    This decorator allows the connection to be used as a context manager, which automatically closes the connection when the block is exited.

    Yields:
        connection (sqlite3.Connection): A connection object representing the database connection.

    Raises:
        sqlite3.Error: If there is an error connecting to the database.

    """
    connection = db.connect()  # Connect to the database
    try:
        yield connection  # Yield the connection object to the user
    finally:
        connection.close()  # Close the connection when the block is exited

