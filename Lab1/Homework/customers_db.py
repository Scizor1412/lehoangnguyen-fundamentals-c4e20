from pymongo import MongoClient
import matplotlib
matplotlib.use("tkAgg")
from matplotlib import pyplot

mongo_uri = "mongodb://admin:admin@ds021182.mlab.com:21182/c4e"

client = MongoClient(mongo_uri)

db = client.get_default_database()

customers = db["customers"]

ads = customers.find({"ref": "ads"}).count()
events = customers.find({"ref": "events"}).count()
word_of_mouth = customers.find({"ref": "wom"}).count()

print (ads)
print (events)
print (word_of_mouth)
# robo 3t
labels = ["ads", "events", "word_of_mouth"]
values = [1938, 3900, 1131]
colors = ["red", "blue", "black"]

pyplot.pie(
    values,
    labels = labels,
    colors = colors
)

pyplot.axis = ("equal")

pyplot.show()