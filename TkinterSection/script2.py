from tkinter import *


def kg_to_others():
    kg = float(entry_value.get())

    grams = kg * 1000
    pounds = kg * 2.20462
    ounces = kg * 35.274

    t1.delete("1.0", END)
    t1.insert(END, grams)
    t2.delete("1.0", END)
    t2.insert(END, pounds)
    t3.delete("1.0", END)
    t3.insert(END, ounces)


window = Tk()
#  Create the "convert" button
b1 = Button(window, text="Convert from Kg", command=kg_to_others)
b1.grid(row=0, column=0)

#  Create the entry cell
entry_value = StringVar()
entry = Entry(window, textvariable=entry_value)
entry.grid(row=0, column=1)

#  Create the text cells
t1 = Text(window, height=5, width=50)
t1.grid(row=1, column=0)

t2 = Text(window, height=5, width=50)
t2.grid(row=1, column=1)

t3 = Text(window, height=5, width=50)
t3.grid(row=1, column=2)

window.mainloop()
