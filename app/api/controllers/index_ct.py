from flask import request

class IndexAPIController():
  def get_index():
    return {'msg':'Index API Controller'}

  def get_about():
    if request.method == "POST":
        return {'msg':'POST About API'}
    if request.method == "DELETE":
        return {'msg':'DELETE About API'}
        
    return {'msg':'GET About API'}