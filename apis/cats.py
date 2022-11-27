from flask_restx import Namespace, Resource, fields
from flask import request, json

api = Namespace('cats', description='Cats related operations')

cat = api.model('Cat', {
    'id': fields.String(required=True, description='The cat identifier'),
    'name': fields.String(required=True, description='The cat name'),
    'color': fields.String(required=True, description='The cat color'),
})

CATS = {
    'felix': {'id': 'felix', 'name': 'Felix', 'color': 'gray'},
    'chloe': {'id': 'chloe', 'name': 'Chloe', 'color': 'blue'},
    'henry': {'id': 'henry', 'name': 'Henry', 'color': 'orange'},
}

@api.route('/')
class CatList(Resource):
    @api.doc('list_cats')
    @api.marshal_list_with(cat)
    def get(self):
        '''List all cats'''
        return list(CATS.values())

@api.route('/<id>')
@api.param('id', 'The cat identifier')
@api.response(404, 'Cat not found')
class Cat(Resource):
    @api.doc('get_cat')
    @api.marshal_with(cat)
    def get(self, id):
        '''Fetch a cat given its identifier'''
        cat = CATS[id]
        if cat is not None:
            return cat
        api.abort(404)

    @api.doc('put_cat')
    @api.doc(body=cat)
    @api.marshal_with(cat)
    def put(self, id):
        '''Put cat data for given identifier'''
        data = json.loads(request.data)
        if (id is not None):
            data['id'] = id
            CATS[id] = data
            return data
        api.abort(400, 'id not specified')


    @api.doc('delete_cat')
    def delete(self, id):
        '''Delete cat data for given identifier'''
        cat = CATS.get(id)
        if cat is not None:
            CATS.pop(id)
            return cat
        api.abort(404)