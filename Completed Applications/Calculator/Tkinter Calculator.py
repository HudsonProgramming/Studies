# Importing all from the tkinter library
from tkinter import *

# Creating the window.
root = Tk()
root.title("Tkinter Calculator")

# Creating an entry box.
e = Entry(root,width=35,borderwidth=5)
# Placing the entry box at 0,0 spaning over 3 columns.
e.grid(row=0,column=0,columnspan=3,padx=10,pady=10)

# Creating function button_click to enable the buttons 0-9 to work and display numbers in the entry box e.
def button_click(number):
    # Creating a variable called current that is getting the contents of the entry box "e".
    current = e.get()
    # Deletes contents that is already in the box, 0 refers to itself (the box), so 0 is the box that will be cleared.
    e.delete(0,END)
    # Inserts number into the box, 0 refers to itself (the box), so 0 is the box that number will go into.
    e.insert(0,str(current)+str(number))

# Creating function button_clear to clear anything in the entry box e.
def button_clear():
    e.delete(0,END)

# Creating function button_add to add values together
def button_add():
    # Creating variable first_number that will get the contents of entry box e.
    first_number = e.get()
    # Creating a global variable f_num that can be used inside any other funtion.
    global f_num
    global math
    # Variable maths is equal to "addition"
    math = "addition"
    # f_num variable is equal to first_number which is the value of the entry box e but it puts the value into a integer data type.
    f_num = int(first_number)
    e.delete(0,END)  

# Creating function button_sub to subtract values from eachother.
def button_sub():
    # Creating variable first_number that will get the contents of entry box e.
    first_number = e.get()
    # Creating a global variable f_num that can be used inside any other funtion.
    global f_num
    global math
    # Variable maths is equal to "subtraction"
    math = "subtraction"
    # f_num variable is equal to first_number which is the value of the entry box e but it puts the value into a integer data type.
    f_num = int(first_number)
    e.delete(0,END)
    
# Creating function button_mul to multiply values together.
def button_mul():
    # Creating variable first_number that will get the contents of entry box e.
    first_number = e.get()
    # Creating a global variable f_num that can be used inside any other funtion.
    global f_num
    # Creating a global variable math that can be used inside any other funtion.
    global math
    # Variable maths is equal to "multiplication"
    math = "multiplication"
    # f_num variable is equal to first_number which is the value of the entry box e but it puts the value into a integer data type.
    f_num = int(first_number)
    e.delete(0,END) 

# Creating function button_div to divide to values from eachother.
def button_div():
    # Creating variable first_number that will get the contents of entry box e.
    first_number = e.get()
    # Creating a global variable f_num that can be used inside any other funtion.
    global f_num
    # Creating a global variable math that can be used inside any other funtion.
    global math
    # Variable maths is equal to "division"
    math = "division"
    # f_num variable is equal to first_number which is the value of the entry box e but it puts the value into a integer data type.
    f_num = int(first_number)
    e.delete(0,END) 

# Creating function button_equal to show the sum of values when added toegther
def button_equal():
    # Creating variable second_number that will get the contents of entry box e.
    second_number = e.get()
    e.delete(0, END)
    # if variable maths = "addition" then inside the entry box ( 0 ), add together f_num and int(second_number) and insert that total in the box.
    if math == "addition":
        e.insert(0, f_num + int(second_number))
    # if variable maths = "subtraction" then inside the entry box ( 0 ), subtract f_num from int(second_number) and insert that total in the box.
    if math == "subtraction":
        e.insert(0, f_num - int(second_number))
    # if variable maths = "multiplication" then inside the entry box ( 0 ), multiply together f_num and int(second_number) and insert that total in the box.
    if math == "multiplication":
        e.insert(0, f_num * int(second_number))
    # if variable maths = "division" then inside the entry box ( 0 ), divide f_num from int(second_number) and insert that total in the box.
    if math == "division":
        e.insert(0, f_num / int(second_number))

# Creating buttons 0-9. Lambda will allow you to pass a value through the parameter, so in button_click 'number' == button_click(Value here)
btn_1 = Button(root,text="1",padx=40,pady=20,command=lambda:button_click(1))
btn_2 = Button(root,text="2",padx=40,pady=20,command=lambda:button_click(2))
btn_3 = Button(root,text="3",padx=40,pady=20,command=lambda:button_click(3))
btn_4 = Button(root,text="4",padx=40,pady=20,command=lambda:button_click(4))
btn_5 = Button(root,text="5",padx=40,pady=20,command=lambda:button_click(5))
btn_6 = Button(root,text="6",padx=40,pady=20,command=lambda:button_click(6))
btn_7 = Button(root,text="7",padx=40,pady=20,command=lambda:button_click(7))
btn_8 = Button(root,text="8",padx=40,pady=20,command=lambda:button_click(8))
btn_9 = Button(root,text="9",padx=40,pady=20,command=lambda:button_click(9))
btn_0 = Button(root,text="0",padx=40,pady=20,command=lambda:button_click(0))

# Creating buttons for adding,subtracting,mulitpling,dividing, clearing and finding the sum of values.
btn_add = Button(root,text="+",padx=39,pady=20,command=button_add)
btn_sub = Button(root,text="-",padx=40,pady=20,command=button_sub)
btn_mul = Button(root,text="X",padx=40,pady=20,command=button_mul)
btn_div = Button(root,text="/",padx=41,pady=20,command=button_div)
btn_clr = Button(root,text="Clear",padx=79,pady=20,command=button_clear)
btn_equal = Button(root,text="=",padx=91,pady=20,command=button_equal)

# Placing row 3 buttons on screen.
btn_1.grid(row=3,column=0)
btn_2.grid(row=3,column=1)
btn_3.grid(row=3,column=2)
# Placing row 2 buttons on screen.
btn_4.grid(row=2,column=0)
btn_5.grid(row=2,column=1)
btn_6.grid(row=2,column=2)
# Placing row 1 buttons on screen.
btn_7.grid(row=1,column=0)
btn_8.grid(row=1,column=1)
btn_9.grid(row=1,column=2)
# Placing row 4 buttons on screen.
btn_0.grid(row=4,column=0)
btn_clr.grid(row=4,column=1,columnspan=2)
# Placing row 5 buttons on screen.
btn_add.grid(row=5,column=0)
btn_equal.grid(row=5,column=1,columnspan=2)
# Placing row 6 buttons on screen.
btn_sub.grid(row=6,column=0)
btn_mul.grid(row=6,column=1)
btn_div.grid(row=6,column=2)

# Window loop keeps window constantly open.
root.mainloop()


# Developed by Layton Hudson 12:50 Friday 21/10/2022
