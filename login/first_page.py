from tkinter import *
from PIL import ImageTk,Image
import sys
sys.path.append(r'register')
import reg  
win = Tk()
win.geometry("925x500")
win.title("LOGIN")
win.configure(bg='#06002e')

#------backgroung img-----

load = Image.open("images\images (2) (1).png")
image_path = ImageTk.PhotoImage(load)
bg_image = Label(win, image=image_path, bg='#06002e')
bg_image.image = bg_image
bg_image.place(x=0, y=0)

#---login img----

login_btn=PhotoImage(file=r"images\button_login.png")

login_label=Label(image=login_btn)

#---reg img----

reg_btn=PhotoImage(file=r"images\button_register.png")

reg_label=Label(image=reg_btn)


Label(win, text="WELCOME TO SAP CALCULATOR ", font=('Microsoft YaHei UI Light', 23, 'bold'), fg='white', bg='#06002e').pack()

Label(win, text="LOGIN ", font=('Microsoft YaHei UI Light', 20, 'bold'), fg='white', bg='#06002e').pack(pady=20)
##-------email--------
def on_enter(e):
    email_login.delete(0,'end')

def on_leave(e):
    mid=email_login.get()
    if mid == '':
        email_login.insert(0,'Ex: ABC@gmail.com')

email_login = Entry(win, width=25, fg='black', border=1, bg='white', font=('Microsoft YaHei UI Light', 19))
email_login.place(x=325, y=150)
email_login.insert(0,"Ex: ABC@gmail.com")
email_login.bind('<FocusIn>',on_enter)
email_login.bind('<FocusOut>',on_leave)
Label(win, text="Mail-id", font=('Microsoft YaHei UI Light', 20, 'bold'), fg='white', bg='#06002e').place(x=150, y=140)

##------password--------

def on_enter(e):
    password.delete(0,'end')

def on_leave(e):
    p=password.get()
    if p == '':
        password.insert(0,'Ex: ABC@2024')



password = Entry(win, width=25, fg='black', border=1, bg='white', font=('Microsoft YaHei UI Light', 19))
password.place(x=325, y=200)
password.insert(0,"Ex: AC@2024")
password.bind('<FocusIn>',on_enter)
password.bind('<FocusOut>',on_leave)
Label(win, text="password", font=('Microsoft YaHei UI Light', 23, 'bold'), fg='white', bg='#06002e').place(x=150, y=190)

##---login btn-----
Button(win,image=login_btn,borderwidth=0,bg='#06002e').place(x=360, y=270)  # login button

##--reg btn-------

Button(win, image=reg_btn,borderwidth=0,bg='#06002e',command=reg.register_).place(x=360, y=340)  # register button
Label(win, text="If u don't have account already!!", font=('Microsoft YaHei UI Light', 10, 'bold'), fg='white', bg='#06002e').place(x=350, y=410)

win.mainloop()