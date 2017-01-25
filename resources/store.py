from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from models.item import ItemModel
from models.store import StoreModel

#Flask restful jsonifies stuff for us
# student class inherits from Resource


class Store(Resource):
    TABLE_NAME = 'stores'

    parser = reqparse.RequestParser()
    parser.add_argument('name',
                        type=str,
                        required=True,
                        help="This field cannot be blank"
                        )
    # parser.add_argument('store_id',
    #                     type=int,
    #                     required=True,
    #                     help="Every Item Needs a Store ID, yo"
    #                     )
    @jwt_required()
    def get(self, name):
        store = StoreModel.find_by_name(name)
        if store:
            return store.json()
        return {'message': 'Store not found'}, 404

    def post(self, name):
        if StoreModel.find_by_name(name):
            return {'message': "A store with name '{}' already exists.".format(name)}, 400

        data = Store.parser.parse_args()

        #item = {'name': name, 'price': data['price']}
        store = StoreModel(name, **data)

        try:
            store.save_to_db()
        except:
            return {"message": "An error occurred inserting the store."}, 500

        return store.json(), 201

    def delete(self, name):
        item = ItemModel.find_by_name(name)
        if item:
            item.delete_from_db()

        return {'message': 'Item deleted'}

class StoreList(Resource):
    TABLE_NAME = 'stores'

    def get(self):
        return {'items': [item.json() for item in ItemModel.query.all()]}
            #{'items': ItemModel.query.all().json()}
