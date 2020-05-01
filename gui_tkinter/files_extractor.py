from tkinter import *
import os

window = Tk(className="Files extractor")
window.minsize(500, 300)

def extract():
    t1.delete('1.0', END)
    file_name = e1_val.get()
    result = ''
    if len(file_name) != 0:
        for root, dirs, files in os.walk(file_name, topdown=True):
            for name in files:
                result = result + os.path.join(root, name) + '\n'
            for name in dirs:
                result = result + os.path.join(root, name) + '\n'
        t1.insert(END, result)
    else:
        t1.insert(END, 'NO PATH GIVEN')



l1 = Label(window, text = "Files Extractor", font = ('Verdana', 15))
l1.pack()

e1_val = StringVar()
e1 = Entry(window, textvariable = e1_val, width = 100)
e1.pack()

b1 = Button(window, text = "Extract", command = extract, font = ('Verdana', 15))
b1.pack()

xscrollbar = Scrollbar(window, orient = HORIZONTAL)
xscrollbar.pack(side = BOTTOM, fill = X)

yscrollbar = Scrollbar(window)
yscrollbar.pack(side = RIGHT, fill = Y)

t1 = Text(window, xscrollcommand = xscrollbar.set, yscrollcommand = yscrollbar.set)
t1.pack()

xscrollbar.config(command = t1.xview)
yscrollbar.config(command = t1.yview)

window.mainloop()