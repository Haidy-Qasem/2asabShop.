from tkinter import*
# from PIL import ImageTk, Image
window=Tk()
window.title("WELCOME TO HUSSIN 2ASAB SHOP")

window.geometry('700x700')

button_0=Button(window,text="Quit",background="red",fg="white",command=window.destroy).place(x=500,y=600)


label_1=Label(window,text="SMALL SIZE",height=5,width=10).place(x=0,y=100)
label_2=Label(window,text="MEDIUM SIZE",height=5,width=10).place(x=0,y=300)
label_2=Label(window,text="LARGE SIZE",height=5,width=10).place(x=0,y=500)

photo_1 = PhotoImage(file = 'size1.png')	
photo_1=photo_1.subsample(13,12)
photo_2 = PhotoImage(file= 'size1.png')	
photo_2=photo_2.subsample(12,9)
photo_4 = PhotoImage(file= 'size1.png')	
photo_4=photo_4.subsample(10,8)
photo_5 = PhotoImage(file = 'bill.png')	
photo_5=photo_5.subsample(2,2) 
 

def Buttonpresstracker ():
	Buttonpresstracker.counter +=1
	print("",Buttonpresstracker.counter)
Buttonpresstracker.counter=0 # line below is important to identify counter
button_1=Button(window,image=photo_1,fg="black",command=Buttonpresstracker,height=200,width=190).place(x=200,y=0)


def Buttonpresstracker_1 ():
	Buttonpresstracker_1.counter +=1
	print("",Buttonpresstracker_1.counter)
Buttonpresstracker_1.counter=0
button_2=Button(window,image=photo_2,fg="black",command=Buttonpresstracker_1,height=200,width=190).place(x=200,y=210)

def Buttonpresstracker_2 ():
	Buttonpresstracker_2.counter +=1
	print("",Buttonpresstracker_2.counter)
Buttonpresstracker_2.counter=0 # line below is important to identify counter
button_3=Button(window,image=photo_4,fg="black",command=Buttonpresstracker_2,height=200,width=190).place(x=200,y=420)

def open_popup():
	top=Tk()
	top.geometry('300x300')
	top.title("BILL")
	# photo_6 = PhotoImage(file = 'bill.png')	
	# photo_6=photo_6.subsample(2,5)
	
	def button_bill():
		bill=(Buttonpresstracker.counter*20)+(Buttonpresstracker_1.counter*25)+(Buttonpresstracker_2.counter*30)
		label_3=Label(top,text=bill).place(x=100,y=60)
	button_5=Button(top,text="BILL",background="light green",fg="black",command=button_bill,height=5,width=10).place(x=5,y=45)
button_4=Button(window,image=photo_5,fg="black",command=open_popup,height=70,width=70).place(x=500,y=500)
window.mainloop()
