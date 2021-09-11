from tkinter import *

def change_size(event):
    a = textbox1.get(1.0,"end")
    a = int(a)
    textbox3['width'] = a
    b = textbox2.get(1.0, "end")
    b = int(b)
    textbox3['height'] = b

def focus_in(event):
    textbox3['bg'] = 'white'

def focus_out(event):
    textbox3['bg'] = 'lightgrey'

root = Tk()

textbox1 = Text(width=10, height=1)
textbox2 = Text(width=10, height=1)
but1 = Button(text='Изменить',width=20)
textbox3 = Text(width=30, bg='lightgrey')

but1.bind('<Button-1>', change_size)
but1.bind('<Return>', change_size)
textbox3.bind('<FocusIn>', focus_in)
textbox3.bind('<FocusOut>', focus_out)
textbox1.pack()
textbox2.pack()
but1.pack()
textbox3.pack()

root.mainloop()
