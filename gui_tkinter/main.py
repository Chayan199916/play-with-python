from tkinter import *

window = Tk()


def perform():
    t1.delete('1.0', END)
    t2.delete('1.0', END)
    t3.delete('1.0', END)
    result1 = str(round(float(e1_val.get()) * 1000, 3)) + ' grams'
    result2 = str(round(float(e1_val.get()) * 2.204, 3)) + ' pounds'
    result3 = str(round(float(e1_val.get()) * 35.27, 3)) + ' ounces'
    t1.insert(END, result1)
    t2.insert(END, result2)
    t3.insert(END, result3)

# b1 = Button(window, text = "Execute", command = perform)
# b1.grid(row = 0, column = 0)

# e1_val = StringVar()
# e1 = Entry(window, textvariable = e1_val)
# e1.grid(row = 0, column = 1)

# t1 = Text(window, height = 1, width = 10)
# t1.grid(row = 0, column = 20)

l1 = Label(window, text = "Kg")
l1.grid(row = 0, column = 0)

e1_val = StringVar()
e1 = Entry(window, textvariable = e1_val)
e1.grid(row = 0, column = 1)

b1 = Button(window, text = "Convert", command = perform)
b1.grid(row = 0, column = 2)

t1 = Text(window, height = 1, width = 20)
t1.grid(row = 1, column = 0)

t2 = Text(window, height = 1, width = 20)
t2.grid(row = 1, column = 1)

t3 = Text(window, height = 1, width = 20)
t3.grid(row = 1, column = 2)

window.mainloop()