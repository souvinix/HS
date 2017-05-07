from tkinter import *
import time
from Account import *
import sqlite3
import os

try:
    connection = sqlite3.connect('/Users/noahg/Desktop/HS II/HS_Database.db')
except:
    connection = sqlite3.connect('HS_Database.db')

cursor = connection.cursor()

try:
    cursor.execute('create table if not exists Accounts (Name, Passwort, Level, Gold, Packs, Staub, Ep, Epnextlevel);')
except:
    pass

Login = False

def RegisterSQL(Name, Passwort, Passwort2):
    Gold = 0
    Level = 1
    Staub = 0
    Packs = 0
    Ep = 0
    Epnextlevel = 100
    Name = Name
    Passwort = Passwort
    Passwort2 = Passwort2
    
    cursor.execute("INSERT INTO Accounts (Name, Passwort, Level, Gold, Packs, Staub, Ep, Epnextlevel) VALUES (?,?,?,?,?,?,?,?)", (Name, Passwort, Level, Gold, Packs, Staub, Ep, Epnextlevel))
    connection.commit()

    __USER__ = Account(Name, Passwort, Level, Gold, Packs, Staub)

def AnmeldenSQL(Name, Passwort):
    global Login
    find_user = ('select * from Accounts where Name = ? and Passwort = ?')
    cursor.execute(find_user, [(Name), (Passwort)])
    results = cursor.fetchall()

    if results:
        for i in results:
            print('Willkommen', str(Name)+'!')
            fenster = anmeldung
            Login = True
            Top.Window('Clear_All')
            AfterLogin()
                        
            
    else:

        print('Der Account mit dem Namen:\n', str(Name),'\nund dem Passwort:\n', str(Passwort),'\nkonnte nicht gefunden werden!\n\n')

def Anmeldebutton_enter(event):
    AnmCanvas.itemconfigure('Anmeldebutton', image = Anmeldebutton_enter_image)
    AnmCanvas.tag_bind('Anmeldebutton', '<Button-1>', Anmeldebutton_function)
def Anmeldebutton_leave(event):
    AnmCanvas.itemconfigure('Anmeldebutton', image = Anmeldebutton_image)
def Registerbutton_enter(event):
    AnmCanvas.itemconfigure('Registerbutton', image = Registerbutton_enter_image)
    AnmCanvas.tag_bind('Registerbutton', '<Button-1>', Registerbutton_function)
def Registerbutton_leave(event):
    AnmCanvas.itemconfigure('Registerbutton', image = Registerbutton_image)

def bestätigen_enter(event):
    if Position == 'Anmelden':
        AnmCanvas.itemconfigure('Bestätigen', image = bestätigen_anm_enter_image)
        AnmCanvas.tag_bind('Bestätigen', '<Button-1>', bestätigen_func)
    elif Position == 'Registrieren':
        AnmCanvas.itemconfigure('Bestätigen', image = bestätigen_anm_enter_image)
        AnmCanvas.tag_bind('Bestätigen', '<Button-1>', bestätigen_reg_func)
def bestätigen_leave(event):
    AnmCanvas.itemconfigure('Bestätigen', image = bestätigen_anm_image)

def bestätigen_func(event):
    global Entry_Name, Entry_Passwort
    Entry_Name = Name_eingabe.get()
    Entry_Passwort = Passwort_eingabe.get()
    AnmeldenSQL(Entry_Name, Entry_Passwort)

    if not Login:
        Name_eingabe.delete(0, 'end')
        Passwort_eingabe.delete(0, 'end')

def Anmeldebutton_function(event):
    global Position, Name_eingabe, Passwort_eingabe
    User.Window('OnlyBG')
    Position = 'Anmelden'
    User.create_backbutton(Position)

    AnmCanvas.create_text(250, 180, text = 'Name:', font = ('Terminator Two', 20), tags = 'Name')
    #Entry
    Name_eingabe = Entry(bd = 15, width = 10, font = ('MelodBold', 20), bg = '#8B591C')
    Name_eingabe.place(x = 150, y = 200)

    AnmCanvas.create_text(250, 310, text = 'Passwort', font = ('Terminator Two', 20), tags = 'Passwort')
    #Entry
    Passwort_eingabe = Entry(bd = 15, width = 10, font = ('MelodBold', 20), bg = '#8B591C', show = '*')
    Passwort_eingabe.place(x = 150, y = 330)

    AnmCanvas.create_image(250, 480, image = bestätigen_anm_image, tags = 'Bestätigen')
    
    AnmCanvas.tag_bind('Bestätigen', '<Enter>', bestätigen_enter)
    AnmCanvas.tag_bind('Bestätigen', '<Leave>', bestätigen_leave)
    anmeldung.bind('<Return>', bestätigen_func)

    

