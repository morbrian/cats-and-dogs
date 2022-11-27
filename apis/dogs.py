from flask_restx import Namespace, Resource, fields
from flask import request, json

api = Namespace('dogs', description='Dogs related operations')

dog = api.model('Dog', {
    'id': fields.String(required=True, description='The dog identifier'),
    'name': fields.String(required=True, description='The dog name'),
    'color': fields.String(required=True, description='The dog color'),
})

DOGS = {
    'gracie': {'id': 'gracie', 'name': 'Gracie', 'color': 'black-tan'},
    'marge': {'id': 'marge', 'name': 'Marge', 'color': 'blonde'},
    'piper': {'id': 'piper', 'name': 'Piper', 'color': 'black'},
}

@api.route('/')
class DogList(Resource):
    @api.doc('list_dogs')
    @api.marshal_list_with(dog)
    def get(self):
        '''List all dogs'''
        return list(DOGS.values())

@api.route('/<id>')
@api.param('id', 'The dog identifier')
@api.response(404, 'Dog not found')
class Dog(Resource):
    @api.doc('get_dog')
    @api.marshal_with(dog)
    def get(self, id):
        '''Fetch a dog given its identifier'''
        dog = DOGS[id]
        if dog is not None:
            return dog
        api.abort(404)

    @api.doc('put_dog')
    @api.doc(body=dog)
    @api.marshal_with(dog)
    def put(self, id):
        '''Put dog data for given identifier'''
        data = json.loads(request.data)
        if (id is not None):
            data['id'] = id
            DOGS[id] = data
            return data
        api.abort(400, 'id not specified')


    @api.doc('delete_dog')
    def delete(self, id):
        '''Delete dog data for given identifier'''
        dog = DOGS.get(id)
        if dog is not None:
            DOGS.pop(id)
            return dog
        api.abort(404)