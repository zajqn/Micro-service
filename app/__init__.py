from flask import Flask, request
from flask_mongoengine import MongoEngine

from .api import api
from .admin import admin

def create_app():
  app = Flask(__name__)
  app.config.from_pyfile('config.cfg')
  
  # Register Blueprint
  app.register_blueprint(api.api_blueprint) # /api
  app.register_blueprint(admin.admin_blueprint) # /admin
 
  db = MongoEngine(app)

  @app.errorhandler(404)
  def handle_bad_request(e):
    if request.path.startswith('/api/'):
      return {'msg':'API Not found'}, 404
    return {'msg':'Not found'}, 404

  @app.errorhandler(405)
  def handle_method(e):
    return {'msg':'Method not allowed'}, 405
  
  @app.errorhandler(403)
  def handle_permission(e):
    return {'msg':'Forbidden'}, 403
  
  @app.errorhandler(Exception)
  def handle_unknow_error(e):
    return {'msg':'Unknown Error'}, 520

  return app