def Registerbutton_function(event):
    global Position, Name_eingabe, Passwort_eingabe, Passwort_eingabe2
    Position = 'Registrieren'
    User.Window('OnlyBG')
    User.create_backbutton(Position)
    AnmCanvas.create_text(250, 150, text = 'Name:', font = ('Terminator Two', 20), tags = 'Name')
    Name_eingabe = Entry(bd = 15, width = 10, font = ('MelodBold', 20), bg = '#8B591C')
    Name_eingabe.place(x = 150, y = 170)

    AnmCanvas.create_text(250, 250, text = 'Passwort:', font = ('Terminator Two', 20), tags = 'Passwort')
    Passwort_eingabe = Entry(bd = 15, width = 10, font = ('MelodBold', 20), bg = '#8B591C', show = '*')
    Passwort_eingabe.place(x = 150, y = 270)

    AnmCanvas.create_text(250, 350, text = 'Passwort wiederholen:', font = ('Terminator Two', 18), tags = 'Passwort2')
    Passwort_eingabe2 = Entry(bd = 15, width = 10, font = ('MelodBold', 20), bg = '#8B591C', show = '*')
    Passwort_eingabe2.place(x = 150, y = 370)

    AnmCanvas.create_image(250, 510, image = bestätigen_anm_image, tags = 'Bestätigen')
    AnmCanvas.tag_bind('Bestätigen', '<Enter>', bestätigen_enter)
    AnmCanvas.tag_bind('Bestätigen', '<Leave>', bestätigen_leave)
    anmeldung.bind('<Return>', bestätigen_reg_func)

def bestätigen_reg_func(event):
    Entry_Name = Name_eingabe.get()
    Entry_Passwort = Passwort_eingabe.get()
    Entry_Passwort2 = Passwort_eingabe2.get()
    Register = True
    
    if Entry_Passwort != Entry_Passwort2:
        print('Passwörter stimmen nicht überein.')
        Register = False

    if Entry_Passwort == '' and Entry_Passwort2 == '':
        print('Füllen sie die Pflichtfelder aus(Passwort).')
        Register = False

    if (len(Entry_Passwort) < 7):
        print('Passwort ist zu kurz! (7 Zeichen)')
        Register = False
        
    if Entry_Name == '':
        print('Füllen sie die Pflichtfelder aus(Name).')
        Register == False

    if (len(Entry_Name) < 4):
        print('Name ist zu kurz! (4 Zeichen)')
        Register == False

    if Register == True:
        find_user = ('select * from Accounts where Name = ?')
        cursor.execute(find_user, [(Entry_Name),])
        results = cursor.fetchall()

        if results:
            print('User existiert bereits!')

        else:
            print('Account wurde erstellt!')
            RegisterSQL(Entry_Name, Entry_Passwort, Entry_Passwort2)
            Name_eingabe.delete(0, 'end')
            Passwort_eingabe.delete(0, 'end')
            Passwort_eingabe2.delete(0, 'end')
    

def backbutton_enter(event):
    AnmCanvas.itemconfigure('backbutton', image = backbutton_enter_anm_image)
    AnmCanvas.tag_bind('backbutton', '<Button-1>', backbutton_func)

def backbutton_leave(event):
    AnmCanvas.itemconfigure('backbutton', image = backbutton_anm_image)

def backbutton_func(event):
    User.Window('Clear_All')
    User.Aufrufen()

