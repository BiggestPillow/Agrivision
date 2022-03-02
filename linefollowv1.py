
# from tkinter import *
# from math import *
# if __name__ == "__main__":
#     root=Tk()
#     canvas=Canvas(root,width=800,height=300,bg="white")
#     canvas.pack()
#     canvas.create_line(0,150,800,150)
#     root.mainloop()
from tkinter import *
import time
from random import*
from math import*

class Ball:
    def __init__(self,canvas,**kw):
        self.canvas = canvas
        self.radius = kw.get('radius',20)
        self.pos_x = kw.get('pos_x',0)
        self.pos_y = kw.get('pos_y',0)
        self.color = kw.get('color','red')
        self.create()

    def calculate_ball_pos(self):
        x1 = self.pos_x
        x2 = self.pos_x + self.radius
        y1 = self.pos_y
        y2 = self.pos_y + self.radius
        return x1,y1,x2,y2

    def create(self):
        coords = self.calculate_ball_pos()
        self.ball = self.canvas.create_oval(coords[0],coords[1],coords[2],coords[3])
        self.canvas.itemconfig(self.ball, fill=self.color)

    def move(self,x=0,y=0):
        self.pos_x += x
        self.pos_y += y        
        coords = self.calculate_ball_pos()
        self.canvas.coords(self.ball,coords[0],coords[1],coords[2],coords[3])

    def runsim(self):
         x=ball.calculate_ball_pos()[0]
         while x<w-50:
             y=ball.calculate_ball_pos()[1]
             x=ball.calculate_ball_pos()[0]
             proportion=150-y-10
             pweight=proportion/10+10
             speed=abs(10-abs(h/2-y)/10)
             if y >h/2:
                 ball.move(speed,pweight)
             elif y<h/2:
                 ball.move(speed,pweight)
             else:
                 ball.move(speed,enviornment)
             mainCanvas.create_oval(x+10,y+10,x+2+10,y+2+10)
             root.update()
             root.after(100)

def keypress(event):
    print(event)
    if event.char == 'w':
        ball.move(0,-5)
    elif event.char == 's':
        ball.move(0,5)
    elif event.char == 'a':
        ball.move(-5,0)
    elif event.char == 'd':
        ball.move(5,0)
    elif event.char =='t':
        ball.runsim()
    else:
        pass

w=800
h=500
if __name__ == "__main__":
    root = Tk()
    mainCanvas = Canvas(root, width=w, height=h)
    root.bind('w',keypress)
    root.bind('s',keypress)
    root.bind('a',keypress)
    root.bind('d',keypress)
    root.bind('t',keypress)
    mainCanvas.create_line(50,h/2,w,h/2)
    mainCanvas.grid()
    ball = Ball(mainCanvas,pos_x=50,pos_y=50)

    root.mainloop()