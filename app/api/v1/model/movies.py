from mongoengine import *

class Movies(Document):
  title = StringField()
  type = StringField()
  year = IntField()
  meta = {
    'collecttion': 'movies'
  }