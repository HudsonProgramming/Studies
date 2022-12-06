from tkinter import *

root = Tk()

#///////////////////////////////////////////////
'''
# Creating Label Widgets
myLabel1 = Label(root, text="Hello World!")
myLabel2 = Label(root, text="!dlroW olleH")


# Placing Widgets on screen
myLabel1.grid(row=0,column=0)
myLabel2.grid(row=1,column=1)
'''
#///////////////////////////////////////////////

# Creating an entry/inputbox Widget
e = Entry(root,width=50,borderwidth=5,fg="white",bg="grey")
e.pack()
e.insert(0,"Enter Your Name: ")

# Creating a function for clicking myButton1
def myClick():
    # Creating a variable called "hello" and using the .get function to get input.
    hello = "Hello " + e.get()
    # Creating Label Widget
    myLabel = Label(root, text=hello,fg="white",bg="grey")
    # Placing Widget on screen
    myLabel.pack()


# Creating Buttons
myButton1 = Button(root, text="Enter your name",padx=50, pady=50,fg="white",bg="grey",command=myClick)

# Placing Buttons on screen
myButton1.pack()

#///////////////////////////////////////////////


root.mainloop()
