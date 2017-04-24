from tkinter import *

class Anmeldefenster(object):
    def Aufrufen(self):
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

        Anm_Canvas = Canvas(anmeldung, width = 600, height = 800)
        Anm_Canvas.place(x=0,y=0)
        Anm_Canvas.create_image(250,338, image = BG, tags = 'Anm_bg')
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
            
        def Anmeldebutton_function(event):
            pass
        def Registerbutton_function(event):
            pass

        Anm_Canvas.tag_bind('Anmeldebutton', '<Enter>', Anmeldebutton_enter)
        Anm_Canvas.tag_bind('Anmeldebutton', '<Leave>', Anmeldebutton_leave)
        Anm_Canvas.tag_bind('Registerbutton', '<Enter>', Registerbutton_enter)
        Anm_Canvas.tag_bind('Registerbutton', '<Leave>', Registerbutton_leave)

        anmeldung.mainloop()

    def Schließen(self):
        Anm_Canvas.destroy()
        pfad = ''
        anmeldung.destroy()

This = Anmeldefenster()
This.Aufrufen()



