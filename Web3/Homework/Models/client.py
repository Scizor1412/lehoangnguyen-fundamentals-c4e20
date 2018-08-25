from mongoengine import *

class Client(Document):
    name = StringField()
    yob = IntField()
    job = StringField()
    phone = StringField()
    company = StringField()
    height = IntField()
    address = StringField()
    status = BooleanField()
    description = ListField()
    image = ImageField()
    measurements = ListField()