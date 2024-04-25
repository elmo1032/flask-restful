#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# standard python imports

import logging # importing the built-in logging module for logging messages throughout the application
from rich.console import Console # importing the Console class from the Rich library for better console output
from rich.logging import RichHandler # importing the RichHandler class from the Rich library for better log formatting
from rich.traceback import install # importing the install function from the Rich library for better error reporting

def create_logger():
    """Create a logger for use in all cases.

    This function creates a logger instance that can be used to log messages
    throughout the application. The log level is determined by the 'LOGLEVEL'

