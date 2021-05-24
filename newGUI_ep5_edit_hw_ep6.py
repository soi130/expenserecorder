from tkinter import *
from tkinter import ttk, messagebox
import csv
from datetime import datetime

GUI = Tk()
GUI.title('Expense Report Hw ep4')
GUI.geometry('900x850+1500+500')

######menu######
menubar = Menu(GUI) #Menu มากจาก tkinter import*
GUI.config(menu=menubar)

#File menu
filemenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label='File',menu=filemenu)
filemenu.add_command(label='Impoort CSV')
filemenu.add_command(label='Export to Google Sheet')

def About():
	messagebox.showinfo('About', 'สวัสดีครับ นี่คือส่วน About')

helpmenu = Menu(menubar)
menubar.add_cascade(label='Help',menu=helpmenu)
helpmenu.add_command(label='About', command=About)

donatemenu = Menu(menubar)
menubar.add_cascade(label='Donate',menu=donatemenu)

################

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
	#record = v_record.get()
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
		#v_record.set(record_text)


		with open('savedata.csv','a',encoding = 'utf-8',newline='') as f:
	    	# with = สั่งเปิดไฟล์แล้วปิดอัตโนมัติ
	    	# 'a' = append at the end of the csv
	    	# newline='' คือทำให้ไม่ต้องมีบรรทัดว่างระหว่างแต่ละรายการ
			fw = csv.writer(f) #สร้างฟังชั่นสำหรับเขียนข้อมูล
			line = [dt,expense,price,quantity,value]
			fw.writerow(line)
		# return curser to the beginning (E1)
		E1.focus()
		# ส่วนของ การแสดงผลใน tab 2
		update_table() #สั่งให้ ใช้ฟังชั่น(update_table) หลังจาก save



	except Exception as e:
		print('ERROR',e)
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

#----Tab 2 element (LV.2)
def read_csv():
	with open('savedata.csv',newline='',encoding='utf-8') as f: #with ทำให้เราไม่ต้องสั่ง open และต้องมาตาม close จะได้ไม่ error file permission
		fr = csv.reader(f) #อ่านค่า f (csv ที่เปิดไว้) แล้วใส่เข้าไปในตัวแปร fr
		data =list(fr) # แปลงไฟล์ csv ให้เป็นลิสต์เพื่อให้คนอ่านออกง่ายๆ
	return data

#table
Title = ttk.Label(T2, text="Summary").pack(pady = 20)

header = ['date/time', 'entry','price','quantity','value'] #ตั้งชื่อคอลั่มเป็นลิส
resulttable = ttk.Treeview(T2,columns=header,show='headings',height=20) #สร้างตาราง
resulttable.pack()

#---first approach of crating header title > using for loop and range
for i in range(len(header)):
	resulttable.heading(header[i],text=header[i])
'''---secound approach using quick for loop
for h in header:
	resulttable.heading(h,text=h)
'''
#set the column width v
headerwidth = [200,170,80,80,80]
for h,w in zip(header,headerwidth): #zip  คือ เอาสอง list มาแปะรวมกัน กลายเป็น list of tuple
	resulttable.column(h,width=w)

def update_table():
	resulttable.delete(*resulttable.get_children())#สั่งให้ล้างตารางก่อนค่อยใส่รายการทั้งหมดที่มีลงไป จะได้ไม่ซ้ำ
	#resulttable.delete(*resulttable.get_children()) มีค่่าเท่ากับ
	# for c in resulttable.get_children():
	# 	resulttable.delete(c)
	data = read_csv()
	for d in data:
		resulttable.insert('',0,value=d)

update_table()

#GUI.bind('<Tab>',Lambda x: E2.focus()) 
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





























