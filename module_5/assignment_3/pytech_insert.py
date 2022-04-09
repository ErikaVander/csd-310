# Erika Vanderhoff
# csd-310
# Assignment 5.3.1
# 4/8/2022

from pymongo import MongoClient

url = "mongodb+srv://admin:admin@cluster0.h2zva.mongodb.net/pytech?retryWrites=true&w=majority"
client = MongoClient(url)
db = client.pytech

fred = {
   "student_id": "1007",
   "first_name": "Fred",
   "last_name": "Commons"
}
thorin = {
   "student_id": "1008",
   "first_name": "Thorin",
   "last_name": "Oakenshield"
}
bilbo = {
   "student_id": "1009",
   "first_name": "Bilbo",
   "last_name": "Baggins"
}

fred_student_id = db.students.insert_one(fred).inserted_id
thorin_student_id = db.students.insert_one(thorin).inserted_id
bilbo_student_id = db.students.insert_one(bilbo).inserted_id

print()
print("-- INSERT STATEMENTS --")
print("Inserted student record "+ fred["first_name"] + " " + fred["last_name"] + " into the students collection with document_id " + str(fred_student_id))
print("Inserted student record "+ thorin["first_name"] + " " + thorin["last_name"] + " into the students collection with document_id " + str(thorin_student_id))
print("Inserted student record "+ bilbo["first_name"] + " " + bilbo["last_name"] + " into the students collection with document_id " + str(bilbo_student_id))
print()