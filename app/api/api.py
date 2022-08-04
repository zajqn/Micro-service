from flask import Blueprint

from .controllers.index_ct import IndexAPIController
from .controllers.v1.index_v1_ct import IndexV1Controller
from .controllers.v2.index_v2_ct import IndexV2Controller

api_blueprint = Blueprint('api', __name__, url_prefix='/api')
api_v1_blueprint = Blueprint('api v1', __name__, url_prefix='/v1')
api_v2_blueprint = Blueprint('api v2', __name__, url_prefix='/v2')

api_blueprint.register_blueprint(api_v1_blueprint)
api_blueprint.register_blueprint(api_v2_blueprint)

# Routing for API
api_blueprint.add_url_rule("/", view_func=IndexAPIController.get_index)
api_blueprint.add_url_rule("/about", view_func=IndexAPIController.get_about, methods=["GET", "POST", "DELETE"])
# Routing for Children API | V1
api_v1_blueprint.add_url_rule("/", view_func=IndexV1Controller.get_index)
# Routing for Children API | V2
api_v2_blueprint.add_url_rule("/", view_func=IndexV2Controller.get_index)