from mongoengine import *

class Order(Document):
    service_id = StringField()
    user_id = StringField()
    time = StringField()
    is_accepted = BooleanField()