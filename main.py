from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('Fahrzeugkontrolle')
#root.iconbitmap()

#r = StringVar()
#r.set("prove")

MODES = [
    ("2545", "2545"),
    ("3254", "3254"),
    ("5522", "5522"),
    ("5548", "5548"),
]

kfz = StringVar()
kfz.set("prove")

for text, mode in MODES:
    Radiobutton(root, text=text, variable=kfz, value=mode).pack(anchor=W)



def clicked(value):
    myLabel = Label(root, text=value)
    myLabel.pack()

#Radiobutton(root, text="Checked", variable=r, value="1", command=lambda: clicked(r.get())).pack()
#Radiobutton(root, text="Checked", variable=r, value="2", command=lambda: clicked(r.get())).pack()

myLabel = Label(root, text=kfz.get())
myLabel.pack()

myButton = Button(root, text="OK", command=lambda: clicked(kfz.get()))
myButton.pack()

root.mainloop()   

'''
root.geometry("500x500")

def show():
    myLabel = Label(root, text=var.get()).pack_info


var = StringVar()

c = Checkbutton(root, text="Checked", variable=var, onvalue="Yes", offvalue="No")
c.deselect()
c.pack()

#myButton = Button(root, text="Show Selection", command=show).pack()

root.mainloop()
'''