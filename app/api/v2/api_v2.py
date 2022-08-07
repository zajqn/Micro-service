from flask import Blueprint
from flask_restful import Api
from .controller.index_ct import IndexController

api_v2_blueprint =  Blueprint('api v2', __name__, url_prefix="/v2")
api = Api(api_v2_blueprint)

api.add_resource(IndexController, '/')