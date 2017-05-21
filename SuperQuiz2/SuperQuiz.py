from tkinter import *
#import random
import sqlite3
import os
#import sys

#sys.setrecursionlimit(1000000)

try:
    Verzeichnis = ('/Users/noahg/Desktop/SuperQuiz2')
    if not os.path.exists(Verzeichnis):
        os.makedirs(Verzeichnis)
except:
    Verzeichnis = ('/home/nwantoch/Arbeitsfläche/SuperQuiz2')
    if not os.path.exists(Verzeichnis):
        os.makedirs(Verzeichnis)

try:
    connection = sqlite3.connect('/Users/noahg/Desktop/SuperQuiz2/SuperDatabase.db')
except:
    try:
        connection = sqlite3.connect('/home/nwantoch/Arbeitsfläche/SuperQuiz2/SuperDatabase.db')
    except:
        connection = sqlite3.connect('SuperDatabase.db')

cursor = connection.cursor()
command = ('SELECT name FROM sqlite_master WHERE type="table";')
cursor.execute(command)
for i in cursor:
    All_Quiz = len(i)
    Quiz_Names = i

print(Quiz_Names)
    
fenster = Tk()
fenster.title('SuperQuiz')
fenster.geometry('800x600')
fenster.resizable(0,0)

Main_Canvas = Canvas(fenster, width = 800, height = 600)
Main_Canvas.place(x = 0, y = 0)

pfad = ''
background = PhotoImage(file = pfad+'SuperQuiz_bg.gif')
rahmen = PhotoImage(file = pfad+'Rahmen.gif')
Position = StringVar()

class Zurückknopf(object):
    def __init__(self, MyCanvas, Menu):
        self.MyCanvas = MyCanvas
        self.Menu = Menu
    def Aufrufen(self):
        self.MyCanvas.create_text(50, 10, text = 'Zurück', font = ('Terminator Two', 15), fill = 'light blue',
                                  tags = 'Backbutton')
        def backbutton_enter(event):
            self.MyCanvas.itemconfigure('Backbutton', fill = 'white')
            self.MyCanvas.tag_bind('Backbutton', '<Button-1>', Back)
        def backbutton_leave(event):
            self.MyCanvas.itemconfigure('Backbutton', fill = 'light blue')
            
        def Back(event):
            if Position == 'Start':
                try:
                    self.Menu.Aufrufen()
                    try:
                        self.MyCanvas.delete('No_Quiz')
                    except:
                        pass
                except:
                    print('Backbutton-Fehler(#1)')
            elif Position == 'Myquiz':
                self.Menu.Aufrufen()
        self.MyCanvas.tag_bind('Backbutton', '<Enter>', backbutton_enter)
        self.MyCanvas.tag_bind('Backbutton', '<Leave>', backbutton_leave)
    
