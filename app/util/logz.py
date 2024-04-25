#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import logging # Import the built-in logging module for logging messages throughout the application
from rich.console import Console # Import the Console class from the Rich library for better console output
from rich.logging import RichHandler # Import the RichHandler class from the Rich library for better log formatting
from rich.traceback import install # Import the install function from the Rich library for better error reporting

def create_logger():
    """Create a logger for use in all cases.

    This function creates a logger instance that can be used to log messages
    throughout the application. The log level is determined by the 'LOGLEVEL'
    environment variable. If the variable is not set, the default level is 'WARNING'.

    Returns:
        logging.Logger: A logger instance with the given log level.
    """
    # Create a logger instance
    # The logger instance is used to log messages throughout the application
    logger = logging.getLogger()

    # Set the log level based on the 'LOGLEVEL' environment variable
    # If the 'LOGLEVEL' variable is not set, the default log level is 'WARNING'
    log_level = logging.WARNING
    if "LOGLEVEL" in environ:
        log_level_str = environ["LOGLEVEL"].upper()
        log_levels = {
            "DEBUG": logging.DEBUG,
            "INFO": logging.INFO,
            "WARNING": logging.WARNING,
            "ERROR": logging.ERROR,
            "CRITICAL": logging.CRITICAL,
        }
        if log_level_str in log_levels:
            log_level = log_levels[log_level_str]

    # Set the log format
    # The log format specifies how log messages are displayed
    formatter = logging.Formatter(
        "[%(levelname)s] %(message)s (in %(filename)s:%(lineno)d)"
    )

    # Add a RichHandler to the logger
    # The RichHandler is used to format log messages using the Rich library
    rich_handler = RichHandler(markup=True, rich_tracebacks=True)
    rich_handler.setFormatter(formatter)
    logger.addHandler(rich_handler)

    # Set the log level for the logger
    # The log level determines which log messages are displayed
    logger.setLevel(log_level)

    # Return the logger instance
    return logger
