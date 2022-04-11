# Erika Vanderhoff
# csd-310
# Assignment 6.3
# 4/11/2022

from pymongo import MongoClient

url = "mongodb+srv://admin:admin@cluster0.h2zva.mongodb.net/pytech?retryWrites=true&w=majority"
client = MongoClient(url)
db = client.pytech

docs = db.students.find({})

print("-- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")
for docu in docs:
   print(docu)
   print("")

jim = {
   "student_id": "1010",
   "first_name": "Jim",
   "last_name": "Elliot"
}

jim_student_id = db.students.insert_one(jim).inserted_id

print()
print("-- INSERT STATEMENTS --")
print("Inserted student record "+ jim["first_name"] + " " + jim["last_name"] + " into the students collection with document_id " + str(jim_student_id))

doc = db.students.find_one({"student_id": "1010"})
print()
print("-- DISPLAYING STUDENT TEST DOC --")
print(doc)

db.students.delete_one({"student_id": "1010"})

docs = db.students.find({})

print()
print("-- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")
for docu in docs:
   print(docu)
   print("")