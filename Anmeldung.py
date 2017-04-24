from tkinter import *

class Anmeldefenster(object):
    def Aufrufen(self, Nda=0):
        global Anm_Canvas, backbutton_anm_image, backbutton_enter_anm_image, anm_pos, anmeldung
        global anm_pos, Passwort_eingabe, Name_eingabe

        def Anmeldebutton_function(event):
            global anm_pos, Passwort_eingabe, Name_eingabe, Anm_Canvas
            self.Schließen('All-BG')
            self.create_backbutton()
            anm_pos = 'Anmelden'

            Anm_Canvas.create_text(250, 170, text = 'Name:', font = ('Terminator Two', 20), tags = 'Name')
            Name_eingabe = Entry(bd = 15, width = 10, font = ('Terminator Two', 20), bg = '#8B591C')
            Name_eingabe.place(x = 150, y = 200)

            Anm_Canvas.create_text(250, 310, text = 'Passwort', font = ('Terminator Two', 20), tags = 'Passwort')
            Passwort_eingabe = Entry(bd = 15, width = 10, font = ('Terminator Two', 20), bg = '#8B591C', show = '*')
            Passwort_eingabe.place(x = 150, y = 330)

            Anm_Canvas.create_image(250, 480, image = bestätigen_anm_image, tags = 'Bestätigen')
            

            def bestätigen_enter(event):
                Anm_Canvas.itemconfigure('Bestätigen', image = bestätigen_anm_enter_image)
                Anm_Canvas.tag_bind('Bestätigen', '<Button-1>', bestätigen_func)
            def bestätigen_leave(event):
                Anm_Canvas.itemconfigure('Bestätigen', image = bestätigen_anm_image)

            def bestätigen_func(event):
                pass

            
            Anm_Canvas.tag_bind('Bestätigen', '<Enter>', bestätigen_enter)
            Anm_Canvas.tag_bind('Bestätigen', '<Leave>', bestätigen_leave)

            
        def Registerbutton_function(event):
            global anm_pos
            anm_pos = 'Registrieren'
            self.Schließen('All-BG')
            self.create_backbutton()
        
        if Nda == 0:
            
            anm_pos = 'Hauptmenü'
            anmeldung = Tk()
            anmeldung.geometry('495x675')
            anmeldung.title('Anmeldung')
            anmeldung.resizable(0,0)
            anmeldung.configure(bg = 'black')

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

            Anm_Canvas = Canvas(anmeldung, width = 600, height = 800)
            Anm_Canvas.place(x=0,y=0)
            Anm_Canvas.create_image(250,338, image = BG, tags = 'Anm_bg')
            Anm_Canvas.create_image(450, 200, image = Hs_Logo, tags = 'HS_LOGO')
            Anm_Canvas.create_image(250, 280, image = Anmeldebutton_image, tags = 'Anmeldebutton')
            Anm_Canvas.create_image(250, 380, image = Registerbutton_image, tags = 'Registerbutton')

            def Anmeldebutton_enter(event):
                Anm_Canvas.itemconfigure('Anmeldebutton', image = Anmeldebutton_enter_image)
                Anm_Canvas.tag_bind('Anmeldebutton', '<Button-1>', Anmeldebutton_function)
            def Anmeldebutton_leave(event):
                Anm_Canvas.itemconfigure('Anmeldebutton', image = Anmeldebutton_image)
            def Registerbutton_enter(event):
                Anm_Canvas.itemconfigure('Registerbutton', image = Registerbutton_enter_image)
                Anm_Canvas.tag_bind('Registerbutton', '<Button-1>', Registerbutton_function)
            def Registerbutton_leave(event):
                Anm_Canvas.itemconfigure('Registerbutton', image = Registerbutton_image)
                

            Anm_Canvas.tag_bind('Anmeldebutton', '<Enter>', Anmeldebutton_enter)
            Anm_Canvas.tag_bind('Anmeldebutton', '<Leave>', Anmeldebutton_leave)
            Anm_Canvas.tag_bind('Registerbutton', '<Enter>', Registerbutton_enter)
            Anm_Canvas.tag_bind('Registerbutton', '<Leave>', Registerbutton_leave)

            anmeldung.mainloop()
            
        elif Nda == 1:

            pfad = 'Anmeldefenster_images/'
            BG = PhotoImage(file = pfad+'Anmeldung_bg.png')
            Anmeldebutton_image = PhotoImage(file = pfad+'Anmeldebutton.png')
            Anmeldebutton_enter_image = PhotoImage(file = pfad+'Anmeldebutton_enter.png')
            Registerbutton_image = PhotoImage(file = pfad+'registerbutton.png')
            Registerbutton_enter_image = PhotoImage(file = pfad+'registerbutton_enter.png')
            Hs_Logo = PhotoImage(file = pfad+'Hearthstone_Logo_Anmeldung1.png')
            backbutton_anm_image = PhotoImage(file = pfad+'backbutton_anm.png')
            backbutton_enter_anm_image = PhotoImage(file = pfad+'backbutton_enter_anm.png')
            
            Anm_Canvas.create_image(250,338, image = BG, tags = 'Anm_bg')
            Anm_Canvas.create_image(450, 200, image = Hs_Logo, tags = 'HS_LOGO')
            Anm_Canvas.create_image(250, 280, image = Anmeldebutton_image, tags = 'Anmeldebutton')
            Anm_Canvas.create_image(250, 380, image = Registerbutton_image, tags = 'Registerbutton')

            def Anmeldebutton_enter(event):
                Anm_Canvas.itemconfigure('Anmeldebutton', image = Anmeldebutton_enter_image)
                Anm_Canvas.tag_bind('Anmeldebutton', '<Button-1>', Anmeldebutton_function)
            def Anmeldebutton_leave(event):
                Anm_Canvas.itemconfigure('Anmeldebutton', image = Anmeldebutton_image)
            def Registerbutton_enter(event):
                Anm_Canvas.itemconfigure('Registerbutton', image = Registerbutton_enter_image)
                Anm_Canvas.tag_bind('Registerbutton', '<Button-1>', Registerbutton_function)
            def Registerbutton_leave(event):
                Anm_Canvas.itemconfigure('Registerbutton', image = Registerbutton_image)
            

            Anm_Canvas.tag_bind('Anmeldebutton', '<Enter>', Anmeldebutton_enter)
            Anm_Canvas.tag_bind('Anmeldebutton', '<Leave>', Anmeldebutton_leave)
            Anm_Canvas.tag_bind('Registerbutton', '<Enter>', Registerbutton_enter)
            Anm_Canvas.tag_bind('Registerbutton', '<Leave>', Registerbutton_leave)

            anmeldung.mainloop()

    def Schließen(self, Modus):
        if Modus == 'All':
            anmeldung.destroy()
        elif Modus == 'All-BG':
            Anm_Canvas.delete('Anmeldebutton', 'Registerbutton', 'HS_LOGO')
        elif Modus == 'BG':
            Anm_Canvas.delete('Anm_bg')

    def create_backbutton(self):
        global anm_pos, Passwort_eingabe, Name_eingabe, Anm_Canvas
        Anm_Canvas.create_image(150,110, image = backbutton_anm_image, tags = 'backbutton')
        def backbutton_enter(event):
            Anm_Canvas.itemconfigure('backbutton', image = backbutton_enter_anm_image)
            Anm_Canvas.tag_bind('backbutton', '<Button-1>', backbutton_func)

        def backbutton_leave(event):
            Anm_Canvas.itemconfigure('backbutton', image = backbutton_anm_image)

        def backbutton_func(event):
            global anm_pos, Passwort_eingabe, Name_eingabe 
            if anm_pos == 'Anmelden':
                self.Schließen('BG')
                self.Aufrufen(1)
                Name_eingabe.destroy()
                Passwort_eingabe.destroy()
                Anm_Canvas.delete('Name', 'Passwort', 'Bestätigen')
            elif anm_pos == 'Registrieren':
                self.Schließen('BG')
                self.Aufrufen(1)
            
        
        Anm_Canvas.tag_bind('backbutton', '<Enter>', backbutton_enter)
        Anm_Canvas.tag_bind('backbutton', '<Leave>', backbutton_leave)
        

This = Anmeldefenster()
This.Aufrufen()
