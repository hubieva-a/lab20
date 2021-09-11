from tkinter import *

def add_to_listbox(event):
    a = text1.get(1.0, "end")
    lbox1.insert("end", a)
    text1.delete(1.0, "end")

def add_to_text(event):
    for i in lbox1.curselection():
        lbox1.get(i)
        text1.insert(END, i)
        lbox1.delete(i)

root = Tk()
text1 = Text(height=1, width=20)
lbox1 = Listbox(width=20, selectmode="single")
text1.bind('<Return>', add_to_listbox)
lbox1.bind('<Double-Button-1>', add_to_text)
text1.pack()
lbox1.pack()

root.mainloop()