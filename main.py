from tkinter import *
from PIL import ImageTk, Image
import csv
'''
with open('PostDummy.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')

    next(csv_reader)
    
    for line in csv_reader:
        x = (line[3])
        #y = (line[1])
        #print(x, y)
'''



root = Tk()
root.title('Fahrzeugkontrolle')
#root.iconbitmap()

#r = StringVar()
#r.set("prove")
'''
MODES = [
    ("2545", "2545"),
    ("3254", "3254"),
    ("5522", "5522"),
    ("5548", "5548"),
]
'''

kfz = StringVar()
kfz.set("prove")

with open('PostDummy.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')

    next(csv_reader)
    
    for line in csv_reader:
        x = (line[3])
        Radiobutton(root, text=x, variable=kfz, value=x).pack(anchor=W)


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