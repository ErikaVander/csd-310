#Erika Vanderhoff
#csd 310
#assignment_9.3
#4/25/22

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

#insert smeagol into table player
cursor.execute("INSERT INTO player (first_name, last_name, team_id) VALUES ('Smeagol', 'Shire Folk', 1)")

#do inner join query to display results of previous command
cursor.execute("SELECT player_id, first_name, last_name, team_name FROM player INNER JOIN team ON player.team_id = team.team_id")

#store results of previous query in variable players
players = cursor.fetchall()

#use for loop to print each player in variable players
print("\n--DISPLAYING PLAYERS AFTER INSERT--")
for player in players:
   print("Player ID: {}".format(player[0]))
   print("First Name: {}".format(player[1]))
   print("Last Name: {}".format(player[2]))
   print("Team Name: {}\n".format(player[3]))

#update player smeagol to have a first name of gollum, a last name of ring stealer and a team_id of 2 (or team sauron)
cursor.execute("UPDATE player SET team_id = 2, first_name = 'Gollum', last_name = 'Ring Stealer' WHERE first_name = 'Smeagol'")

#do inner join query to display results of previous command
cursor.execute("SELECT player_id, first_name, last_name, team_name FROM player INNER JOIN team ON player.team_id = team.team_id")

#store results of previous query in variable players
players = cursor.fetchall()

#use for loop to print each player in variable players
print("\n--DISPLAYING PLAYERS AFTER DELETE--")
for player in players:
   print("Player ID: {}".format(player[0]))
   print("First Name: {}".format(player[1]))
   print("Last Name: {}".format(player[2]))
   print("Team Name: {}\n".format(player[3]))

#delete player with first name gollum
cursor.execute("DELETE FROM player WHERE first_name = 'Gollum'")

#do inner join query to display results of previous command
cursor.execute("SELECT player_id, first_name, last_name, team_name FROM player INNER JOIN team ON player.team_id = team.team_id")

#store results of previous query in variable players
players = cursor.fetchall()

#use for loop to print each player in variable players
print("\n--DISPLAYING PLAYERS AFTER DELETE--")
for player in players:
   print("Player ID: {}".format(player[0]))
   print("First Name: {}".format(player[1]))
   print("Last Name: {}".format(player[2]))
   print("Team Name: {}\n".format(player[3]))