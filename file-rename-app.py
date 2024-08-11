from tkinter import *
import tkinter
import os
from tkinter import filedialog
from tkinter.ttk import *
window = Tk()
 
window.title("Welcome to File_rename App")
 
window.geometry('600x400')

lbl=Label(window,text="Select folder/directory")

lbl.grid(column=0,row=0)

lbl1=Label(window,text="Will you want to rename 11 digit or 12 digit")
lbl2=Label(window)
lbl3=Label(window,text="Please Choose extention")

lbl1.grid(column=0,row=1)
lbl2.grid(column=2,row=0)
lbl3.grid(column=0,row=4)



def clicked():
   global filename
   filename=filedialog.askdirectory(parent=window,title='Choose a file')
   lbl2.configure(text=filename)

btn=Button(window, text="Upload Folder", command=clicked)

btn.grid(column=1, row=0)


cb_strings = ['11', '12']
cb_strings1 = ['.jpg', '.jpeg', '.png']
def sel():
   global x
   x=str(var.get())  
def sel1():
   global y
   y=str(var1.get())

var = StringVar()
#var.set(cb_strings[0])
var1 = StringVar()
#var1.set(cb_strings1[0])
r=1
for item in cb_strings:
    button = Radiobutton(window, text=item, variable=var, value=item, command=sel).grid(row=1,column=r)
    r=r+1
j=1  
for item in cb_strings1:
    button1 = Radiobutton(window, text=item, variable=var1, value=item, command=sel1).grid(row=4,column=j)
    j=j+1
    

def clicked6():
    os.chdir(filename)
    p=0
    l=StringVar()
    for f in os.listdir():
        f_name,f_ext = os.path.splitext(f)
        ff_name = f_name[:int(x)]
        ff_exe=y
        final_name = ff_name + ff_exe
        if l!=final_name:
           #print(f)
           os.rename(f,final_name)
           p=p+1
        else:
           os.remove(f)
        l=final_name
        
        #q=[]
        
        #q.append(final_name)

    lbl4=Label(window)
    lbl4.grid(column=0,row=7)
    lbl4.configure(text="Done.Successfully "+str(p)+" Files Rename")
        
        
        

btn1=Button(window, text="Submit",command=clicked6)

btn1.grid(column=0,row=6)




 

 
window.mainloop()
