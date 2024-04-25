#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from app.db import db

class ItemModel(db.Model):
    __tablename__ = 'items'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    price = db.Column(db.Numeric(10, 2))

    def serialize(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns if c.name != 'id'}