class Hauptmenü(object):
    def __init__(self, MyCanvas):
        global Position
        
        self.MyCanvas = MyCanvas
        self.logo_pos = 0
        self.logo_y = 0
        self.startbutton_pos = 0
        self.startbutton_y = 0
        self.myquizbutton_pos = 0
        self.myquizbutton_y = 0
        
    def Aufrufen(self):

        def startbutton_enter(event):
            self.MyCanvas.itemconfigure('Startbutton', fill = 'white')
            self.MyCanvas.tag_bind('Startbutton', '<Button-1>', start)
        def startbutton_leave(event):
            self.MyCanvas.itemconfigure('Startbutton', fill = 'light blue')
        def myquizbutton_enter(event):
            self.MyCanvas.itemconfigure('Myquizbutton', fill = 'white')
            self.MyCanvas.tag_bind('Myquizbutton', '<Button-1>', myquiz)
        def myquizbutton_leave(event):
            self.MyCanvas.itemconfigure('Myquizbutton', fill = 'light blue')
            
        self.MyCanvas.create_image(0, 0, image = background, tags = 'Background')

        self.logo = self.MyCanvas.create_text(400, 100, text = 'SuperQuiz', fill = 'red',
                                              font = ('Terminator Two', 80), tags = 'Logo')

        self.startbutton = self.MyCanvas.create_text(400, 400, text = 'Starten', font = ('Terminator Two', 50),
                                  fill = 'light blue', tags = 'Startbutton')

        self.myquizbutton = self.MyCanvas.create_text(400, 300, text = "Mein Quiz", font = ('Terminator Two', 50),
                                                      fill = 'light blue', tags = 'Myquizbutton')
        
        self.MyCanvas.tag_bind('Myquizbutton', '<Enter>', myquizbutton_enter)
        self.MyCanvas.tag_bind('Myquizbutton', '<Leave>', myquizbutton_leave)
        self.MyCanvas.tag_bind('Startbutton', '<Enter>', startbutton_enter)
        self.MyCanvas.tag_bind('Startbutton', '<Leave>', startbutton_leave)

        Position = 'Hauptmenü'

    def move_logo(self):
        Geschwindigkeit = 30
        if self.logo_pos == 0:
            self.logo_y = 1
        elif self.logo_pos == 25:
            self.logo_y = -1

        if self.logo_y == 1:
            self.logo_pos += 1
        elif self.logo_y == -1:
            self.logo_pos -= 1
        
        x = 0
        self.MyCanvas.move(self.logo, self.logo_y, x)
        self.MyCanvas.after(Geschwindigkeit, self.move_logo)

    def move_startbutton(self):
        Geschwindigkeit = 25
        if self.startbutton_pos == 0:
            self.startbutton_y = 1
        elif self.startbutton_pos == 15:
            self.startbutton_y = -1

        if self.startbutton_y == 1:
            self.startbutton_pos += 1
        elif self.startbutton_y == -1:
            self.startbutton_pos -= 1
        
        x = 0
        self.MyCanvas.move(self.startbutton, x, self.startbutton_y)
        self.MyCanvas.after(Geschwindigkeit, self.move_startbutton)

    def move_myquizbutton(self):
        Geschwindigkeit = 25
        if self.myquizbutton_pos == 0:
            self.myquizbutton_y = -1
        elif self.myquizbutton_pos == 15:
            self.myquizbutton_y = 1

        if self.myquizbutton_y == -1:
            self.myquizbutton_pos += 1
        elif self.myquizbutton_y == 1:
            self.myquizbutton_pos -= 1
        
        x = 0
        self.MyCanvas.move(self.myquizbutton, x, self.myquizbutton_y)
        self.MyCanvas.after(Geschwindigkeit, self.move_myquizbutton)

    def move_ALL(self, ):
        self.move_logo()
        self.move_startbutton()
        self.move_myquizbutton()

    def Entfernen(self):
        try:
            self.MyCanvas.delete('Startbutton', 'Myquizbutton', 'Logo', 'Background')
        except:
            print('Fehler beim löschen der Buttons/des Logos/Background')

MeinHauptmenü = Hauptmenü(Main_Canvas)
MeinHauptmenü.Aufrufen()
Backbutton = Zurückknopf(Main_Canvas, MeinHauptmenü)
MeinHauptmenü.move_ALL()

def start(event):
    global Position
    MeinHauptmenü.Entfernen()
    Backbutton.Aufrufen()
    Position = 'Start'
    try:
        if All_Quiz:
            Menge = 0
            Rahmen_Pos = 100
            for s in range(All_Quiz):
                print(All_Quiz)
                Main_Canvas.create_image(400, Rahmen_Pos, image = rahmen, tags = 'Rahmen')
                Menge += 1
                Rahmen_Pos += 100
                
                
    except:
        Main_Canvas.create_text(400, 275, text = 'Kein Quiz wurde erstellt.', font = ('Terminator Two', 30),
                                 fill = 'red', tags = 'No_Quiz')
def myquiz(event):
    global Position
    MeinHauptmenü.Entfernen()
    Position = 'Myquiz'
        
fenster.mainloop()
