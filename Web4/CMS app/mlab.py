import mongoengine
# mongodb://<dbuser>:<dbpassword>@ds237072.mlab.com:37072/cmsapp


db_name='cmsapp'
username = 'Scizor'
password = 'firepower1995'
host = 'ds237072.mlab.com'
port = 37072
def connect():
    mongoengine.connect(
    db_name,
    username = username,
    password = password,
    host = host,
    port = port)