import tkinter as tk
from turtle import width
#my_w = my window, d= dimention, c= canvas, b=button, r=rectangle
my_w = tk.Tk()
width, height = 810, 610 # set the variables
c_width, c_height = width-10, height-45

d = str(width) + 'x' + str(height)
my_w.geometry(d)
c1=tk.Canvas(my_w, width=c_width, height=c_height, bg='lightpink')
c1.grid(row=1, column=0, padx=5, pady=5)

step = 5
x1,y1 = 5, int(c_height/2)
x2,y2 = x1+30, y1+30
r1 = c1.create_rectangle(x1,y1,x2,y2,fill='grey')

def my_move(event):
    c1.move(r1,step,step)

b1=tk.Button(my_w, text='Move', bg='lightblue', font=14, command=lambda:my_move('x'))
b1.grid(row=2, column=0)

my_w.mainloop()

