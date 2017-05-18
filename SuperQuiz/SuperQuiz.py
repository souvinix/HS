from tkinter import *
import sqlite3
import random

try:
    connection = sqlite3.connect('/Users/noahg/Desktop/SuperQuiz/SuperDatabase.db')
except:
    connection = sqlite3.connect('SuperDatabase.db')

cursor = connection.cursor()
command = ('create table if not exists Quiz (Frage, a1, a2, a3 ,a4);')
cursor.execute(command)

fenster = Tk()
fenster.title('SuperQuiz')
fenster.geometry('800x600')
fenster.resizable(0,0)

class Hauptmenü(object):
    def __init__(self, master):
        self.master = master
        self.logo_pos = 0
        self.MyCanvas = Canvas(self.master, width = 800, height = 600)
        self.MyCanvas.place(x = 0, y = 0)

        self.logo = self.MyCanvas.create_text(400, 100, text = 'SuperQuiz', fill = 'red',
                                              font = ('Terminator Two', 80), tags = 'Logo')

    def Move_logo(self, direction):
        if direction == 'down' and self.logo_pos < 50:
            x = 0
            y = 1
            self.logo_pos += 1
            self.MyCanvas.after(30, self.Move_logo('up'))
        elif direction == 'up':
            x = 0
            y = -1
            self.logo_pos -= 1
            self.MyCanvas.after(30, self.Move_logo('down'))
            if self.logo_pos == 0:
                self.MyCanvas.after(30, self.Move_logo('up'))

        else:
            print('Fehler')
                
        self.MyCanvas.move(self.logo, x, y)
        #self.MyCanvas.after(30, self.Move_logo)


MeinHauptmenü = Hauptmenü(fenster)
MeinHauptmenü.Move_logo('down')
fenster.mainloop()
