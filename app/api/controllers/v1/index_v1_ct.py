from flask import request

class IndexV1Controller():
  def get_index():
    return {'msg':'API V1'}
