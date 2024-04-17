from tkinter import *
from PIL import ImageTk,Image
def register_():
    win_r = Toplevel()
    win_r.geometry("925x500")
    win_r.title("REGISTER")
    win_r.configure(bg='#06002e')

    #load = Image.open(r"images\images (1).png")
    image_path = ImageTk.PhotoImage(file=r"images\images (1).png")

    reg_btn=PhotoImage(file=r"images\button_register.png")

    reg_label=Label(image=reg_btn)
    reg_label.image= reg_btn

    bg_image = Label(win_r, image=image_path, bg='#06002e')
    bg_image.image = bg_image
    bg_image.place(x=0, y=0)
    Label(win_r,text="REGISTER",font=('Microsoft YaHei UI Light',23,'bold'),fg="white",bg="#261b79").pack(padx=10,pady=10)

    user_entry=Entry(win_r,width=25,fg='black',border=1,bg='white',font=('Microsoft YaHei UI Light',19,'bold'))
    user_entry.pack(padx=20,pady=20)
    Label(win_r,text="username",border=0,font=('Microsoft YaHei UI Light',20,'bold'),fg='white',bg='#7475f4').place(x=100,y=80)
        
    password_entry=Entry(win_r,width=25,fg='black',border=1,bg='white',font=('Microsoft YaHei UI Light',19,'bold'),show='*')
    password_entry.pack(padx=20,pady=20)
    Label(win_r,text="password",font=('Microsoft YaHei UI Light',20,'bold'),fg='white',bg='#5e64e5').place(x=100,y=160)
    hotel_entry=Entry(win_r,width=25,fg='black',border=1,bg='white',font=('Microsoft YaHei UI Light',19,'bold'))
    hotel_entry.pack(padx=20,pady=20)
    Label(win_r,text="Email-ID",border=0,font=('Microsoft YaHei UI Light',20,'bold'),fg='white',bg='#39329a').place(x=100,y=235)
    ph_no_entry=Entry(win_r,width=25,fg='black',border=1,bg='white',font=('Microsoft YaHei UI Light',19,'bold'))
    ph_no_entry.pack(padx=20,pady=20)
    Label(win_r,text="ph_number",font=('Microsoft YaHei UI Light',20,'bold'),fg='white',bg='#291e7e').place(x=100,y=310)
        
    Button(win_r, image=reg_btn,borderwidth=0,bg='#251673').pack(padx=20,pady=20)#register button in sec win_r_rdow

    win_r.mainloop()
