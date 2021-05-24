#guibasic2-expense.py

from tkinter import *
from tkinter import ttk
import csv
from datetime import datetime

GUI = Tk()
GUI.title('Expanse Recorder by nak')
GUI.geometry('500x500+1800+500')

F1 = Frame(GUI)
F1.place(x=120,y=50)

days = {'Mon':'จันทร์',
        'Tue':'อังคาร',
        'Wed':'พุธ',
        'Thu':'พฤหัส',
        'Fri':'ศุกร์',
        'Sat':'เสาร์',
        'Sun':'อาทิตย์'}

def Save(event=None): #event=None สำหรับเหตุการณ์กด Enter ที่ Bind ไว้ด้านล่าง
    expense = v_expense.get() #get data form v_expense >> from StraingVar()
    price = v_price.get()
    quantity = v_quantity.get()
    try:
        value = float(price)*int(quantity)
        #dt=datetime.now()
        today = datetime.now().strftime('%a') # days['Mon'] = 'จันทร์'
        dt = datetime.now().strftime('%y-%m-%d-{} %H:%M:%S'.format(days[today]))
        print('entry: {} price: {} quantity:{} value:{} time:{}'.format(expense,price,quantity,value,dt))
        v_expense.set('') #reset the variable
        v_price.set('')
        v_quantity.set('')
        #----- save to csv----
        today = datetime.now().strftime('%a') # days['Mon'] = 'จันทร์'
        dt = datetime.now().strftime('%y-%m-%d-{} %H:%M:%S'.format(days[today]))
        with open('savedata.csv','a',encoding ='utf-8',newline='') as f:
        # with = สั่งเปิดไฟล์แล้วปิดอัตโนมัติ
        # 'a' = append at the end of the csv
        # newline='' คือทำให้ไม่ต้องมีบรรทัดว่างระหว่างแต่ละรายการ
            fw = csv.writer(f) #สร้างฟังชั่นสำหรับเขียนข้อมูล
            line = [expense,price,quantity,value,dt]
            fw.writerow(line)
        # return curser to the beginning (E1)
        E1.focus()
    except:
        print('ERROR')
#bind <enter>
GUI.bind('<Return>',Save)
   
FONT1 = (None,20)

#---text1---
L = Label(F1,text='entry',font=FONT1).pack()    
v_expense = StringVar() #special var for text storage
E1 = ttk.Entry(F1,textvariable=v_expense,font=FONT1)
E1.pack() #pack in center of the area (F1=Frame(GUI))
#-----------

#---text2---
L = Label(F1,text='price',font=FONT1).pack()    
v_price = StringVar() #special var for text storage
E2 = ttk.Entry(F1,textvariable=v_price,font=FONT1)
E2.pack() #pack in center of the area (F1=Frame(GUI))
#-----------

#---text3---
L = Label(F1,text='quantity',font=FONT1).pack()    
v_quantity = StringVar() #special var for text storage
E3 = ttk.Entry(F1,textvariable=v_quantity,font=FONT1)
E3.pack() #pack in center of the area (F1=Frame(GUI))
#-----------

B2 = ttk.Button(F1,text='Save',command=Save)
B2.pack(ipadx=50,ipady=20)


GUI.mainloop() 
