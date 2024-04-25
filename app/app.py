#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
from flask import Flask, request
from flask_jwt_extended import JWTManager
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import safe_str_cmp, generate_password_hash, check_password_hash

# Initialize app and config
app = Flask(__name__)
# Load app settings
app.config.from_object(os.environ['APP_SETTINGS'])
# Disable tracking modifications
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# Initialize app with JWT
app.config['JWT_SECRET_KEY'] = 'super-secret'  # Replace this with your own secret key
jwt = JWTManager(app)
# Initialize app with RESTful API
api = Api(app)

# Database setup
db = SQLAlchemy(app)

# Import resources
from resources.item import ItemResource
from resources.item_list import ItemListResource
from resources.user_register import UserRegisterResource
from resources.resource import Resource
from resources.user_login import UserLoginResource
from resources.store.store import StoreResource
from resources.store.store_list import StoreListResource

# Add resources to API
api.add_resource(ItemResource, '/item/<string:name>')
api.add_resource(ItemListResource, '/items')
api.add_resource(UserRegisterResource, '/register')
api.add_resource(UserLoginResource, '/login')
api.add_resource(StoreResource, '/store/<string:name>')
api.add_resource(StoreListResource, '/stores')

# Before first request
@app.before_first_request
def create_tables():
    try:
        db.create_all()
    except sqlalchemy.exc.SQLAlchemyError as e:
        print(f"Error creating tables: {e}")

# JWT authentication
@jwt.user_loader
def load_user(id):
    # ...

# Run app
if __name__ == '__main__':
    app.run(debug=True)


from flask_restful import Resource
from models.item import ItemModel
from schemas.item import ItemSchema

item_schema = ItemSchema()
items_schema.many = True  # Allow serialization of multiple items

class ItemResource(Resource):
    """
    Resource for managing items
    """
    def get(self, name):
        """
        Get an item by name
        :param name: Name of the item
        :return: Item object or 404 error
        """
        item = ItemModel.find_by_name(name)
        if item:
            return item_schema.jsonify(item)
        return {"message": "Item not found"}, 404

    def post(self, name):
        """
        Create a new item
        :param name: Name of the item
        :return: Created item or 404 error
        """
        if Item.find_by_name(name):
            return {"message": "An item with this name already exists"}, 404

        data = item_schema.load(request.get_json())
        item = ItemModel.new(name, **data)
        db.create(item)
        return item_schema.jsonify(item), 201

    def delete(self, name):
        """
        Delete an item by name
        :param name: Name of the item
        :return: Deleted item or 404 error
        """
        item = ItemModel.find_by_name(name)
        if not item:
            return {"message": "Item not found"}, 404

        db.delete(item)
        return item_schema.jsonify(item)

    def put(self, name):
        """
        Update an item by name
        :param name: Name of the item
        :return: Updated item or 404 error
        """
        data = item_schema.load(request.get_json())
        item = ItemModel.find_by_name(name)

        if not item:
            if ItemModel.find_by_name(data["name"]):
                return {"message": "An item with this name already exists"}, 400
            item = ItemModel.new(name, **data)
        else:
            item.update(**data)

        db.create(item)
        return item_schema.jsonify(item)
