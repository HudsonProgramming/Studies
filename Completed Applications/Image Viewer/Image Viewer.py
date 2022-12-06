#///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

# Importing libraries
from tkinter import *
from PIL import ImageTk,Image

# Creating the window
root = Tk()
root.title("Image Viewer")
icon_img = ImageTk.PhotoImage(file='images\Icon.png')
root.tk.call('wm', 'iconphoto', root._w, icon_img)

#///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

# Storing the images
my_img_0 = ImageTk.PhotoImage(Image.open("images\Img_0.png"))
my_img_1 = ImageTk.PhotoImage(Image.open("images\Img_1.png"))
my_img_2 = ImageTk.PhotoImage(Image.open("images\Img_2.png"))
my_img_3 = ImageTk.PhotoImage(Image.open("images\Img_3.png"))
my_img_4 = ImageTk.PhotoImage(Image.open("images\Img_4.png"))

# Image list
img_list = [my_img_0, my_img_1, my_img_2 ,my_img_3, my_img_4]
img_list[0]

# Shows current moment in list
status = Label(root,text="Image 1 of  " + str(len(img_list)),bd=1,relief=SUNKEN, anchor=E)

my_Label = Label(image=my_img_0)
my_Label.grid(row=0,column=0,columnspan=3)

#///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

# Forward function ( -> )
def forward(img_num):
    
    global my_Label
    global btn_forward
    global btn_backward
    
    # Making use of forget to forget the last value.
    my_Label.grid_forget()  
    my_Label = Label(image=img_list[img_num-1])   
    btn_forward = Button(root,text=">>>",pady=5, command=lambda: forward(img_num + 1))
    btn_backward = Button(root,text="<<<",pady=5, command=lambda: backward(img_num - 1))

    if img_num == 5:
        btn_forward = Button(root,text=">>>",pady=5,state=DISABLED)
    
    my_Label.grid(row=0,column=0,columnspan=3, sticky=W+E)
    btn_backward.grid(row=1,column=0, sticky=W+E)    
    btn_forward.grid(row=1,column=2, sticky=W+E)

    status = Label(root,text="Image " +  str(img_num) +" of " + str(len(img_list)),bd=1,relief=SUNKEN, anchor=E)
    status.grid(row=2,column=0,columnspan=3, sticky=W+E)
    
#///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

# Backward function ( -> )
def backward(img_num):
    global my_Label
    global btn_forward
    global btn_backward

    # Making use of forget to forget the last value.
    my_Label.grid_forget()
    my_Label = Label(image=img_list[img_num-1])   
    btn_forward = Button(root,text=">>>",pady=5, command=lambda: forward(img_num +1))
    btn_backward = Button(root,text="<<<", pady=5,command=lambda: backward(img_num - 1))

    if img_num == 1:
        btn_backward = Button(root,text="<<<",pady=5,state=DISABLED)

    my_Label.grid(row=0,column=0,columnspan=3, sticky=W+E)
    btn_backward.grid(row=1,column=0, sticky=W+E)    
    btn_forward.grid(row=1,column=2, sticky=W+E)

    status = Label(root,text="Image " +  str(img_num) +" of " + str(len(img_list)),bd=1,relief=SUNKEN, anchor=E)
    status.grid(row=2,column=0,columnspan=3, sticky=W+E)
    
#///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

btn_forward= Button(root, text=">>>",pady=5,command=lambda: forward(2))
btn_backward = Button(root, text="<<<" ,pady=5,command=backward, state=DISABLED)
btn_exit = Button(root, text="Exit.",pady=5,command=root.destroy)

btn_exit.grid(row=1,column=1,pady=5, sticky=W+E)
btn_backward.grid(row=1,column=0, sticky=W+E)
btn_forward.grid(row=1,column=2, sticky=W+E)
status.grid(row=2,column=0,columnspan=3, sticky=W+E)

#///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

root.mainloop()

#///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

# Developed By Layton Hudson
