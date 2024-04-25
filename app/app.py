#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
from flask import Flask, request
from flask_jwt_extended import JWTManager
from flask_restful import Api, Resource, reqparse
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import safe_str_cmp, generate_password_hash, check_password_hash

# Initialize app and config
app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
jwt = JWTManager(app)
api = Api(app)

# Database setup
db = SQLAlchemy(app)

# Resources
class Item(Resource):
    # ...

class ItemList(Resource):
    # ...

class UserRegister(Resource):
    # ...

class User(Resource):
    # ...

class Store(Resource):
    # ...

class StoreList(Resource):
    # ...

# Add resources to API
api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')
api.add_resource(UserRegister, '/register')
api.add_resource(User, '/user')
api.add_resource(Store, '/store/<string:name>')
api.add_resource(StoreList, '/stores')

# Before first request
@app.before_first_request
def create_tables():
    db.create_all()

# JWT authentication
@jwt.user_loader
def load_user(id):
    # ...

# Run app
if __name__ == '__main__':
    app.run(debug=True)
