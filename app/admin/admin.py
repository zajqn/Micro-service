from flask import Blueprint
from .controllers.index_ct import IndexAdminController

admin_blueprint = Blueprint('admin', __name__, template_folder='templates', url_prefix='/admin')

# Routing for Admin 
admin_blueprint.add_url_rule("/", view_func=IndexAdminController.get_index)