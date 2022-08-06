from flask import Blueprint
from .controller.index_ct import IndexController

# Blueprint /admin
admin_blueprint = Blueprint('admin', __name__, template_folder="templates", url_prefix="/admin")


# Rule route
admin_blueprint.add_url_rule("/", view_func=IndexController.get_index)
admin_blueprint.add_url_rule("/about", view_func=IndexController.get_about, methods=["GET", "POST"])