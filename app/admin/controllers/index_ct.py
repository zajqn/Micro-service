from flask import render_template, Response

class IndexAdminController():
  def get_index():
    return Response(render_template("index.html"))