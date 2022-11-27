from flask_restx import Api 

from .cats import api as cats
from .dogs import api as dogs

api = Api(
    title='My Title',
    version='1.0',
    description='A description',
    # All API metadatas
)

api.add_namespace(cats)
api.add_namespace(dogs)