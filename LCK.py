from tkinter import *
from tkinter import messagebox
from PIL import Image 
def authen():
	user = username_box.get()
	pwd = pwd_box.get()
	if (value1 == 'administrator'):
		if (value2 == 'Cetera@2019'):
			messagebox.showinfo('Notification','Success!')
		else:
			messagebox.showerror('Notification','Failed!')
	else:
		messagebox.showerror('Notification','Failed!')

#Tao form
main_page = Tk()
main_page.title('Application')
#Welcome
logon = Label(main_page,text='Log in your Account',font=('Comic Sans MS',25)).pack()
#tao username_field
username_field = Label(main_page, text='Username:',font=('Comic Sans MS',18)).pack()
#entry username_field
username_box = Entry(main_page,width=30,font=('Calibri')).pack()
#tao pwd_field
pwd_field = Label(main_page,text='Password:',font=('Comic Sans MS',18)).pack()
#entry pwd_field
pwd_box = Entry(main_page,width=30,font=('Calibri'),show="*").pack()
#Login Button
login_button = Button(main_page,text='Login',font=('Comic Sans MS',18),command=authen).pack()
main_page.mainloop()