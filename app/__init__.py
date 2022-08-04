import os
from flask import Flask
from .config import config_by_name
from .api import api
from .admin import admin

def create_app():
  app = Flask(__name__, instance_relative_config=True)

  if os.environ.get('FLASK_ENV') == "dev":
    print("Enviroment: {}".format("dev"))
    app.config.from_object(config_by_name["dev"])
  elif os.environ.get('FLASK_ENV') == "test":
    print("Enviroment: {}".format("test"))
    app.config.from_object(config_by_name["test"])
  else:
    print("Enviroment: {}".format("prod"))
    app.config.from_object(config_by_name["prod"])

  app.register_blueprint(api.api_blueprint)
  app.register_blueprint(admin.admin_blueprint)

  @app.errorhandler(404)
  def handle_bad_request(e):
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
