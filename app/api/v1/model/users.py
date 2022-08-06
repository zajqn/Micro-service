from mongoengine import *

class Users(Document):
  username = StringField()
  age = IntField()
  meta = {
    'collecttion': 'users'
  }