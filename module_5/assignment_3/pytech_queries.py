# Erika Vanderhoff
# csd-310
# Assignment 5.3.2
# 4/8/2022

from pymongo import MongoClient

#Connecting to MongoDB
url = "mongodb+srv://admin:admin@cluster0.h2zva.mongodb.net/pytech?retryWrites=true&w=majority"
client = MongoClient(url)
db = client.pytech

#Calling find and storing data in docs variable
docs = db.students.find({})

#Printing each student in docs using for loop
print("-- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")
for doc in docs:
   print(doc)
   print("")

#Calling find_one, storing data in doc variable and printing doc
print("-- DISPLAYING STUDENT DOCUMENT FROM find_one() QUERY --")
doc = db.students.find_one({"student_id": "1007"})
print(doc)