from tkinter import *
import tkinter
import os
from tkinter import filedialog
from tkinter.ttk import *
window = Tk()
 
window.title("Welcome to File_rename App")
 
window.geometry('600x200')

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

btn=Button(window, text="Click Me", command=clicked)

btn.grid(column=1, row=0)

var = IntVar()
def clicked1():
     global x
     x=11
def clicked2():
     global x
     x=12
rad1= Radiobutton(window,text='11', value=1, command=clicked1)

 
rad2= Radiobutton(window,text='12', value=2, command=clicked2)



def clicked6():
    os.chdir(filename)
    for f in os.listdir():
        f_name,f_ext = os.path.splitext(f)
        ff_name = f_name[:x]
        if chk_state.get()==1:
            ff_exe = '.jpg'
        elif chk_state1.get()==1:
            ff_exe = '.jpeg'
        elif chk_state2.get()==1:
             ff_exe = '.png'
        final_name = ff_name + ff_exe
        os.rename(f,final_name)
        print(final_name)
    
chk_state = IntVar()
chk_state1 = BooleanVar()
chk_state2 = BooleanVar()

chk1 = Checkbutton(window, text='jpg', var=chk_state,onvalue = 1, offvalue = 0)
chk2 = Checkbutton(window, text='jpeg', var=chk_state1,onvalue = 1, offvalue = 0)
chk3 = Checkbutton(window, text='png', var=chk_state2,onvalue = 1, offvalue = 0)

chk1.grid(column=1, row=4)
chk2.grid(column=2, row=4)
chk3.grid(column=3, row=4)
btn1=Button(window, text="Submit",command=clicked6)

btn1.grid(column=0,row=6)

rad1.grid(column=1, row=1)
 
rad2.grid(column=2, row=1)


 

 
window.mainloop()

 

