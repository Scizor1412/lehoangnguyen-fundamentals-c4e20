from models.service import Service
import mlab

mlab.connect()

all_service = Service.objects(id = "5b781ea9533b450a00c34bdc")

# first_service = all_service[0]

print (all_service)