import sqlite3
connection = sqlite3.connect("/Users/noahg/Desktop/HS II/HS_Database.db")

cursor = connection.cursor()

cursor.execute("SELECT Level FROM Accounts where Name = 'Noah'")

print("Noahs Level:")
Level = cursor.fetchall() 
for i in Level:
    print(i[0])

cursor.execute("SELECT Gold FROM Accounts where Name = 'Noah'")

print("Noahs Gold:")
Level = cursor.fetchall() 
for i in Level:
    print(i[0])

cursor.execute("SELECT Packs FROM Accounts where Name = 'Noah'")

print("Noahs Packs:")
Level = cursor.fetchall() 
for i in Level:
    print(i[0])

cursor.execute("SELECT Staub FROM Accounts where Name = 'Noah'")

print("Noahs Satub:")
Level = cursor.fetchall() 
for i in Level:
    print(i[0])

cursor.execute("SELECT Ep FROM Accounts where Name = 'Noah'")

print("Noahs Ep:")
Level = cursor.fetchall() 
for i in Level:
    print(i[0])

cursor.execute("SELECT Epnextlevel FROM Accounts where Name = 'Noah'")

print("Noahs Ep bis zum nächsten Level:")
Level = cursor.fetchall() 
for i in Level:
    print(i[0])

Name = 'Admin'
Passwort = ''
command = ('select ? from Accounts where Name = ? and Passwort = ?')
cursor.execute(command, (Level, Name, Passwort))
Level = cursor.fetchall()
for i in Level:
    Level = i[0]
    print(Level)
