from flask import Blueprint
from .v1.api_v1 import api_v1_blueprint
from .v2.api_v2 import api_v2_blueprint



api_blueprint =  Blueprint('api', __name__, url_prefix="/api") # /api
api_blueprint.register_blueprint(api_v1_blueprint) # /api/v1
api_blueprint.register_blueprint(api_v2_blueprint) # /api/v2

