from tkinter import *
from tkinter import ttk

# function calculating feet to metres
def calculate(*args):
    try:
        value = float(feet.get())
        metres.set(int(0.3048 * value * 10000.0 + 0.5) / 10000.0)
    except ValueError:
        pass

# set up window
root = Tk()
root.title('Feet to Metres')

mainframe = ttk.Frame(root, padding='3 3 12 12')
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

# setting up the feet variables
feet = StringVar()
feet_entry = ttk.Entry(
    mainframe, 
    width=7,
    textvariable=feet    
)
feet_entry.grid(
    column=2,
    row=1,
    sticky=(W, E)
)

# setting up the metres variable
metres = StringVar()
ttk.Label(
    mainframe,
    textvariable=metres).grid(column=2, row=2, sticky=(W, E))


ttk.Button(
    mainframe,
    text='Calculate',
    command=calculate).grid(column=3, row=3, sticky=W)

ttk.Label(mainframe, text='feet').grid(column=3, row=1, sticky=W)

ttk.Label(mainframe, text='is equivalent to').grid(column=1, row=2, sticky=W)

ttk.Label(mainframe, text='metres').grid(column=3, row=2, sticky=W)

# looping thru the child components (Labels, Button etc) to add padding to avoid the app looking scrunched up
for child in mainframe.winfo_children():
    child.grid_configure(padx=5, pady=5)

# putting the focus on the feet_entry field places the cursor inside the field for the user
feet_entry.focus()

# when the user presses the return key, the calculate function is called just as if the Calculate button is clicked
root.bind('<Return>', calculate)

# starts the event loop
root.mainloop()