from ..model import users, movies

class Users_Service():
  def get_user():
    result = users.Users.objects.to_json()
    return result

  def add_user(username, age):
    if username and age:
      users.Users(username = username, age = age).save()
    return {"msg":"Add user OK"}
  
  def delte_user_by_username(username):
    if username:
      users.Users.objects(username = username).first().delete()
    return {"msg":"Delete user by username OK"}