from flask import request

class IndexV2Controller():
  def get_index():
    return {'msg':'API V2'}
