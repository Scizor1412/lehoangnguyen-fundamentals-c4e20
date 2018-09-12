from models.service import Service
import mlab

mlab.connect()

id_to_find = "5b7820e0533b451810746e01"

# hera = Service.objects(id = id_to_find) # [Service obj]
# hera = Service.objects.get(id=id_to_find) # Service obj
service = Service.objects.with_id(id_to_find) # Service obj

if service is not None:
    # service.delete()
    # print ("Deleted")
    print ("Before: ")
    print (service.to_mongo())
    service.update(set__yob=2002, set__name = "Quan", set__gender = 0)
    service.reload()
    print ("After: ")
    print (service.to_mongo())
else:
    print ("Not found")

#connect
## mlab.py
#design
## class Service(Document): tên class viết hoa chữ đầu
#CRUD
## Read
#form
# post
#put sửa 1 doc
# patch sửa 1 phần
# delete
# pre flight thăm dò

#input
#set default input value
#radio button