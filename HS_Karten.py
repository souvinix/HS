import sqlite3

try:
    connection = sqlite3.connect('/Users/noahg/Desktop/HS II/HS_Database.db')
except:
    connection = sqlite3.connect('Arbeitsfläche/HS_Database.db')

cursor = connection.cursor()

command = ('create table if not exists Diener (Kartenname, Atk, Hp, Mana, Art_Rasse, Effektart_zb_Kampfschrei, Effekt, Seltenheit)')
cursor.execute(command)

command = ('create table if not exists Zauber (Kartenname, Mana, Effekt, Seltenheit)')
cursor.execute(command)

command = ('select * from Zauber')
cursor.execute(command)
result = cursor.fetchall()

print('~'*15)
print('Alle Zauber:')
print('~'*15)
for i in result:
    Alle_Zauber = i[0]
    print(Alle_Zauber)

command = ('select * from Diener')
cursor.execute(command)
result = cursor.fetchall()

print('~'*15)
print('Alle Diener:')
print('~'*15)
for i in result:
    Alle_Diener = i[0]
    print(Alle_Diener)
