from flask import Blueprint
from flask_restful import Api
from .controller.index_ct import IndexController

admin_blueprint =  Blueprint('admin', __name__, template_folder="templates", url_prefix="/admin") # /api
admin = Api(admin_blueprint)

admin.add_resource(IndexController, '/')