from tkinter import *
from tkinter import messagebox
#ham
def authen():
	value1 = username_box.Get()
	value2 = pwd_box.Get()
	if (value1 == 'administrator'):
		if (value2 == 'Cetera@2019'):
			messagebox.showinfo('Notification','Success')
		else:
			messagebox.showerror('Notification','Failed')
	else:
		messagebox.showerror('Notification','Failed')




#tao form
chaukha = Tk()

#title
chaukha.title('LCK Application')

#Login to your account
labels = Label(chaukha,text='Log in to you account',font=('Calibri',22)).pack()
#tao username
users = Label(chaukha,text='e-mail:',font=('Calibri',18)).pack()
#entry username
username_box = Entry(chaukha,width=30,font=('Calibri')).pack()


#password
pwd = Label(chaukha,text='Password:',font=('Calibri',18)).pack()
#entry password
pwd_box = Entry(chaukha,width=30,font=('Calibri'),show=('*')).pack()

#Login button
loginbutton = Button(chaukha,text='Login',font=('Calibri',20),command=authen).pack()
#end
chaukha.mainloop()