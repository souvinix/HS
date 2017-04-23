from tkinter import *
import time

#My windows
fenster = Tk()
fenster.title('Hearthstone II')
fenster.geometry('800x600')
fenster.resizable(0,0)

#Position des Users:
POS = 'Hauptmenü'

#My images
pfad = ''
pfad2 = 'Buttons/'
background1 = PhotoImage(file = pfad+'background1.gif')
Hearthstone_Logo = PhotoImage(file = pfad+'Hearthstone_Logo.png')
startbutton_image = PhotoImage(file = pfad2+'startbutton.png')
startbutton_enter_image = PhotoImage(file = pfad2+'startbutton_enter.png')
quitbutton_image = PhotoImage(file = pfad2+'verlassenbutton.png')
quitbutton_enter_image = PhotoImage(file = pfad2+'verlassenbutton_enter.png')
optionbutton_image = PhotoImage(file = pfad2+'optionbutton.png')
optionbutton_enter_image = PhotoImage(file = pfad2+'optionbutton_enter.png')
Zettel = PhotoImage(file = pfad+'Zettel.png')
backbutton_image = PhotoImage(file = pfad2+'backbutton.png')
backbutton_enter_image = PhotoImage(file = pfad2+'backbutton_enter.png')
ladebutton_image = PhotoImage(file = pfad2+'ladebutton.png')
ladebutton_enter_image = PhotoImage(file = pfad2+'ladebutton_enter.png')
speicherbutton_image = PhotoImage(file = pfad2+'speicherbutton.png')
speicherbutton_enter_image = PhotoImage(file = pfad2+'speicherbutton_enter.png')
shop_image = PhotoImage(file = pfad+'shop_image.png')
shop_enter_image = PhotoImage(file = pfad+'shop_enter_image.png')
goldanzeige = PhotoImage(file = pfad+'Goldanzeige1.png')
packanzeige = PhotoImage(file = pfad+'Packanzeige1.png')

fenster.iconbitmap('hs_icon.ico')

class MENU(object):
    def Aufrufen():
        global MyCanvas
        def startbutton_enter(event):
            MyCanvas.itemconfigure('startbutton', image = startbutton_enter_image)
            MyCanvas.tag_bind('startbutton', '<Button-1>', startbutton_maus1)
        def startbutton_leave(event):
            MyCanvas.itemconfigure('startbutton', image = startbutton_image)

        def optionbutton_enter(event):
            MyCanvas.itemconfigure('optionbutton', image = optionbutton_enter_image)
            MyCanvas.tag_bind('optionbutton', '<Button-1>', optionbutton_maus1)
        def optionbutton_leave(event):
            MyCanvas.itemconfigure('optionbutton', image = optionbutton_image)

        def quitbutton_enter(event):
            MyCanvas.itemconfigure('quitbutton', image = quitbutton_enter_image)
            MyCanvas.tag_bind('quitbutton', '<Button-1>', quitbutton_maus1)
        def quitbutton_leave(event):
            MyCanvas.itemconfigure('quitbutton', image = quitbutton_image)

        def shopbutton_enter(event):
            MyCanvas.itemconfigure('shopbutton', image = shop_enter_image)
            MyCanvas.tag_bind('shopbutton', '<Button-1>', shop_maus1)
            MyCanvas.itemconfigure('shoptext', fill = 'white')
        def shopbutton_leave(event):
            MyCanvas.itemconfigure('shopbutton', image = shop_image)
            MyCanvas.itemconfigure('shoptext', fill = 'black')

        MyCanvas = Canvas(fenster, width = 800, height = 600)
        MyCanvas.place(x = 0, y = 0)
        MyCanvas.create_image(400,300, image = background1, tags = 'canv_background1')
        MyCanvas.create_image(400,105, image = Hearthstone_Logo, tags = 'canv_hearthstone_logo')
        MyCanvas.create_image(360,275, image = startbutton_image, tags = 'startbutton')
        MyCanvas.create_image(450,400, image = optionbutton_image, tags = 'optionbutton')
        MyCanvas.create_image(540,525, image = quitbutton_image, tags = 'quitbutton')
        MyCanvas.create_image(160, 550, image = shop_image, tags = 'shopbutton')
        MyCanvas.create_text(160, 480, text = 'Shop', font = ('Terminator Two', 30), fill = 'black', tags = 'shoptext')

        MyCanvas.tag_bind('startbutton', '<Enter>', startbutton_enter)
        MyCanvas.tag_bind('startbutton', '<Leave>', startbutton_leave)
        MyCanvas.tag_bind('optionbutton', '<Enter>', optionbutton_enter)
        MyCanvas.tag_bind('optionbutton', '<Leave>', optionbutton_leave)
        MyCanvas.tag_bind('quitbutton', '<Enter>', quitbutton_enter)
        MyCanvas.tag_bind('quitbutton', '<Leave>', quitbutton_leave)
        MyCanvas.tag_bind('shopbutton', '<Enter>', shopbutton_enter)
        MyCanvas.tag_bind('shopbutton', '<Leave>', shopbutton_leave)

    def Entfernen(Hintergrund):
        if Hintergrund.lower() == 'ja':
            MyCanvas.delete('startbutton', 'quitbutton', 'optionbutton', 'canv_hearthstone_logo', 'shopbutton', 'shoptext')
        elif Hintergrund.lower() == 'nein':
            MyCanvas.delete('startbutton', 'quitbutton', 'optionbutton', 'canv_hearthstone_logo', 'canv_background1', 'shopbutton', 'shoptext')

