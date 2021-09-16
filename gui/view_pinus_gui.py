from tkinter import *
import tkinter.messagebox

root = Tk()
root.geometry('700x500')
root.title("View pinus")

menubar = Menu(root)
root.config(menu=menubar)
submenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Help", menu=submenu)
submenu.add_command(label="About Us", command= lambda : tkinter.messagebox.showinfo("View pinus", "Version 69.420"))

Label(root, text="Pinus length:").pack()

e = Entry(root, borderwidth=2, textvariable=IntVar(value=12))
e.pack()

def f():
    try:
        l = int(e.get())
    except ValueError:
        tkinter.messagebox.showerror("Get a real pp", "Length has to be positive integer!")
        return

    global plabel
    if l <= 0:
        p = ''
        tkinter.messagebox.showwarning("Get a bigger pp", "Too small pp")
    elif l > 420:
        p = ''
        tkinter.messagebox.showwarning("Too big", "Whoa! Slow down dude!")
    else:
        p = "8" + "="*l + "D"
    plabel['text'] = p
    return p

photo = PhotoImage(file="D:\code\python\\view-pinus\pinus.png")
Button(root, text="View", image=photo, command=f).pack()

plabel = Label(root, text='', pady=5)
plabel.pack()

root.mainloop()