from tkinter import *


def motion(event):
    c.move(ball, 1, 0)
    if c.coords(ball)[2] < 300:
        root.after(10, motion)


root = Tk()
c = Canvas(root, width=300, height=300, bg="white")
c.pack()
ball = c.create_oval(0, 100, 40, 140, fill='orange')

but1 = Button(text='Move')
but1.bind('<Button-1>', motion)
but1.pack()

root.mainloop()