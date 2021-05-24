from tkinter import *
from tkinter import ttk, messagebox
import csv
from datetime import datetime

GUI = Tk()
GUI.title('Expense Report Hw ep4')
GUI.geometry('800x700+1800+500')

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
	if expense == '':
		messagebox.showerror('Error','Please enter the item purchased') # show error popup
		return #end of the Save function here
	elif price == '':
		messagebox.showerror('Error','Please fill the price') # show error popup
		return
	elif quantity == '':
		messagebox.showerror('Error','Please fill the quantity') # show error popup
		return

	try:
		value = float(price)*int(quantity)
		today = datetime.now().strftime('%a') # %a = return Weekday as locale’s abbreviated name (Mon...Tue....	
		dt = datetime.now().strftime('%y-%m-%d-{} %H:%M:%S'.format(days[today]))
		print('purchase: {} price: {} quantity: {} value: {} day: {}'.format(expense,price,quantity,value,dt))
		text = 'purchase: {} price: {} quantity: {}\n value: {}\n day: {}'.format(expense,price,quantity,value,dt)
		v_result.set(text)
		v_expense.set('') #clear old data
		v_price.set('') #clear old data
		v_quantity.set('') #clear old data
		# tab2 Lable Creation
		record_text = '{} --- {} --- {} --- {} --- {}'.format(dt,expense,price,quantity,value)
		v_record.set(record_text)


		with open('savedata.csv','a',encoding = 'utf-8',newline='') as f:
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
		messagebox.showerror('Error','Fill only number in the space') # show error popup
		v_expense.set('') # clear textbox after error
		v_price.set('') # clear textbox after error
		v_quantity.set('') # clear textbox after error

#bind <Return> to Save()
GUI.bind('<Return>',Save)

#----set font
FONT1 = (None,20)

#----other widget--on tab1
#----center image--on tab1
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

v_result = StringVar()
v_result.set('----RESULT----')
result = Label(T1,textvariable=v_result,font=FONT1,fg='lime')
result.pack(pady=20)

#----Tab 2 element (LV-1)
v_record = StringVar()
v_record.set('----Record----')
record = Label(T2, textvariable=v_record,font=FONT1,fg='lime')
record.pack(pady=20)





GUI.mainloop()

'''
การบ้าน EP.5 ง่ายๆ 555
ให้เลือกทำ 2 LEVEL ใครอยากทำแบบง่ายก็เลือก Level 1 ใครอยากทำแบบยากก็ Level 2
LEVEL 1
ในแท็บที่ 2 (ค่าใช้จ่ายทั้งหมด)
ให้โชว์ผลลัพท์จากไฟล์ CSV ตามนี้ ทุกครั้งที่มีการอัพเดตจะมีการบันทึก record ใหม่ให้
LEVEL 2
ทำตารางโชว์ผลลัพท์แบบภาพด้านล่าง ในภาษา tkinter เขาเรียกว่า Treeview โดยให้โชว์ข้อมูลทุกครั้งที่มีการอัพเดต 
-----------------
ลายแทง1: https://github.com/UncleEng.../YiPun/blob/master/YiPun.py... 
ลายแทง2:
ใบ้ keyword ให้ค้นหาในยูทูปว่า: tkinter treeview
'''





























