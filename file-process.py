import tkinter
import os
from tkinter import filedialog
from tkinter import *


window = tkinter.Tk()
 
window.title("Welcome to File_rename app")
window.geometry('350x200')
lbl = Label(window, text="Select_Folder")
lbl1=Label(window)
lbl.grid(column=1,row=0)
lbl1.grid(column=3,row=0)
#root=tkinter.Tk()
def clicked():
   filename=filedialog.askdirectory(parent=window,title='Choose a file')
   print (filename)
   os.chdir(filename)
   for f in os.listdir():
       f_name,f_ext = os.path.splitext(f)
       ff_name = f_name[:11]
       ff_exe = '.jpg'
       final_name = ff_name + ff_exe
       os.rename(f,final_name)
       print(final_name)


btn = Button(window, text="Click Me",bg="orange",fg="BLUE",command=clicked)

btn.grid(column=2,row=0)

window.mainloop()


