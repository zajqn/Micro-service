from flask import request
from flask_restful import Resource

class IndexController(Resource):
  def get(self):
    return {'msg':'get v2 index'}

  def post(self):
    return {'msg':'post v2 index'}
  
  def put(self):
    return {'msg':'put v2 index'}