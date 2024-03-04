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

