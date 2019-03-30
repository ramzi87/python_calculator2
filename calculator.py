
from tkinter import *

root = Tk()
root.geometry("350x330+250+200")
root.configure(background="#ACFA58")
root.title("Calculator")
root.resizable(width=False,height=False)

icon = PhotoImage(file='my_photo.png')
root.call('wm','iconphoto',root._w,icon)


operator = ""
text_Input = StringVar()

def button_click(numbers):
	global operator
	operator += str(numbers)
	text_Input.set(operator)

def btn_Clear():
	global operator
	operator = ""
	text_Input.set("")

def btn_Equals():
	global operator
	result=str(eval(operator))
	text_Input.set(result)
	operator = result


txt_display = Entry(root,width=28,font=('Times',16,'bold'),textvariable=text_Input,bg="#A9D0F5",bd=6,justify="right")
txt_display.place(x=15,y=10)

btn7=Button(root,padx=10,width=4,height=2,font=('Times',12,'bold'),text="7",bd=4,bg="#CEECF5",fg="black",command=lambda:button_click(7))
btn7.place(x=15,y=60)

btn8=Button(root,padx=10,width=4,height=2,font=('Times',12,'bold'),text="8",bd=4,bg="#CEECF5",fg="black",command=lambda:button_click(8))
btn8.place(x=95,y=60)

btn9=Button(root,padx=10,width=4,height=2,font=('Times',12,'bold'),text="9",bd=4,bg="#CEECF5",fg="black",command=lambda:button_click(9))
btn9.place(x=175,y=60)

btn_add=Button(root,padx=10,width=4,height=2,font=('Times',12,'bold'),text="+",bd=4,bg="#CEECF5",fg="black",command=lambda:button_click('+'))
btn_add.place(x=260,y=60)

btn4=Button(root,padx=10,width=4,height=2,font=('Times',12,'bold'),text="4",bd=4,bg="#CEECF5",fg="black",command=lambda:button_click(4))
btn4.place(x=15,y=120)

btn5=Button(root,padx=10,width=4,height=2,font=('Times',12,'bold'),text="5",bd=4,bg="#CEECF5",fg="black",command=lambda:button_click(5))
btn5.place(x=95,y=120)

btn6=Button(root,padx=10,width=4,height=2,font=('Times',12,'bold'),text="6",bd=4,bg="#CEECF5",fg="black",command=lambda:button_click(6))
btn6.place(x=175,y=120)

btn_subtract=Button(root,padx=10,width=4,height=2,font=('Times',12,'bold'),text="-",bd=4,bg="#CEECF5",fg="black",command=lambda:button_click('-'))
btn_subtract.place(x=260,y=120)

btn1=Button(root,padx=10,width=4,height=2,font=('Times',12,'bold'),text="1",bd=4,bg="#CEECF5",fg="black",command=lambda:button_click(1))
btn1.place(x=15,y=180)

btn2=Button(root,padx=10,width=4,height=2,font=('Times',12,'bold'),text="2",bd=4,bg="#CEECF5",fg="black",command=lambda:button_click(2))
btn2.place(x=95,y=180)

btn3=Button(root,padx=10,width=4,height=2,font=('Times',12,'bold'),text="3",bd=4,bg="#CEECF5",fg="black",command=lambda:button_click(3))
btn3.place(x=175,y=180)

btn_multiply=Button(root,padx=10,width=4,height=2,font=('Times',12,'bold'),text="*",bd=4,bg="#CEECF5",fg="black",command=lambda:button_click('*'))
btn_multiply.place(x=260,y=180)

btn0=Button(root,padx=10,width=4,height=2,font=('Times',12,'bold'),text="0",bd=4,bg="#CEECF5",fg="black",command=lambda:button_click(0))
btn0.place(x=15,y=240)

btn_clear=Button(root,padx=10,width=4,height=2,font=('Times',12,'bold'),text="C",bd=4,bg="#CEECF5",fg="black",command=btn_Clear)
btn_clear.place(x=95,y=240)

btn_equal=Button(root,padx=10,width=4,height=2,font=('Times',12,'bold'),text="=",bd=4,bg="#CEECF5",fg="black",command=btn_Equals)
btn_equal.place(x=175,y=240)

btn_division=Button(root,padx=10,width=4,height=2,font=('Times',12,'bold'),text="/",bd=4,bg="#CEECF5",fg="black",command=lambda:button_click('/'))
btn_division.place(x=260,y=240)





root.mainloop()