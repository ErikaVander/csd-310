#Erika Vanderhoff
#csd 310
#assignment_12.3
#5/13/2022

from sqlite3 import Cursor
from tkinter import Menu
from tkinter.tix import Select
from tokenize import String
from venv import create
from wsgiref import validate
import mysql.connector
from mysql.connector import errorcode

#creating user object to use to connect to mysql.pysports
config = {
   "user": "whatabook_user",
   "password": "MySQL8IsGreat!",
   "host": "localhost",
   "database": "whatabook",
   "raise_on_warnings": True 
}

# try connecting otherwise print error messages
try:
   db = mysql.connector.connect(**config)

   print("\n   Database user {} connected to MySQL on host {} with database {}".format(config["user"], config["host"], config["database"]))

except mysql.connector.Error as err:
   if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
      print("  The supplied username or password are invalid")

   elif err.errno == errorcode.ER_BAD_DB_ERROR:
      print("  The specified database does not exist\n")

   else:
      print(err)

#create cursor object
cursor = db.cursor()

#create class whatABook
class whatABook :
   #keep track of current navigation status
   navigation : String = "main menu"
   #keep track of current user_id
   user_id : String = ""
   #keep track of current book_id
   book_id : String = ""
   #prompt user to select a course of action
   def promptUser(self) :
      #if current navigation status == main menu, prompt user to select command from main menu
      if self.navigation == "main menu": 
         print("\n\n         --------Main Menu--------")
         userNavInput = input("\nType one of these numbers and press enter: \n   1. view books      -> view a list of our books\n   2. store location  -> view store's location and hours\n   3. my account      -> login to view and use your wishlist\n   4. exit            -> exit the program\n")

         #if statements to determine course of action based on user input
         if userNavInput == "1":
            self.show_books(cursor)
         elif userNavInput == "2":
            self.show_locations(cursor)
         elif userNavInput == "3":
            self.validate_user(cursor)
         elif userNavInput == "4":
            print("\nexiting the program\nhave a nice day...")
            return
         #if user doesn't make valid input tell them and prompt them to press enter to return to main menu
         else:
            print("\nInvalid input, please try again")
            input("Press Enter to continue...")
            self.promptUser()

      #if current navigation status == my account which can only happen once a user logs in, prompt user to select command from wishlist menu
      elif self.navigation == "my account":
         print("\n\n         --------Wishlist Menu--------")
         userNavInput = input("\nType one of these numbers and press enter: \n   1. view wishlist   -> view a list of the books in your wishlist\n   2. add book        -> add a book to your wishlist\n   3. main menu       -> go back to the main menu\n   4. exit            -> exit the program\n")

         #if statements to determine course of action based on user input
         if userNavInput.lower() == "1":
            self.show_wishlist(cursor, self.user_id)
         elif userNavInput.lower() == "2":
            self.show_books_to_add(cursor, self.user_id)
         elif userNavInput.lower() == "3":
            self.navigation = "main menu"
            self.promptUser()
         elif userNavInput.lower() == "4":
            print("\nexiting the program\nhave a nice day...")
            return
         #if user doesn't make valid input tell them and prompt them to press enter to return to wishlist menu
         else:
            print("\nInvalid input, please try again")
            input("Press Enter to continue...")
            self.promptUser()

   def show_books(self, _cursor) :
      #use select statement to get specific info from table book
      _cursor.execute("SELECT book.book_name, book.author, book.description FROM book")
      #fetchall that info and store in var books
      books = _cursor.fetchall()
      #print info
      print("\n---WhatABook books---")
      for book in books :
         print("\n" + book[0] + " by " + book[1] + "\ndescription: " + book[2])
      input("\nPress Enter to continue...")
      #once user wishes to move on call prompt user to display menu
      self.promptUser()
      

   def show_locations(self, _cursor) :
      #get info about store from table store
      _cursor.execute("SELECT locale_first_line, locale_second_line, hours FROM store")
      stores = _cursor.fetchall()
      print("\n---WhatABook store information---")
      for store in stores : 
         print("\nStore location: \n   " + store[0] + "\n   " + store[1] + "\n\nStore hours: \n   " + store[2])
      input("\nPress Enter to continue...")
      #once user wishes to move on call prompt user to display menu
      self.promptUser()

   def validate_user(self, _cursor) :
      user_id : String = input("\nPlease enter your user ID to login:\n")
      _cursor.execute("SELECT user_id, first_name, last_name FROM user")
      users = _cursor.fetchall()
      #check every user within table user to see if program user entered valid userID
      for user in users :
         if user_id == str(user[0]) :
            print("\nLogin of " + user[1] + " " + user[2] + " successful")
            input("Press Enter to continue...")
            self.navigation = "my account"
            self.user_id = str(user[0])
            #once user wishes to move on call prompt user to display menu
            self.promptUser()
            return
      #if login doesn't succeed tell user
      input("\nInvalid user ID, press enter to go back to main menu...")
      #once user wishes to move on call prompt user to display menu
      self.promptUser()
      return
      
   def show_wishlist(self, _cursor, _user_id) :
      #get all books within user's wishlist
      _cursor.execute("SELECT book.book_id, book.book_name, book.author FROM wishlist INNER JOIN book ON wishlist.book_id = book.book_id INNER JOIN user ON wishlist.user_id = user.user_id WHERE user.user_id = " + _user_id)

      print("\n---Books in your wishlist---")
      books = _cursor.fetchall()
      for book in books :
         print("\n" + book[1] + " by " + book[2])
      input("\nPress Enter to continue...")
      #once user wishes to move on call prompt user to display menu
      self.promptUser()
   
   def show_books_to_add(self, _cursor, _user_id) : 
      #get all books not within user's wishlist
      _cursor.execute("SELECT book.book_id, book.book_name, book.author FROM book WHERE book.book_id NOT IN (SELECT book_id FROM wishlist WHERE user_id = " + _user_id + ")")

      print("\n---Books to add to your wishlist---")
      books = _cursor.fetchall()
      #if length of books is zero there are no more books in wishlist otherwise print all books
      if len(books) == 0 :
         input("\nYou already have all the books in your wishlist, \npress enter to go back to wishlist menu...")
         #once user wishes to move on call prompt user to display menu
         self.promptUser()
         return
      for book in books :
         print("\nbook ID: " + str(book[0]) + "\nbook: " + book[1] + " by " + book[2])
      #allow user to look through books before prompting them to enter bookID of book they wish to add
      input("\nPress Enter once you've decided on a book...")
      self.add_book_to_wishlist(cursor, _user_id, books)

   def add_book_to_wishlist(self, _cursor, _user_id, books) :
      _book_id = input("\nType the ID of the book you want to add: \n   ")
      for book in books :
         #if the bookID matches the bookID one of the books fetched from show_books_to_add select statement then
         #it is not already in user's wishlist and can be added
         if str(book[0]) == str(_book_id) :
            _cursor.execute("INSERT INTO wishlist(user_id, book_id) VALUES(" + str(_user_id) + ", " + str(_book_id) + ")")
            #show user result of adding book
            self.show_wishlist(_cursor, _user_id)
            return
         #if length of books == 0 user already has all books in wishlist
         elif len(books) == 0 :
            input("\nYou already have all the books in your wishlist, \npress enter to go back to wishlist menu...")
            #once user wishes to move on call prompt user to display menu
            self.promptUser()
            return
      #if the previous two conditions are not met user has entered invalid input or user is trying to add a book the user already has in wishlist
      print("\nYou already have that book in your wishlist or you entered invalid input.")
      user_input = input("press 1 to try again and any other key to return to wishlist menu...\n")
      if str(user_input) == str(1) :
         self.add_book_to_wishlist(_cursor, _user_id, books)
         return
      #once user wishes to move on call prompt user to display menu
      self.promptUser()
      return


#create instance of class whatABook
wb = whatABook()
#call promptUser() to start the program off
wb.promptUser()