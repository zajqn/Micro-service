from flask import Blueprint
from .v1.controller.index_ct import IndexController

# Blueprint /api
api_blueprint = Blueprint('api', __name__, url_prefix="/api")
api_v1_blueprint = Blueprint('api', __name__, url_prefix="/v1")

api_blueprint.register_blueprint(api_v1_blueprint)

# Rule route
api_v1_blueprint.add_url_rule("/", view_func=IndexController.get_index)
api_v1_blueprint.add_url_rule("/about", view_func=IndexController.get_about, methods=["GET", "POST"])