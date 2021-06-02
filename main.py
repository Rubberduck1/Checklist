import tkinter as tk
import csv
 
 
def yield_csv(file_path):
    with open(file_path, 'r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for line in csv_reader:
            yield line
 
 
class App(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title('Fahrzeugkontrolle')
        self.geometry('500x500')
        self.string_var = tk.StringVar()
        self.string_var.set("prove")
        self.r_btns = {}
 
        csv_ = yield_csv('PostDummy.csv')
        next(csv_)
        for line in csv_:
            value = f'{line[3]}, {line[1]}'
            r_btn = tk.Radiobutton(self, text=line[3],
                                   variable=self.string_var, value=value)
            r_btn.pack(anchor=tk.W)
            self.r_btns[value] = r_btn
 
        myLabel = tk.Label(self, text=self.string_var.get())
        myLabel.pack()
 
        myButton = tk.Button(self, text="OK", command=self.on_btn)
        myButton.pack()
 
    def on_btn(self):
        value = self.string_var.get()
        myLabel = tk.Label(self, text=value)
        myLabel.pack()
        self.r_btns[value].destroy()
 
 
if __name__ == '__main__':
    app = App()
    app.mainloop()