class Anmeldefenster(object):
    def __init__(self):
        global anmeldung
        anmeldung = Tk()
        anmeldung.geometry('495x675')
        anmeldung.title('Anmeldung')
        anmeldung.resizable(0,0)
        anmeldung.configure(bg = 'black')
    def Aufrufen(self):
        global AnmCanvas, Anmeldebutton_enter_image, Anmeldebutton_image, Registerbutton_image, Registerbutton_enter_image
        global Hs_Logo, backbutton_anm_image, backbutton_enter_anm_image, bestätigen_anm_image, bestätigen_anm_enter_image
        global User, Position

        User = self

        #PhotoImages:
        pfad = 'Anmeldefenster_images/'
        BG = PhotoImage(file = pfad+'Anmeldung_bg.png')
        Anmeldebutton_image = PhotoImage(file = pfad+'Anmeldebutton.png')
        Anmeldebutton_enter_image = PhotoImage(file = pfad+'Anmeldebutton_enter.png')
        Registerbutton_image = PhotoImage(file = pfad+'registerbutton.png')
        Registerbutton_enter_image = PhotoImage(file = pfad+'registerbutton_enter.png')
        Hs_Logo = PhotoImage(file = pfad+'Hearthstone_Logo_Anmeldung1.png')
        backbutton_anm_image = PhotoImage(file = pfad+'backbutton_anm.png')
        backbutton_enter_anm_image = PhotoImage(file = pfad+'backbutton_enter_anm.png')
        bestätigen_anm_image = PhotoImage(file = pfad+'Bestätigen_anm.png')
        bestätigen_anm_enter_image = PhotoImage(file = pfad+'Bestätigen_anm_enter.png')

        Position = 'Hauptmenü'

        AnmCanvas = Canvas(anmeldung, width = 600, height = 800)
        AnmCanvas.place(x=0,y=0)
        AnmCanvas.create_image(250,338, image = BG, tags = 'Background')
        AnmCanvas.create_image(450, 200, image = Hs_Logo, tags = 'LOGO')
        AnmCanvas.create_image(250, 280, image = Anmeldebutton_image, tags = 'Anmeldebutton')
        AnmCanvas.create_image(250, 380, image = Registerbutton_image, tags = 'Registerbutton')            

        AnmCanvas.tag_bind('Anmeldebutton', '<Enter>', Anmeldebutton_enter)
        AnmCanvas.tag_bind('Anmeldebutton', '<Leave>', Anmeldebutton_leave)
        AnmCanvas.tag_bind('Registerbutton', '<Enter>', Registerbutton_enter)
        AnmCanvas.tag_bind('Registerbutton', '<Leave>', Registerbutton_leave)

        anmeldung.mainloop()

    def Window(self, Modus):
        if Modus == 'Exit' or Modus == 'Close':
            try:
                Name_eingabe.destroy()
            except:
                pass
            try:
                Passwort_eingabe.destroy()
            except:
                pass
            try:
                Passwort_eingabe2.destroy()
            except:
                pass
            anmeldung.destroy()
        elif Modus == 'OnlyBG':
            AnmCanvas.delete('Anmeldebutton', 'Registerbutton', 'LOGO')
    
        elif Modus == 'DelBG':
            AnmCanvas.delete('Background')

        elif Modus == "Clear_All":
            try:
                AnmCanvas.delete('Background')
            except:
                pass
            try:
                AnmCanvas.delete('LOGO')
            except:
                pass
            try:
                AnmCanvas.delete('Anmeldebutton', 'Registerbutton')
            except:
                pass
            try:
                Name_eingabe.destroy()
            except:
                pass
            try:
                Passwort_eingabe.destroy()
            except:
                pass
            try:
                Passwort_eingabe2.destroy()
            except:
                pass
            try:
                AnmCanvas.delete('Name')
            except:
                pass
            try:
                AnmCanvas.delete('Passwort')
            except:
                pass
            try:
                AnmCanvas.delete('Passwort2')
            except:
                pass

    def create_backbutton(self, Where):
        if Where == Position:
            AnmCanvas.create_image(150,110, image = backbutton_anm_image, tags = 'backbutton')
            AnmCanvas.tag_bind('backbutton', '<Enter>', backbutton_enter)
            AnmCanvas.tag_bind('backbutton', '<Leave>', backbutton_leave)
            

            
        else:
            print('"Where" must be "Position"\nWhere:',str(Where),'\nPosition:',str(Position))



def Analyze_Account():
    global Level, Gold, Packs, Staub, Ep, Epnextlevel
    command = ('select Level from Accounts where Name = ? and Passwort = ?')
    cursor.execute(command, (Name, Passwort))
    Level = cursor.fetchall()
    for i in Level:
        Level = i[0]

    command = ('select Gold from Accounts where Name = ? and Passwort = ?')  
    cursor.execute(command, (Name, Passwort))
    Gold = cursor.fetchall()
    for i in Gold:
        Gold = i[0]

    command = ('select Packs from Accounts where Name = ? and Passwort = ?')
    cursor.execute(command, (Name, Passwort))
    Packs = cursor.fetchall()
    for i in Packs:
        Packs = i[0]

    command = ('select Staub from Accounts where Name = ? and Passwort = ?')
    cursor.execute(command, (Name, Passwort))
    Staub = cursor.fetchall()
    for i in Staub:
        Staub = i[0]

    command = ('select Ep from Accounts where Name = ? and Passwort = ?')
    cursor.execute(command, (Name, Passwort))
    Ep = cursor.fetchall()
    for i in Ep:
        Ep = i[0]

    command = ('select Epnextlevel from Accounts where Name = ? and Passwort = ?')
    cursor.execute(command, (Name, Passwort))
    Epnextlevel = cursor.fetchall()
    for i in Epnextlevel:
        Epnextlevel = i[0]

