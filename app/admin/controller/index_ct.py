from flask import request

class IndexController():
  def get_index():
    
    return {"msg":"API Index OK"}

  def get_about():

    if request.method == "POST":
      return {"msg":"API ABOUT POST OK"}

    return {"msg":"API ABOUT GET OK"}