#Erika Vanderhoff
#csd 310
#assignment_9.3
#4/25/22

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

class whatABook :
   navigation : String = "main menu"
   user_id : String = ""
   book_id : String = ""
   def promptUser(self) :
      if self.navigation == "main menu": 
         print("\n\n         --------Main Menu--------")
         userNavInput = input("\nType one of these commands and press enter: \n   view books      -> view a list of our books\n   store location  -> view store's location and hours\n   my account      -> login to view and use your wishlist\n   exit            -> exit the program\n")

         if userNavInput.lower() == "view books":
            self.show_books(cursor)

         elif userNavInput.lower() == "store location":
            self.show_locations(cursor)

         elif userNavInput.lower() == "my account":
            self.validate_user(cursor)

         elif userNavInput.lower() == "exit":
            return

         else:
            print("\nInvalid input, please try again")
            input("Press Enter to continue...")
            self.promptUser()

      elif self.navigation == "my account":
         print("\n\n         --------Wishlist Menu--------")
         userNavInput = input("\nType one of these commands and press enter: \n   view wishlist   -> view a list of the books in your wishlist\n   add book        -> add a book to your wishlist\n   main menu       -> go back to the main menu\n   exit            -> exit the program\n")

         if userNavInput.lower() == "view wishlist":
            self.show_wishlist(cursor, self.user_id)

         elif userNavInput.lower() == "add book":
            self.show_books_to_add(cursor, self.user_id)

         elif userNavInput.lower() == "main menu":
            self.navigation = "main menu"
            self.promptUser()
         elif userNavInput.lower() == "exit":
            print("\nexiting the program\nhave a nice day...")
            return
         else:
            print("\nInvalid input, please try again")
            input("Press Enter to continue...")
            self.promptUser()

   def show_books(self, _cursor) :
      _cursor.execute("SELECT book.book_name, book.author, book.description FROM book")
      books = _cursor.fetchall()
      print("\n---WhatABook books---")
      for book in books :
         print("\n" + book[0] + " by " + book[1] + "\ndescription: " + book[2])
      input("\nPress Enter to continue...")
      self.promptUser()
      

   def show_locations(self, _cursor) :
      _cursor.execute("SELECT locale_first_line, locale_second_line, hours FROM store")
      stores = _cursor.fetchall()
      print("\n---WhatABook store information---")
      for store in stores : 
         print("\nStore location: \n   " + store[0] + "\n   " + store[1] + "\n\nStore hours: \n   " + store[2])
      input("\nPress Enter to continue...")
      self.promptUser()

   def validate_user(self, _cursor) :
      user_id : String = input("\nPlease enter your user ID to login:\n")
      _cursor.execute("SELECT user_id, first_name, last_name FROM user")
      users = _cursor.fetchall()
      for user in users :
         if user_id == str(user[0]) :
            print("\nLogin of " + user[1] + " " + user[2] + " successful")
            input("Press Enter to continue...")
            self.navigation = "my account"
            self.user_id = str(user[0])
            self.promptUser()
            return
      input("\nInvalid user ID, press enter to go back to main menu...")
      self.promptUser()
      return
      
   def show_wishlist(self, _cursor, _user_id) :
      _cursor.execute("SELECT book.book_id, book.book_name, book.author FROM wishlist INNER JOIN book ON wishlist.book_id = book.book_id INNER JOIN user ON wishlist.user_id = user.user_id WHERE user.user_id = " + _user_id)

      print("\n---Books in your wishlist---")
      books = _cursor.fetchall()
      for book in books :
         print("\n" + book[1] + " by " + book[2])
      input("\nPress Enter to continue...")
      self.promptUser()
   
   def show_books_to_add(self, _cursor, _user_id) : 
      _cursor.execute("SELECT book.book_id, book.book_name, book.author FROM book WHERE book.book_id NOT IN (SELECT book_id FROM wishlist WHERE user_id = " + _user_id + ")")

      print("\n---Books to add to your wishlist---")
      books = _cursor.fetchall()
      for book in books :
         print("\nbook ID: " + str(book[0]) + "\nbook: " + book[1] + " by " + book[2])
      input("\nPress Enter once you've decided on a book...")
      self.add_book_to_wishlist(cursor, _user_id)

   def add_book_to_wishlist(self, _cursor, _user_id) :
      _book_id = input("\nType the ID of the book you want to add: \n   ")
      try:
         _cursor.execute("INSERT INTO wishlist(user_id, book_id) VALUES(" + _user_id + ", " + _book_id + ")")
      except:
         input("\nInvalid bookID, press enter to go back to try again...")
         self.add_book_to_wishlist(_cursor, _user_id)
         return
      self.show_wishlist(_cursor, _user_id)



wb = whatABook()
wb.promptUser()