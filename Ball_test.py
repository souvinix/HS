from tkinter import *
from random import *

class Ball:
    def __init__(self, canvas, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.canvas = canvas
        self.ball = canvas.create_oval(self.x1, self.y1, self.x2, self.y2, fill="red", tags = 'ball')

    def move_ball(self):
        deltax = 1
        deltay = 1
        self.canvas.move(self.ball, deltax, deltay)
        self.canvas.after(40, self.move_ball)

    def return_ball(self):
        #self.canvas.move(self.ball, - 20, -20)
        print('Ball')
        
    def Ball_bind(self):
        self.canvas.tag_bind('ball', '<Enter>', self.return_ball)
    
# initialize root Window and canvas
root = Tk()
root.title("Balls")
canvas = Canvas(root, width = 1000, height = 1000)
canvas.pack()

# create two ball objects and animate them
ball1 = Ball(canvas, 10, 10, 30, 30)

ball1.move_ball()
ball1.Ball_bind()

root.mainloop()
