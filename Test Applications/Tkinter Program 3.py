from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title("Image Viewer")
iconimg = PhotoImage(file='Icon.png')
root.tk.call('wm', 'iconphoto', root._w, iconimg)


my_img = ImageTk.PhotoImage(Image.open("Icon.png"))
my_Label = Label(image=my_img)
my_Label.pack()

exit_btn = Button(root, text="Exit." ,command=root.destroy)
exit_btn.pack()

root.mainloop()
