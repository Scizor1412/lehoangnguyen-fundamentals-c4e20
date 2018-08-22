from mongoengine import *

class Service(Document):
    #Document là từ khóa cố định, Service là tên biến, đặt thế nào cũng được
    name = StringField()
    yob = IntField()
    gender = IntField()
    height = IntField()
    phone = StringField()
    address = StringField()
    status = BooleanField()
