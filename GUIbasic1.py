#guibasic1.py

from tkinter import *
from tkinter import ttk #import theme

GUI = Tk()
#let GUI = Tk() class
GUI.geometry('500x300+1800+500')
#+x+y ด้านหลังคือสั้่่งให้เรนเดอร์จากขอบจอมาเท่าไร

#B1 = Button(GUI,text='Hello')
#create button characteristic
#B1.pack(ipadx=20,ipady=50)
#pack this variable into the center of the area (in this case GUI = Tk())
#ipadx = internal x padding 

F1 = Frame(GUI)
# create a Frame within GUI
F1.place(x=20,y=50)

def Hello():
    print('Hello you')

B2 = ttk.Button(F1,text='Hello',command=Hello)
#create button characteristic
B2.pack(ipadx=50,ipady=20)
#pack this variable into the specific area



GUI.mainloop() #บรรทัดสุดท้าย เพื่อสั่งให้รันตลอดเวลา
