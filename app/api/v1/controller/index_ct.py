from flask import request
from ..model import users, movies

class IndexController():
  def get_index():
    for user in users.Users.objects():
      print('user.username', user.username)

    for movie in movies.Movies.objects():
      print('movie.title', movie.title)

    return {"msg":"API Index OK"}

  def get_about():

    if request.method == "POST":
      return {"msg":"API ABOUT POST OK"}

    return {"msg":"API ABOUT GET OK"}