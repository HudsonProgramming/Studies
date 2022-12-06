import tkinter as tk
from tkinter import *
#from PIL import ImageTK,Image

class MainGUI:
    def __init__(self):

        self.window = tk.Tk()
        self.window.geometry("500x300")
        self.window.title("Tkinter Application")
        self.window.configure(bg="grey15")

        # Remove Title Bar
        self.window.overrideredirect(True)

        # Move Window
        def move_app(e):
            self.window.geometry(f"+{e.x_root}+{e.y_root}")
        
        # Create Fake Title Bar
        self.titlebar = Frame(self.window, bg="grey7", relief="raised")
        self.titlebar.pack(expand=0, side=TOP, fill=X)

        # Bind Title Bar
        self.titlebar.bind("<B1-Motion>", move_app)        

        # Title Bar Text       
        self.titlebar_label = Label(self.titlebar, text="TEST APPLICATION 01", bg="grey7",fg="white")
        self.titlebar_label.pack(side=LEFT, pady=2)

        # Title Bar Exit Button
        self.titlebar_exit_btn = Button(self.titlebar, text="  X  ", bg="grey7",fg="white", relief="raised", command=quit)
        self.titlebar_exit_btn.pack(side=RIGHT, pady=2)

        # Create Exit Button
        self.titlebar_exit_btn = Button(self.window, text="Close.", font=("Helvetica",12), command=quit)
        self.titlebar_exit_btn.pack(pady=100)

        self.window.mainloop()

MainGUI()

