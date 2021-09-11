from tkinter import *

def add_item(event):
    selected = list(lbox1.curselection())
    for i in selected:
        lbox2.insert("end", i)
        lbox1.delete(i)

def remove_item(event):
    selected = list(lbox2.curselection())
    lbox1.insert("end", selected)  #
    for i in selected:
        lbox2.delete(i)

root = Tk()

lbox1 = Listbox(selectmode="extended", width=20, height=10)
lbox2 = Listbox(selectmode="extended", width=20, height=10)
for i in ('rose', 'daisy', 'lily', 'peony', 'violet', 'lilac'):
    lbox1.insert(0, i)

but1 = Button(width=5, height=3, text='>>')
but2 = Button(width=5, height=3, text='<<')
but1.bind('<Button-1>', add_item)
but2.bind('<Button-1>', remove_item)
lbox1.grid()
but1.grid()
but2.grid()
lbox2.grid()

root.mainloop()