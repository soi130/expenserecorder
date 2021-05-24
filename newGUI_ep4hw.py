from tkinter import *
from tkinter import ttk
import csv
from datetime import datetime

GUI = Tk()
GUI.title('Expense Report Hw ep4')
GUI.geometry('500x500+1800+500')

#F1 = Frame(GUI)

#----tab
Tab = ttk.Notebook(GUI)
T1 = Frame(Tab)
T2 = Frame(Tab)
Tab.pack(fill=BOTH,expand=1)
#----tab creation
icon1 = PhotoImage(file='i1.png')
icon2 = PhotoImage(file='i2.png')
Tab.add(T1,text='Add Expense',image=icon1,compound='left')
Tab.add(T2,text='Expense List',image=icon2,compound='left')

#----days dictionary for later use
days = {'Mon':'จันทร์',
        'Tue':'อังคาร',
        'Wed':'พุธ',
        'Thu':'พฤหัส',
        'Fri':'ศุกร์',
        'Sat':'เสาร์',
        'Sun':'อาทิตย์'}

#----Define Save function
def Save(event=None): #event = None for keybinding
	expense = v_expense.get()
	price = v_price.get()
	quantity = v_quantity.get()
	value = float(price)*int(quantity)
	today = datetime.now().strftime('%a') # %a = return Weekday as locale’s abbreviated name (Mon...Tue....	
	dt = datetime.now().strftime('%y-%m-%d-{} %H:%M:%S'.format(days[today]))
	print('purchase: {} price: {} quantity: {} value: {} day: {}'.format(expense,price,quantity,value,dt))
	v_expense.set('')
	v_price.set('')
	v_quantity.set('')


	with open('savedata.csv','a',encoding = 'utf-8',newline='') as f:
    	# with = สั่งเปิดไฟล์แล้วปิดอัตโนมัติ
    	# 'a' = append at the end of the csv
    	# newline='' คือทำให้ไม่ต้องมีบรรทัดว่างระหว่างแต่ละรายการ
		fw = csv.writer(f) #สร้างฟังชั่นสำหรับเขียนข้อมูล
		line = [expense,price,quantity,value,dt]
		fw.writerow(line)
	# return curser to the beginning (E1)
	E1.focus()
#bind <Return> to Save()
GUI.bind('<Return>',Save)

#----set font
FONT1 = (None,20)

#----other widget
#----center image
center_image=PhotoImage(file='i3.png')
header_picture =  ttk.Label(T1,image=center_image)
header_picture.pack()
#----text1
L = Label(T1,text='purchase',font=FONT1).pack()
v_expense = StringVar()
E1 = ttk.Entry(T1,textvariable=v_expense,font=FONT1)
E1.pack()
#----text2
L = Label(T1,text='price',font=FONT1).pack()
v_price = StringVar()
E2 = ttk.Entry(T1,textvariable=v_price,font=FONT1)
E2.pack()
#----text3
L = Label(T1,text='quantity',font=FONT1).pack()
v_quantity = StringVar()
E3 = ttk.Entry(T1,textvariable=v_quantity,font=FONT1)
E3.pack()
#----button
icon4 = PhotoImage(file='i4.png')
B2 = ttk.Button(T1,text='Save',image=icon4,command=Save,compound='left')
B2.pack(ipady=20,pady=20)

GUI.mainloop()