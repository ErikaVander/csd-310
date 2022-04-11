# Erika Vanderhoff
# csd-310
# Assignment 6.2
# 4/11/2022

from pymongo import MongoClient

url = "mongodb+srv://admin:admin@cluster0.h2zva.mongodb.net/pytech?retryWrites=true&w=majority"
client = MongoClient(url)
db = client.pytech

docs = db.students.find({})

print("-- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")
for doc in docs:
   print(doc)
   print("")

result = db.students.update_one({"student_id": "1007"}, {"$set": {"last_name": "Valteck"}})

print("-- DISPLAYING STUDENT DOCUMENT FROM find_one() QUERY --")
doc = db.students.find_one({"student_id": "1007"})
print(doc)