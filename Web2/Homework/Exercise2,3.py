import mlab
from service import Service
from mongoengine import *
import bson

mlab.connect()

search_id = "5b781ea9533b450a00c34bdc"

search_object = Service.objects.get (id = "5b781ea9533b450a00c34bdc")

search_object.delete()