def Account_Info(printing = False):
    global Infos
    Infos = ('Name: {}\nPasswort: {}\nLevel: {}\nGold: {}\nPacks: {}\nStaub: {}\nEp: {}\nEpnextlevel: {}'
             .format(Name, Passwort, Level, Gold, Packs , Staub, Ep, Epnextlevel))

    if printing:
        print(Infos)

def AfterLogin():
    global Name, Passwort
    fenster = anmeldung
    Name = Entry_Name
    Passwort = Entry_Passwort

    Analyze_Account()
    Account_Info(True)

    fenster.quit()
    #My windows    
    fenster.title('Hearthstone II')
    fenster.geometry('800x600')
    fenster.resizable(0,0)

    #Position des Users:
    POS = 'Hauptmenü'

    #My images
    pfad = 'HS_IMAGES/'
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
    shop_packs_image = PhotoImage(file = pfad+'shop_packs.png')
    shop_packs_enter_image = PhotoImage(file = pfad+'shop_packs_enter.png')
    settings_image = PhotoImage(file = pfad + 'settings_image.png')
    settings_enter_image = PhotoImage(file = pfad + 'settings_enter_image.png')
    

    fenster.iconbitmap(pfad+'hs_icon.ico')

    class MENU(object):
        def Aufrufen(Canv = False):
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
            def settings_enter(event):
                MyCanvas.itemconfigure('settings', image = settings_enter_image)
                MyCanvas.tag_bind('settings', '<Button-1>', Einstellungen)
            def settings_leave(leave):
                MyCanvas.itemconfigure('settings', image = settings_image)

            if Canvas:
                MyCanvas = Canvas(fenster, width = 800, height = 600)
                MyCanvas.place(x = 0, y = 0)
            MyCanvas.create_image(400,300, image = background1, tags = 'canv_background1')
            MyCanvas.create_image(400,105, image = Hearthstone_Logo, tags = 'canv_hearthstone_logo')
            MyCanvas.create_image(360,275, image = startbutton_image, tags = 'startbutton')
            MyCanvas.create_image(450,400, image = optionbutton_image, tags = 'optionbutton')
            MyCanvas.create_image(540,525, image = quitbutton_image, tags = 'quitbutton')
            MyCanvas.create_image(160, 550, image = shop_image, tags = 'shopbutton')
            MyCanvas.create_text(160, 480, text = 'Shop', font = ('Terminator Two', 30), fill = 'black', tags = 'shoptext')
            MyCanvas.create_image(600, 280, image = settings_image, tags = 'settings')

            MyCanvas.tag_bind('settings', '<Enter>', settings_enter)
            MyCanvas.tag_bind('settings', '<Leave>', settings_leave)
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
                    MyCanvas.delete('goldanzeige', 'packanzeige', 'backbutton', 'goldanzeige_text', 'packanzeige_text')
                    MyCanvas.delete('shop_packs', 'shop_packs_text')
                    Hauptmenü.Aufrufen()
                    POS = 'Hauptmenü'
            
            MyCanvas.tag_bind('backbutton', '<Enter>', backbutton_enter)
            MyCanvas.tag_bind('backbutton', '<Leave>', backbutton_leave)
            
    def Einstellungen(event):
        POS = 'Einstellungen'
    
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
        MyCanvas.create_text(480, 50, text = str(Gold), font = ('MelodBold', 10), tags = 'goldanzeige_text')
        MyCanvas.create_text(635, 50, text = str(Packs), font = ('MelodBold', 10), tags = 'packanzeige_text')
        MyCanvas.create_image(180, 230, image = shop_packs_image, tags = 'shop_packs')
        MyCanvas.create_text(175, 320, text = 'PACKS', font = ('MelodBold', 25), tags = 'shop_packs_text')
        MyCanvas.tag_bind('shop_packs', '<Enter>', shop_packs_enter)
        MyCanvas.tag_bind('shop_packs', '<Leave>', shop_packs_leave)
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

    def shop_packs_enter(event):
        MyCanvas.itemconfigure('shop_packs', image = shop_packs_enter_image)
        MyCanvas.itemconfigure('shop_packs_text', fill = 'white')
        MyCanvas.tag_bind('shop_packs', '<Button-1>', shop_packs_func)
    def shop_packs_leave(event):
        MyCanvas.itemconfigure('shop_packs_text', fill = 'black')
        MyCanvas.itemconfigure('shop_packs', image = shop_packs_image)

    def shop_packs_func(event):
        print('Packs!')

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
        os._exit(1)


    Hauptmenü = MENU
    Backbutton = BACKBUTTON
    Hauptmenü.Aufrufen(Canv = True)
    fenster.mainloop()


Top = Anmeldefenster()
Top.Aufrufen()
