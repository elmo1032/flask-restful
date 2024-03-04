#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# standard python imports

import logging
from rich.console import Console
from rich.logging import RichHandler
from rich.traceback import install
# install the rich traceback formatter for better error reporting
install()

def create_logger():
    """Create a logger for use in all cases.

    This function creates a logger instance that can be used to log messages
    throughout the application. The log level is determined by the 'LOGLEVEL'
    environment variable. If the variable is not set, the default log level is
    set to 'WARNING'. The logger instance is returned, and can be used to log
    messages using the standard logging methods (e.g. debug(), info(), warning(),
    error(), critical()). The logger instance also includes a RichHandler, which
    formats log messages using the Rich library for better readability.

    Returns:
        logging.Logger: A logger instance that can be used to log messages
        throughout the application.
    """
    log_level = logging.WARNING
    if 'LOGLEVEL' in environ:
        log_level = environ['LOGLEVEL'].upper()
        log_level = getattr(logging, log_level, logging.WARNING)

    logger = logging.getLogger()
    logger.setLevel(log_level)
    logger.handlers = []

    console = Console()
    handler = RichHandler(console=console, rich_tracebacks=True)
    logger.addHandler(handler)

    return logger
