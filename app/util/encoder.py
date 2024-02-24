#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# standard python imports

import json

from sqlalchemy.ext.declarative import DeclarativeMeta

class AlchemyEncoder(json.JSONEncoder):
    """
    A custom JSON encoder for encoding SQLAlchemy objects into JSON.

    This class extends the json.JSONEncoder class to handle SQLAlchemy
    declarative base classes, which are not json-encodable by default.
    """

    def default(self, obj):
        """
        The default method is overridden to handle SQLAlchemy objects.

        If the object is an instance of an SQLAlchemy declarative base class,
        it will encode its fields into a dictionary. Otherwise, it will
        use the default JSONEncoder behavior.

        :param obj: The object to encode
        :return: A json-encodable dictionary
        """
        if isinstance(obj.__class__, DeclarativeMeta):
            # an SQLAlchemy class
            fields = {}
            for field in [x for x in dir(obj) if
                          not x.startswith('_') and x != 'metadata']:
                # Loop through all the object's attributes, excluding
                # private attributes and the 'metadata' attribute

                data = obj.__getattribute__(field)
                try:
                    json.dumps(data)  # this will fail on non-encodable values, like other classes
                    fields[field] = data
                except TypeError:
                    # If the attribute can't be directly encoded to JSON,
                    # set its value to None
                    fields[field] = None
            # a json-encodable dict
            return fields

        return json.JSONEncoder.default(self, obj)
        # If the object is not an SQLAlchemy declarative base class,
        # use the default JSONEncoder behavior
