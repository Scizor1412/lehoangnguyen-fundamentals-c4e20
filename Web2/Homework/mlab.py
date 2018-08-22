import mongoengine

#mongodb://<dbuser>:<dbpassword>@ds123822.mlab.com:23822/muadongkhonglanh

host = "ds123822.mlab.com"
port = 23822
db_name = "muadongkhonglanh"
user_name = "muadongkhonglanh-Scizor"
password = "Firepower*1995"


def connect():
    mongoengine.connect(
        db_name,
        host=host, 
        port=port, 
        username=user_name, 
        password=password)