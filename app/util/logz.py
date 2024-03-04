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
    environment variable, with a default level of 'INFO'. The logger uses the
    'rich' handler for formatting log messages and tracebacks.
    """
    # get the log level from the environment variable or default to 'INFO'
    loglevel = os.environ.get('LOGLEVEL', 'INFO').upper()
    # create a RichHandler instance for formatting log messages and tracebacks
    rich_handler = RichHandler(rich_tracebacks=True, markup=True)
    # create a basic logger configuration with the specified log level and handler
    logging.basicConfig(level=loglevel, format='%(message)s',
                        datefmt="[%Y/%m/%d %H:%M;%S]",
                        handlers=[rich_handler])
    # return the logger instance
    return logging.getLogger('rich')
