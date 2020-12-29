from flask_restful import Resource, reqparse
from flask_jwt import jwt_required

from models.store import StoreModel

class Store(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('name',
        type=str,
        required=True,
        help="This field cannot be left blank"
    )

    @jwt_required()
    def get(self,name):
        store = StoreModel.find_by_name(name)
        if store:
            return store.json()
        
        return {"message" : "Store not Found"} , 404

    @jwt_required()
    def post(self, name):
        if StoreModel.find_by_name(name):
            return {'message': "A Store with name '{}' already exists.".format(name)}

        store = StoreModel(name)

        try:
            store.save_to_db()
        except:
            return {"message": "An error occurred inserting the item."}, 500

        return store.json()

    @jwt_required()
    def delete(self,name):

        store = StoreModel.find_by_name(name)

        if store:
            store.delete_from_db()
            return {"message" : f"Store {name} Deleted"}, 200            

        return {"message" : f"Store {name} Not Found"}, 404


class StoreList(Resource):

    @jwt_required()
    def get(self):
        return {"stores" : [store.json() for store in StoreModel.find_all()]}, 200