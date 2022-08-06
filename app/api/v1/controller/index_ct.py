from unittest import result
from flask import request
from ..service.user_service import Users_Service

class IndexController():
  def get_index():
    
    result = Users_Service.get_user()
    print(result)
    return {"msg":"API Index OK"}

  def get_about():
    if request.method == "POST":
      username = "TuanLA"
      age = 35
      Users_Service.add_user(username, age)
      return {"msg":"API ABOUT POST OK"}

    if request.method == "DELETE":
      username = "TuanLA"
      Users_Service.delte_user_by_username(username)
      return {"msg":"API ABOUT DELETE OK"}

    if request.method == "PUT":
      oldusername = "TuanLA"
      username = "TuanLA21"
      Users_Service.update_username(oldusername, username)
      return {"msg":"API ABOUT PUT OK"}

    return {"msg":"API ABOUT GET OK"}
  
  