from tkinter import *
from PIL import Image, ImageTk

def register_():
    win_r = Tk()
    win_r.geometry("925x500")
    win_r.title("REGISTER")
    win_r.configure(bg='#06002e')

    load = Image.open(r"images\button_register.png")  # Open the image file
    reg_btn_image = ImageTk.PhotoImage(load)  # Convert the image for Tkinter

    bg_image = Label(win_r, image=reg_btn_image, bg='#06002e')
    bg_image.image = reg_btn_image  # Keep a reference to prevent garbage collection
    bg_image.place(x=0, y=0)

    Label(win_r, text="REGISTER", font=('Microsoft YaHei UI Light', 23, 'bold'), fg="white", bg="#261b79").pack(padx=10, pady=10)

    user_entry = Entry(win_r, width=25, fg='black', border=1, bg='white', font=('Microsoft YaHei UI Light', 19, 'bold'))
    user_entry.pack(padx=20, pady=20)
    Label(win_r, text="username", border=0, font=('Microsoft YaHei UI Light', 20, 'bold'), fg='white', bg='#7475f4').place(x=100, y=80)

    Button(win_r, image=reg_btn_image, borderwidth=0, bg='#251673').pack(padx=20, pady=20)  # register button in sec window

    win_r.mainloop()

register_()
