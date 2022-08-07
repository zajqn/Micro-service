from flask_restful import Resource
from ..service.user_service import Users_Service


class IndexController(Resource):
  def get(self):
    data = Users_Service.get_user()
    print(data)
    return {'msg':'get v1 index'}

  def post(self):
    return {'msg':'post v1 index'}
  
  def put(self):
    return {'msg':'put v1 index'}