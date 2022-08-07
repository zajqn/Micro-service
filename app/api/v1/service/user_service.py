from ..model import user_model

class Users_Service():
  def get_user():
    data = user_model.Users.objects.to_json()
    return data
  
  def add_user(username, age):
    if username and age:
      user_model.Users(username = username, age = age).save()
    return {"msg":"Add user OK"}
  
  def delte_user_by_username(username):
    if username:
      user_model.Users.objects(username = username).first().delete()
    return {"msg":"Delete user by username OK"}
  
  def update_username(oldusername, username):
    if username:
      user = user_model.Users.objects(username = oldusername)
      user.update(username = username)
    return {"msg":"Update user by username OK"}