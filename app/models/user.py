#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# standard python imports
import contextlib

# Add any necessary imports here

# Define any necessary functions or classes here

# Connect to the database using a context manager to automatically close the connection
@contextlib.contextmanager
def connect_db():
    """Connects to the database and returns a connection object. Automatically closes the connection when the block is exited."""
    connection = db.connect()
    try:
        yield connection
    finally:
        connection.close()


# Example usage
if __name__ == "__main__":
    # Connect to the database using the context manager
    with connect_db() as conn:
        # Perform database operations here
        pass

    # Alternatively, you can still connect to the database manually and close the connection manually
    # conn = connect_db()
    # Perform database operations here
    # close_db(conn)
