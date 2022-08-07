from flask_restful import Resource


class IndexController(Resource):
  def get(self):
    return {'msg':'get admin index'}

  def post(self):
    return {'msg':'post admin index'}
  
  def put(self):
    return {'msg':'put admin index'}