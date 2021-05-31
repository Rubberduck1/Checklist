from tkinter import *
from PIL import ImageTk, Image
import csv


root = Tk()
root.title('Fahrzeugkontrolle')
root.geometry('500x1000')
#root.iconbitmap('bus.png')

kfz = StringVar()
kfz.set("prove")

with open('PostDummy.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')

    next(csv_reader)
    
    for line in csv_reader:
        x = (line[3])
        y = (line[1])
        z = (x + ",   " + y)
        Radiobutton(root, text=x, variable=kfz, value=z).pack(anchor=W)


def clicked(value):
    myLabel = Label(root, text=value)
    myLabel.pack()

myLabel = Label(root, text=kfz.get())
myLabel.pack()

myButton = Button(root, text="OK", command=lambda: clicked(kfz.get()))
myButton.pack()

root.mainloop()