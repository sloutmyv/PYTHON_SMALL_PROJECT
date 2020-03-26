###############################################################################
# Date ! 27/03/2020
# Auteur : SYC
# Comment : Just some balls in a windows
###############################################################################



from tkinter import *
from random import randint

# class
class Ball:
    def __init__(self, canvas, x1,y1,x2,y2,dx,dy):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.dx = dx
        self.dy = dy
        self.canvas = canvas
        self.ball = canvas.create_oval(self.x1,self.y1,self.x2,self.y2, fill="red")
        self.active = True
        self.move_active()

    def move_ball(self):
        self.canvas.move(self.ball,self.dx,self.dy)
        pos = self.canvas.coords(self.ball)
        if pos[3] > HEIGHT or pos[1] <=0:
            self.dy = -self.dy
        if pos[2] > WIDTH or pos[0] <=0:
            self.dx = -self.dx

    def move_active(self):
        if self.active:
            self.move_ball()
            self.canvas.after(5, self.move_active)



# global WIDTH
# global HEI/GHT
WIDTH = 500
HEIGHT = 500
DIAM_BALLS = 20
NB_BALLS = 10

# initialize root window and canvas
window = Tk()
window.title("Title")
window.resizable(False,False)

canvas = Canvas(window, width=WIDTH, height=HEIGHT) # canvas = zone de dessin
canvas.pack()

# create balls
balls = []
for i in range(NB_BALLS):
    x1 = randint(0,WIDTH-DIAM_BALLS)
    y1 = randint(0,HEIGHT-DIAM_BALLS)
    x2 = x1+20
    y2 = y1+20
    dx = 1
    dy = 1
    balls.append(Ball(canvas,x1,y1,x2,y2,dx,dy))

window.mainloop()
