#//////////////////////////////////////////////////////////////////////////////////////////////////#

import tkinter as tk
# This is importing the tkinter library and then using tk as an alias for later references.

root = tk.Tk()
# root is the name given to the window. tk.TK() constructs the window.

root.geometry("800x600")
# .geometry sets the size for the window.

root.title("My First GUI")
# .title prints text at top of the window displaying the application name.

#//////////////////////////////////////////////////////////////////////////////////////////////////#

label = tk.Label(root, text="Hello World!", font=('Arial',18))
# label is a variable which has information on the display of Hello world! in Arial at size 18.
# The parent is root as that is the window the label is going in.

label.pack(padx=20,pady=20)
# this displays the label, pad(x/y) is the padding around the label.

#//////////////////////////////////////////////////////////////////////////////////////////////////#

textbox = tk.Text(root, height=3 ,font=('Arial', 16))
textbox.pack(padx=10,pady=10)
# Exactly like the label except this is a text box. It goes right after the label and it's been given a height of 3

'''myentry = tk.Entry(root)
myentry.pack()
# Similar to the texbox however this is made for simple entries such as one word or a sentence.'''
#//////////////////////////////////////////////////////////////////////////////////////////////////#

button = tk.Button(root, text="Click Me!", font=('Arial', 18))
button.pack(padx=10,pady=10)

# Simple button

#//////////////////////////////////////////////////////////////////////////////////////////////////#

buttonframe = tk.Frame(root)
buttonframe.columnconfigure(0, weight=1) # Column 1
buttonframe.columnconfigure(1, weight=1) # Column 2
buttonframe.columnconfigure(2, weight=1) # Column 3

btn1 = tk.Button(buttonframe, text="1", font=('Arial', 18))
#btn1 is a button with the buttonframe as the parent as it will be inside the button frame.
btn1.grid(row=0, column=0, sticky=tk.W+tk.E)
#btn1 is located at row 0, column 0. It will stretch west and east ( sticky=tk.W+tk.E ) to fill in any empty space.

btn2 = tk.Button(buttonframe, text="2", font=('Arial', 18))
btn2.grid(row=0, column=1, sticky=tk.W+tk.E)

btn3 = tk.Button(buttonframe, text="3", font=('Arial', 18))
btn3.grid(row=0, column=2, sticky=tk.W+tk.E)

btn4 = tk.Button(buttonframe, text="4", font=('Arial', 18))
btn4.grid(row=1, column=0, sticky=tk.W+tk.E)

btn5 = tk.Button(buttonframe, text="5", font=('Arial', 18))
btn5.grid(row=1, column=1, sticky=tk.W+tk.E)

btn6 = tk.Button(buttonframe, text="6", font=('Arial', 18))
btn6.grid(row=1, column=2, sticky=tk.W+tk.E)

buttonframe.pack(fill='x')
# fill='x' will stretch it to make it fill all x dimensions.

'''anotherbtn = tk.Button(root, text="TEST")
anotherbtn.place(x=200, y=200, height=100, width=100)
# This is how you would go about manually placing buttons etc.'''

#//////////////////////////////////////////////////////////////////////////////////////////////////#

root.mainloop()
# This Tkinter event loop watches out for button clicks, keypresses and any code after it that is running until you close the window.

#//////////////////////////////////////////////////////////////////////////////////////////////////#

