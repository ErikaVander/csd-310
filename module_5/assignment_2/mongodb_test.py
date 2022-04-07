# Erika Vanderhoff
# csd-310
# Assignment 5.2
# 4/6/2022

from pymongo import MongoClient

url = "mongodb+srv://admin:admin@cluster0.h2zva.mongodb.net/pytech?retryWrites=true&w=majority"
client = MongoClient(url)
db = client.pytech

print("-- Pytech Collection List --")
print(db.list_collection_names())