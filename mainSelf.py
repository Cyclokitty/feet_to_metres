from tkinter import *
from tkinter import ttk
from turtle import st

class FeetToMetres:
    def __init__(self, root):
        
        root.title('Feet to Metres')

        mainframe = ttk.Frame(root, padding='3 3 12 12')
        mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)

        self.feet = StringVar()
        feet_entry = ttk.Entry(mainframe, width=7, textvariable=self.feet)
        feet_entry.grid(column=2, row=1, sticky=(W, E))

        self.metres = StringVar()

        ttk.Label(mainframe, textvariable=self.metres).grid(column=2, row=2, sticky=(W, E))

        ttk.Button(mainframe, text='Calculate', command=self.calculate).grid(column=3, row=3, sticky=W)

        ttk.Label(mainframe, text='feet').grid(column=3, row=1, sticky=W)

        ttk.Label(mainframe, text='is equivalent to').grid(column=1, row=2, sticky=E)
        
        ttk.Label(mainframe, text='metres').grid(column=3, row=2, sticky=W)

        for child in mainframe.winfo_children():
            child.grid_configure(padx=5, pady=5)

        feet_entry.focus()
        root.bind('<Return>', self.calculate)

    def calculate(self, *args):
        try:
            value = float(self.feet.get())
            self.metres.set(int(0.3048 * value * 10000.0 + 0.5)/10000.0)
        except ValueError:
            pass
root= Tk()
FeetToMetres(root)
root.mainloop()