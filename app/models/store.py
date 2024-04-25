#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from app.db import db

class StoreModel(db.Model):
    """Store model for storing store information in the database."""

    __tablename__ = 'stores'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)

    def __repr__(self):
        """Provide a human-readable representation of the StoreModel object."""
        return f'<StoreModel id={self.id} name={self.name}>'
