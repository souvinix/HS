from tkinter import *
import sqlite3
from Account import *
#from Hs2 import Login

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
            AfterLogin()
            #anmeldung.destroy()
                        
            
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
    if Position == 'Anmelden':
        User.Window('OnlyBG')
        User.Aufrufen()
        try:
            Name_eingabe.destroy()
            Passwort_eingabe.destroy()
            AnmCanvas.delete('Name', 'Passwort', 'Bestätigen')
        except:
            pass
        
    elif Position == 'Registrieren':
        User.Window('OnlyBG')
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

                

    def create_backbutton(self, Where):
        if Where == Position:
            AnmCanvas.create_image(150,110, image = backbutton_anm_image, tags = 'backbutton')
            AnmCanvas.tag_bind('backbutton', '<Enter>', backbutton_enter)
            AnmCanvas.tag_bind('backbutton', '<Leave>', backbutton_leave)
            

            
        else:
            print('"Where" must be "Position"\nWhere:',str(Where),'\nPosition:',str(Position))



