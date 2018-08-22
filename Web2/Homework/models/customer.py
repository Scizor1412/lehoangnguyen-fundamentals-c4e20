from mongoengine import *

class Customer(Document):
    #Document là từ khóa cố định, Service là tên biến, đặt thế nào cũng được
    name = StringField()
    yob = IntField()
    gender = IntField()
    height = IntField()
    phone = StringField()
    address = StringField()
    email = StringField()
    job = StringField()
    company = StringField()