class BACKBUTTON(object):
    def create():
        MyCanvas.create_image(60,30, image = backbutton_image, tags = 'backbutton')

        def backbutton_enter(event):
            MyCanvas.itemconfigure('backbutton', image = backbutton_enter_image)
            MyCanvas.tag_bind('backbutton', '<Button-1>', backbutton_maus1)
        def backbutton_leave(event):
            MyCanvas.itemconfigure('backbutton', image = backbutton_image)

        def backbutton_maus1(event):
            global POS
            if POS == 'Hauptmenü':
                pass
            elif POS == 'Optionen':
                MyCanvas.delete('Zettel', 'backbutton', 'canv_background1', 'text1', 'ladebutton', 'speicherbutton')
                Hauptmenü.Aufrufen()
                POS = 'Hauptmenü'
                
            elif POS == 'Start':
                Hauptmenü.Aufrufen()
            elif POS == 'Shop':
                MyCanvas.delete('goldanzeige', 'packanzeige', 'backbutton')
                Hauptmenü.Aufrufen()
                POS = 'Hauptmenü'
        
        MyCanvas.tag_bind('backbutton', '<Enter>', backbutton_enter)
        MyCanvas.tag_bind('backbutton', '<Leave>', backbutton_leave)
        

def startbutton_maus1(event):
    global POS
    POS = 'Start'
    Hauptmenü.Entfernen('nein')
    Backbutton.create()

def shop_maus1(event):
    global POS
    POS = 'Shop'
    MyCanvas.create_image(450, 50, image = goldanzeige, tags = 'goldanzeige')
    MyCanvas.create_image(650, 50, image = packanzeige, tags = 'packanzeige')
    Hauptmenü.Entfernen('ja')
    Backbutton.create()

def optionbutton_maus1(event):
    global POS
    POS = 'Optionen'
    Hauptmenü.Entfernen('ja')
    MyCanvas.create_image(400, 300, image = Zettel, tags = 'Zettel')
    MyCanvas.create_text(400, 100, text = 'Laden/Speichern', font = ('Terminator Two', 17), tags = 'text1')
    MyCanvas.create_image(320, 150, image = ladebutton_image, tags = 'ladebutton')
    MyCanvas.create_image(470, 150, image = speicherbutton_image, tags = 'speicherbutton')
    
    MyCanvas.tag_bind('ladebutton', '<Enter>', ladebutton_enter)
    MyCanvas.tag_bind('ladebutton', '<Leave>', ladebutton_leave)
    MyCanvas.tag_bind('speicherbutton', '<Enter>', speicherbutton_enter)
    MyCanvas.tag_bind('speicherbutton', '<Leave>', speicherbutton_leave)
    Backbutton.create()

def ladebutton_enter(event):
    MyCanvas.itemconfigure('ladebutton', image = ladebutton_enter_image)
    MyCanvas.tag_bind('ladebutton', '<Button-1>', ladebutton_maus1)
def ladebutton_leave(event):
    MyCanvas.itemconfigure('ladebutton', image = ladebutton_image)
    
def speicherbutton_enter(event):
    MyCanvas.itemconfigure('speicherbutton', image = speicherbutton_enter_image)
    MyCanvas.tag_bind('speicherbutton', '<Button-1>', speicherbutton_maus1)
def speicherbutton_leave(event):
    MyCanvas.itemconfigure('speicherbutton', image = speicherbutton_image)

def ladebutton_maus1(event):
    pass

def speicherbutton_maus1(event):
    pass

def quitbutton_maus1(event):
    fenster.destroy()

    
        

Hauptmenü = MENU
Backbutton = BACKBUTTON
Hauptmenü.Aufrufen()
fenster.mainloop()

