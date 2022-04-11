# Erika Vanderhoff
# csd-310
# Assignment 6.3
# 4/11/2022

from pymongo import MongoClient

#Linking to MongoDB database
url = "mongodb+srv://admin:admin@cluster0.h2zva.mongodb.net/pytech?retryWrites=true&w=majority"
client = MongoClient(url)
db = client.pytech

#Creating a find() function because these lines of code are used twice
def find():
   #Finding the students collection and storing it in variable docs
   docs = db.students.find({})

   #Printing all students with for loop
   print()
   print("-- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")
   for docu in docs:
      print(docu)
      print("")

#Calling the find() function
find()

#Creating a new object, jim
jim = {
   "student_id": "1010",
   "first_name": "Jim",
   "last_name": "Elliot"
}

#Adding jim to the students collection
jim_student_id = db.students.insert_one(jim).inserted_id

#Letting the user know that jim has been added to the database
print()
print("-- INSERT STATEMENTS --")
print("Inserted student record "+ jim["first_name"] + " " + jim["last_name"] + " into the students collection with document_id " + str(jim_student_id))

#Finding jim and printing out his data
doc = db.students.find_one({"student_id": "1010"})
print()
print("-- DISPLAYING STUDENT TEST DOC --")
print(doc)

#Deleting jim
db.students.delete_one({"student_id": "1010"})

#Calling the find() function
find()