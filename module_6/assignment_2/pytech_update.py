# Erika Vanderhoff
# csd-310
# Assignment 6.2
# 4/11/2022

from pymongo import MongoClient

#Connecting to MongoDB database
url = "mongodb+srv://admin:admin@cluster0.h2zva.mongodb.net/pytech?retryWrites=true&w=majority"
client = MongoClient(url)
db = client.pytech

#Calling the find function and displaying each student
docs = db.students.find({})

print("-- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")
for doc in docs:
   print(doc)
   print("")

#Updating last name of student with id of 1007
result = db.students.update_one({"student_id": "1007"}, {"$set": {"last_name": "Valteck"}})

#Calling the find_one function and printing the updated students data
print("-- DISPLAYING STUDENT DOCUMENT FROM find_one() QUERY --")
doc = db.students.find_one({"student_id": "1007"})
print(doc)