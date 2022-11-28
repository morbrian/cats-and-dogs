from flask_restx import Api 

from .cats import api as cats
from .dogs import api as dogs

api = Api(
    title='Sample Data Services',
    version='1.0',
    description='Simple sandbox services to help try out development ideas',
    # All API metadatas
)

api.add_namespace(cats)
api.add_namespace(dogs)