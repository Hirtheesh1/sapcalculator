from tkinter import *
from PIL import ImageTk,Image
from first_page import login

root = Tk()
root.geometry("925x500")
root.title("WELCOME")
root.configure(bg='white')
Label(root,text="Welcome to SAP calculator",font=('Microsoft YaHei UI Light', 23, 'bold'),fg="black",bg="white").pack()

Label(root,text="Who are you?",font=('Microsoft YaHei UI Light', 23, 'bold'),fg="black",bg="white").pack(padx=10,pady=10)
load = Image.open("images\student5651 (1).jpg")
root.resizable(0,0)
image_path = ImageTk.PhotoImage(load)
bg_image = Button(root, image=image_path,border=0 ,bg='white',command=login)
bg_image.image = bg_image
bg_image.place(x=50, y=100)
Label(root,text="Student",font=('Microsoft YaHei UI Light',16, 'bold'),fg="black",bg="white").place(x=130,y=350)

load_t = Image.open(r"images\teacher_logo.jpg")
image_path_t = ImageTk.PhotoImage(load_t)
bg_image_t = Button(root, image=image_path_t,border=0 ,bg='white')
bg_image_t.image = bg_image_t
bg_image_t.place(x=350, y=100)

Label(root,text="Faculty",font=('Microsoft YaHei UI Light',16, 'bold'),fg="black",bg="white").place(x=430,y=350)

load_p = Image.open(r"images\principal_logo.jpg")
image_path_p = ImageTk.PhotoImage(load_p)
bg_image_p = Button(root, image=image_path_p,border=0 ,bg='white')
bg_image_p.image = bg_image_p
bg_image_p.place(x=650, y=100)

Label(root,text="The Principal",font=('Microsoft YaHei UI Light',16, 'bold'),fg="black",bg="white").place(x=700,y=350)

root.mainloop()
