import sqlite3

Database = '/Users/noahg/Desktop/Neuer Ordner/HS_Database.db'
connection = sqlite3.connect(Database)

cursor = connection.cursor()

#command = '''create table Accounts (Name string, Passwort string, Level int, Gold int, Packs int, Staub int, Ep int, Epnextlevel int);'''
command = '''select * from Accounts'''

cursor.execute(command)

