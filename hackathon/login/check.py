from tkinter import *
from PIL import ImageTk, Image

win = Tk()
win.geometry("925x500")
win.title("LOGIN")
win.configure(bg='#06002e')

load = Image.open("login\images (2) (1).png")
image_path = ImageTk.PhotoImage(load)
bg_image = Label(win, image=image_path, bg='#06002e')
bg_image.image = bg_image
bg_image.place(x=0, y=0)

Label(win, text="WELCOME TO SAP CALCULATOR ", font=('Microsoft YaHei UI Light', 23, 'bold'), fg='white', bg='#06002e').pack()

Label(win, text="LOGIN ", font=('Microsoft YaHei UI Light', 23, 'bold'), fg='white', bg='#06002e').pack(pady=20)

email_login = Entry(win, width=25, fg='white', border=1, bg='white', font=('Microsoft YaHei UI Light', 19, 'bold'))
email_login.place(x=325, y=150)
Label(win, text="Mail-id", font=('Microsoft YaHei UI Light', 23, 'bold'), fg='white', bg='#06002e').place(x=150, y=140)
password = Entry(win, width=25, fg='white', border=1, bg='white', font=('Microsoft YaHei UI Light', 19, 'bold'), show='*')
password.place(x=325, y=200)
Label(win, text="password", font=('Microsoft YaHei UI Light', 23, 'bold'), fg='white', bg='#06002e').place(x=150, y=190)

# Round Button Function
def round_button(widget):
    widget.config(relief="flat", highlightthickness=0, borderwidth=0)
    widget.bind("<Enter>", lambda e: widget.config(bg="#6fa8dc"))
    widget.bind("<Leave>", lambda e: widget.config(bg="#57a1f8"))

# Login Button
login_button = Button(win, text='login', width=20, pady=7, bg='#57a1f8', fg='black', font=('Microsoft YaHei UI Light', 16, 'bold'))
login_button.place(x=340, y=250)
round_button(login_button)

# Register Button
register_button = Button(win, text='REGISTER', width=20, pady=7, bg='#57a1f8', fg='black', font=('Microsoft YaHei UI Light', 16, 'bold'))
register_button.place(x=340, y=320)
round_button(register_button)

Label(win, text="If u don't have account already!!", font=('Microsoft YaHei UI Light', 10, 'bold'), fg='white', bg='#06002e').place(x=360, y=390)

win.mainloop()
