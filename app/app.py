project/
│
├── __init__.py
├── app.py
└── resources/
    ├── __init__.py
    ├── item.py
    ├── store.py
    ├── user.py
    └── user_register.py


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
app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
jwt = JWTManager(app)
api = Api(app)

# Database setup
db = SQLAlchemy(app)

# Resources
class ItemResource(Resource):
    # ...

class ItemListResource(Resource):
    # ...

class UserRegisterResource(Resource):
    # ...

class UserResource(Resource):
    # ...

class StoreResource(Resource):
    # ...

class StoreListResource(Resource):
    # ...

# Add resources to API
api.add_resource(ItemResource, '/item/<string:name>')
api.add_resource(ItemListResource, '/items')
api.add_resource(UserRegisterResource, '/register')
api.add_resource(UserResource, '/user')
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
from models import ItemModel
from schemas import ItemSchema

item_schema = ItemSchema()
items_schema = ItemSchema(many=True)

class ItemResource(Resource):
    def get(self, name):
        item = ItemModel.find_by_name(name)
        if item:
            return item_schema.jsonify(item)
        return {"message": "Item not found"}, 404

    def post(self, name):
        if ItemModel.find_by_name(name):
            return {"message": "An item with this name already exists"}, 400

        data = item_schema.load(request.get_json())
        item = ItemModel.new(name, **data)
        db.create(item)
        return item_schema.jsonify(item), 201

    def delete(self, name):
        item = ItemModel.find_by_name(name)
        if not item:
            return {"message": "Item not found"}, 404

        db.delete(item)
        return item_schema.jsonify(item)

    def put(self, name):
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
