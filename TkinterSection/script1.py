from tkinter import *


def km_to_miles():
    miles= float(e1_value.get()) * 1.6
    t1.insert(END,miles)


#  Create a new window.
window = Tk()

b1 = Button(window, text="Execute", command=km_to_miles)
b1.grid(row=0, column=0)

e1_value=StringVar()
e1 = Entry(window, textvariable=e1_value)
e1.grid(row=0, column=1)

t1 = Text(window, height=5, width=50)
t1.grid(row=1, column=0)

#  Make the window stay up instead of being closed immediately after being created.
window.mainloop()
