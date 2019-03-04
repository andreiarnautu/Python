"""
The program will store the following information about the books:
    -> Title, Author
    -> Year, ISBN

User commands:
    (1) view all records
    (2) search an entry
    (3) add an entry
    (4) update an entry
    (5) close the window
"""

from tkinter import *

window = Tk()

#  Labels and text entries
title_label = Label(window, text = "Title")
title_label.grid(row=0, column=0)

author_label = Label(window, text = "Author")
author_label.grid(row=0, column=2)

year_label = Label(window, text = "Year")
year_label.grid(row=1, column=0)

isbn_label = Label(window, text = "ISBN")
isbn_label.grid(row=1, column=2)

title_text = StringVar()
title_entry = Entry(window, textvariable=title_text)
title_entry.grid(row=0, column=1)

author_text = StringVar()
author_entry = Entry(window, textvariable=author_text)
author_entry.grid(row=0, column=3)

year_text = StringVar()
year_entry = Entry(window, textvariable=year_text)
year_entry.grid(row=1, column=1)

isbn_text = StringVar()
isbn_entry = Entry(window, textvariable=isbn_text)
isbn_entry.grid(row=1, column=3)

#  The listbox and its scrollbar
list_box = Listbox(window, height=6, width=35)
list_box.grid(row=2, column=0, rowspan=6, columnspan=2)

scrollbar = Scrollbar(window)
scrollbar.grid(row=2, column=2, rowspan=6)

#  Attach the scrollbar to the listbox
list_box.configure(yscrollcommand=scrollbar.set)
scrollbar.configure(command=list_box.yview)

#  Create the buttons
button_1 = Button(window, text="View all", width=12)
button_1.grid(row=2, column=3)

button_2 = Button(window, text="Search entry", width=12)
button_2.grid(row=3, column=3)

button_3 = Button(window, text="Add entry", width=12)
button_3.grid(row=4, column=3)

button_4 = Button(window, text="Update selected", width=12)
button_4.grid(row=5, column=3)

button_5 = Button(window, text="Delete selected", width=12)
button_5.grid(row=6, column=3)

button_6 = Button(window, text="Close", width=12)
button_6.grid(row=7, column=3)

window.mainloop()
