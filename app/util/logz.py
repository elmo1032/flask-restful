#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import logging
from typing import Any
from rich.console import Console
from rich.logging import RichHandler
from rich.traceback import install

def create_logger() -> logging.Logger:
    """Create a logger for use in all cases.

    This function creates a logger instance that can be used to log messages
    throughout the application. The log level is determined by the 'LOGLEVEL'
    environment variable. If the variable is not set, the default level is 'WARNING'.

    Returns:
        logging.Logger: A logger instance with the given log level.
    """
    # Create a logger instance
    logger = logging.getLogger()

    # Remove the default handler of the logger
    logger.handlers.clear()

    # Set the log level based on the 'LOGLEVEL' environment variable
    # If the 'LOGLEVEL' variable is not set, the default log level is 'WARNING'
    log_level = logging.WARNING
    if "LOGLEVEL" in os.environ:
        log_level_str = os.environ["LOGLEVEL"].upper()
        log_levels = {
            "DEBUG": logging.DEBUG,
            "INFO": logging.INFO,
            "WARNING": logging.WARNING,
            "ERROR": logging.ERROR,
            "CRITICAL": logging.CRITICAL,
        }
        if log_level_str in log_levels:
            log_level = log_levels[log_level_str]
        else:
            raise ValueError(f"Invalid log level: {log_level_str}")

    # Set the log format
    # The log format specifies how log messages are displayed
    formatter = logging.Formatter(
        "[%(levelname)s] %(message)s (in %(filename)s:%(lineno)d)"
    )

    # Add a RichHandler to the logger
    # The RichHandler is used to format log messages using the Rich library
    install()
    console = Console()
    rich_handler = RichHandler(markup=True, rich_tracebacks=True, console=console)
    rich_handler.setFormatter(formatter)
    logger.addHandler(rich_handler)

    # Set the log level for the logger
    # The log level determines which log messages are displayed
    logger.setLevel(log_level)

    # Return the logger instance
    return logger
