#Erika Vanderhoff
#csd 310
#assignment_8.2
#4/22/22

import mysql.connector
from mysql.connector import errorcode

#creating user object to use to connect to mysql.pysports
config = {
   "user": "pysports_user",
   "password": "MYSQL8IsGreat!",
   "host": "localhost",
   "database": "pysports",
   "raise_on_warnings": True 
}

#try connecting otherwise print error messages
try:
   db = mysql.connector.connect(**config)

   print("\n   Database user {} connected to MySQL on host {} with database {}".format(config["user"], config["host"], config["database"]))

   input("\n\n   Press any key to continue...")

except mysql.connector.Error as err:
   if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
      print("  The supplied username or password are invalid")

   elif err.errno == errorcode.ER_BAD_DB_ERROR:
      print("  The specified database does not exist")

   else:
      print(err)

#close db at the end
finally:
   db.close()
   