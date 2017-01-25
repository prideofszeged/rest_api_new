from flask import Flask
from flask_jwt import JWT
from flask_restful import Api

from resources.store import StoreList, Store
from resources.item import Item, ItemList
from resources.user import UserRegister
from security import authenticate, identity


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = '11223344'
api = Api(app)

@app.before_first_request
def create_tables():
    """
    Creates tables before first request if they don't exist
    """
    db.create_all()

jwt = JWT(app, authenticate, identity)

api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')
api.add_resource(UserRegister, '/register')
api.add_resource(Store, '/store/<string:name>')
api.add_resource(StoreList, '/stores')



if __name__ == '__main__':
    from db import db
    # because of circular imports
    db.init_app(app)
    #app.run(port=4995, debug=True)  # important to mention debug=True
    app.run(port=5000, debug=True)  # important to mention debug=True