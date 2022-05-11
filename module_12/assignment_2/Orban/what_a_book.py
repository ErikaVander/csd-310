# Ben Orban
# Assignment 12.3 WhatABook Delivery

""" import statements """
from calendar import c
import sys
import mysql.connector
from mysql.connector import errorcode


""" database config object """
config = {
    "user": "whatabook_user",
    "password": "MySQL8IsGreat!",
    "host": "127.0.0.1",
    "database": "whatabook",
    "raise_on_warnings": True
}

def show_menu():
    db = mysql.connector.connect(**config) # connect to the WhatABook database 
    cursor = db.cursor() # cursor for MySQL queries
    choice = str(0)

    while(choice != str(4)):
        print("\nMain Menu")
        print("1. View Books")
        print("2. View Store Locations")
        print("3. My Account")
        print("4. Exit")

        choice = input("Enter your selection: ")

        if(choice == str(1)):
            show_books(cursor)
        if(choice == str(2)):
            show_locations(cursor)
        if(choice == str(3)):
            user_id = str(input("Please enter your user id: "))
            isValidUser = validate_user(user_id, cursor)

            if(isValidUser):
                show_account_menu(cursor, user_id)
        
    db.close()

def show_books(_cursor):
    print("Show Books")
    _cursor.execute("SELECT * FROM book")
    books = _cursor.fetchall()
    for book in books:
        print(book)

def show_locations(_cursor):
    print("Show Locations")
    _cursor.execute("SELECT * FROM store")
    locations = _cursor.fetchall()
    for location in locations:
        print(location)

def validate_user(_user_id, _cursor):
    _cursor.execute("SELECT * FROM user WHERE user_id = " + _user_id)
    result = _cursor.fetchall()
    if(result):
        return True

def show_account_menu(_cursor, _user_id):
    account_choice = str(0)

    while(account_choice != str(3)):
        print("\nWishlist Menu")
        print("1. Wishlist")
        print("2. Add Book")
        print("3. Main Menu")

        account_choice = input("Enter your selection: ")

        if(account_choice == str(1)):
            show_wishlist(_cursor, _user_id)
        if(account_choice == str(2)):
            book_id = show_books_to_add(_cursor, _user_id)
            if(book_id):
                isAdded = add_book_to_wishlist(_cursor, _user_id, book_id)
                print("Book Successfully Added")
                

def show_wishlist(_cursor, _user_id):
    _cursor.execute("SELECT b.book_name, b.author, b.details FROM book b INNER JOIN wishlist w ON w.book_id = b.book_id WHERE w.user_id =" + _user_id)
    books = _cursor.fetchall()

    if(books):
        for book in books:
            print("\nBook: " + book[0])
            print("Author: " + book[1])
            if(book[2]):
                print("Details: " + book[2])

def show_books_to_add(_cursor, _user_id):
    _cursor.execute("SELECT * FROM book WHERE book_id NOT IN (SELECT book_id FROM wishlist WHERE user_id =" + _user_id + ")")
    books = _cursor.fetchall()
    
    for book in books:
        print(book)
    
    return str(input("Enter Book ID to add to Wishlist: "))


def add_book_to_wishlist(_cursor, _user_id, _book_id):
    _cursor.execute("INSERT INTO wishlist(user_id, book_id) VALUES('" + _user_id + "', '"+ _book_id + "')")
    _cursor.execute("SELECT book_id FROM wishlist WHERE user_id=" + _user_id + " AND book_id =" + _book_id)
    isAdded = _cursor.fetchall()

    return isAdded

show_menu()