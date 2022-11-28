from flask_restx import Namespace, Resource, fields
from flask import request, json
from .database import Database

api = Namespace('cats', description='Cats related operations')

cat_model_template = {
    'id': fields.String(required=True, description='The cat identifier'),
    'name': fields.String(required=True, description='The cat name'),
    'color': fields.String(required=True, description='The cat color'),
}
cat = api.model('Cat', cat_model_template)

seed_data = {
    'felix': {'id': 'felix', 'name': 'Felix', 'color': 'gray'},
    'chloe': {'id': 'chloe', 'name': 'Chloe', 'color': 'blue'},
    'henry': {'id': 'henry', 'name': 'Henry', 'color': 'orange'},
}
database = Database(seed_data)

@api.route('/')
class CatList(Resource):
    @api.doc('list_cats')
    @api.marshal_list_with(cat)
    def get(self):
        '''List all cats'''
        return database.records()

    @api.doc('put_cats')
    @api.doc(body=[cat])
    @api.marshal_with(cat)
    def put(self):
        '''Create or replace specified cats'''
        data = json.loads(request.data)
        stored = list(map(lambda d: database.store(None, d), data))
        return stored


@api.route('/<id>')
@api.param('id', 'The cat identifier')
@api.response(404, 'Cat not found')
class Cat(Resource):
    @api.doc('get_cat')
    @api.marshal_with(cat)
    def get(self, id):
        '''Fetch a cat given its identifier'''
        cat = database.fetch(id)
        if cat is not None:
            return cat
        api.abort(404)

    @api.doc('put_cat')
    @api.doc(body=cat)
    @api.marshal_with(cat)
    def put(self, id):
        '''Put cat data for given identifier'''
        data = json.loads(request.data)
        if id is not None:
            saved =  database.store(id, data)
            if saved is not None:
                return saved
        api.abort(400, 'id not specified')


    @api.doc('delete_cat')
    def delete(self, id):
        '''Delete cat data for given identifier'''
        cat = database.delete(id)
        if cat is not None:
            return cat
        api.abort(404)