from flask import Blueprint
from flask_restful import Api
from .controller.index_ct import IndexController

api_v1_blueprint =  Blueprint('api v1', __name__, url_prefix="/v1")
api = Api(api_v1_blueprint)

api.add_resource(IndexController, '/')