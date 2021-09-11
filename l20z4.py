from tkinter import *

root = Tk()

new_canvas = Canvas(root, width=200, height=200, bg='#00008B')
new_canvas.pack()

new_canvas.create_oval(180, 20, 130, 70, width=2, fill='white')
new_canvas.create_rectangle(60, 90, 140, 190, fill='grey')
new_canvas.create_polygon(100, 10, 40, 90, 160, 90, fill='orange')

a = 0
b = 10
k = 1
while k <= 40:
    a += 5
    b += 5
    k +=1
    new_canvas.create_line(a, 200, b, 180, fill='orange')

root.mainloop()