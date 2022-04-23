#Erika Vanderhoff
#csd 310
#assignment_8.3
#4/22/22

from tkinter.tix import Select
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

except mysql.connector.Error as err:
   if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
      print("  The supplied username or password are invalid")

   elif err.errno == errorcode.ER_BAD_DB_ERROR:
      print("  The specified database does not exist")

   else:
      print(err)

#create cursor object
cursor = db.cursor()

#getting team_id, team_name, and mascot from row team
cursor.execute("SELECT team_id, team_name, mascot FROM team")
teams = cursor.fetchall()

#using for loop to display team_id, team_name, and mascot
print("\n-- DISPLAYING TEAM RECORDS --")
for team in teams:
   print("Team ID: {}".format(team[0]))
   print("Team Name: {}".format(team[1]))
   print("Mascot: {}\n".format(team[2]))

#getting player_id, first_name, and last_name from row player
cursor.execute("SELECT player_id, first_name, last_name, team_id FROM player")
players = cursor.fetchall()

#using for loop to display player_id, first_name, last_name and team_id
print("-- DISPLAYING PLAYER RECORDS --")
for player in players:
   print("Player ID: {}".format(player[0]))
   print("First Name: {}".format(player[1]))
   print("Last Name: {}".format(player[2]))
   print("Team ID: {}\n".format(player[3]))

#waiting till using wishes to exit program by pressing enter key
input("\n\n   Press any key to continue...")
db.close()