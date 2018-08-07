from pymongo import MongoClient

mongo_uri = "mongodb://admin:admin@ds021182.mlab.com:21182/c4e"

client = MongoClient(mongo_uri)

db = client.get_default_database()

posts = db["posts"]

new_post = {
    "title": "An advice for anyone",
    "author": "Scizor",
    "content": "'Never give up on your dream', for whatever it means."
}

posts.insert_one(new_post)