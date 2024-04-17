from tkinter import *
from PIL import Image, ImageTk
# import tkinter as tk
from tkinter import messagebox
import mysql.connector

windows = Tk()
windows.geometry('500x640')
windows.resizable(False,False)
#windows.attributes('-transparentcolor', 'black')
windows.title('Simple Coding Style')






#show and hide password
def show():
    passwordEntry.configure(show='#')
    check1.configure(command=hide)

def hide():
    passwordEntry.configure(show='')
    check1.configure(command=show)



def show1():
        renterpasswordEntry.configure(show='#')
        check2.configure(command=hide1)

def hide1():
        renterpasswordEntry.configure(show='')
        check2.configure(command=show1)



def back():
    windows.destroy()
    import loginpg

#
# Field Validations
def submit():


    if firstnameEntry.get()=='' or lastnameEntry.get()=='' or emailentry.get()=='' or gender.get()=='' \
            or usernameEntry.get()=='' or passwordEntry.get()=='' or \
            renterpasswordEntry.get()=='':
            messagebox.showerror('Alert!', 'All Fields must be entered') #this is to check if all the entry fields are
            # empty if it is true it'll show a msgbox error

    elif passwordEntry.get() != renterpasswordEntry.get():
        messagebox.showerror('Alert!', 'Passwords didn\'t Match')



    else:

        db=mysql.connector.connect(host='localhost',password='1234',user='root',auth_plugin='mysql_native_password')
        cur=db.cursor()
    #
        #1st section
        try:
            query='create database p_registration'
            cur.execute(query)
            query='use p_registration'
            cur.execute(query)

            query='create table personaldata (id int auto_increment primary key not null, firstname varchar(40), ' \
                  'lastname varchar(40), email varchar(40), gender varchar(40), ' \
                  'username varchar(40), passwrd varchar(10), ' \
                  'confirmpasswrd varchar(10))'
            cur.execute(query)
            # messagebox.showinfo('Success','Database was created successfully')

        except:
            cur.execute('use p_registration')
            #2nd section
        query='insert into personaldata(firstname, lastname, email, gender,  username, passwrd, confirmpasswrd)' \
              ' values(%s,%s,%s,%s,%s,%s,%s)'
        cur.execute(query,(firstnameEntry.get(), lastnameEntry.get(), emailentry.get(), gender.get(),
                           usernameEntry.get(),passwordEntry.get(), renterpasswordEntry.get()))
        db.commit() #to execute the change
        db.close()
        messagebox.showinfo('Success', 'Successful Registration.')

        #to clear the fields after a successful registration
        firstnameEntry.delete(0, END)
        lastnameEntry.delete(0, END)
        emailentry.delete(0, END)
        usernameEntry.delete(0, END)
        passwordEntry.delete(0, END)
        renterpasswordEntry.delete(0, END)
        gender.set(0)
        

        windows.destroy()
        import loginpg


#section for getting data from the entry fields
firstname = StringVar()
lastname = StringVar()
email = StringVar()
gender = StringVar()
username = StringVar()
passwrd = StringVar()
confirmpasswrd = StringVar()

# frame=Frame(windows)
frame=Frame(windows, width=610, height=640 , bg='#06002e', bd=8)
frame.place(x=0,y=0)


pil_image = Image.open(r"C:\Users\hirth\OneDrive\Desktop\New folder (2)\working programs\download.jpg")

# Convert the PIL image object to a Tkinter PhotoImage object
tk_image = ImageTk.PhotoImage(pil_image)

# Create a label with the Tkinter image as the background
label = Label(windows, image=tk_image)
label.image = tk_image  # Keep a reference to the image

# Position the label to fill the entire window
label.place(x=0, y=0)



#labels on window
heading =Label(windows, text='Personal Registration Form', fg='#97FFFF', bg='blue', font=('Calibre', 20, 'bold'))
heading.place(x=90, y=3)




firstnameLabel= Label(windows, text="First Name:", fg='#97FFFF',bg='grey', font=('Calibre', 15, 'bold'))
firstnameLabel.place(x=10, y=70)

firstnameEntry=Entry(windows, width=30, borderwidth=2)
firstnameEntry.place(x=240, y=70)


lastnameLabel= Label(windows, text="Last Name:", fg='#97FFFF',bg='grey', font=('Calibre', 15, 'bold'))
lastnameLabel.place(x=10, y=110)

lastnameEntry=Entry(windows, width=30, borderwidth=2)
lastnameEntry.place(x=240, y=110)

idlabelEmail=Label(windows, text='Email:', fg='#97FFFF', bg='grey', font=('Calibre', 15, 'bold'))
idlabelEmail.place(x=10, y=150)

emailentry=Entry(windows, width=30, borderwidth=2)
emailentry.place(x=240, y=150)

genderLabel=Label(windows, text='Select Gender:', fg='#97FFFF', bg='grey', font=('Calibre', 15, 'bold'))
genderLabel.place(x=10, y=200)


gender.set(0)
genderRadio1=Radiobutton(windows, text='Male', variable=gender, value='Male', font='tahoma 13 bold')
# genderRadio1.select()
genderRadio1.place(x=240, y=200)


genderRadio2=Radiobutton(windows, text='Female', variable=gender, value='Female', font='tahoma 13 bold')
# genderRadio2.deselect()
genderRadio2.place(x=350, y=200)



usernamelbl = Label(windows, text='Username:', fg='#97FFFF', bg='grey', font=('Calibre', 15, 'bold'))
usernamelbl.place(x=10, y=300)

usernameEntry=Entry(windows, width=30, borderwidth=2)
usernameEntry.place(x=240, y=300)

passwordlbl = Label(windows, text='Password:', fg='#97FFFF', bg='grey', font=('Calibre', 15, 'bold'))
passwordlbl.place(x=10, y=350)

passwordEntry=Entry(windows, width=30, borderwidth=2)
passwordEntry.place(x=240, y=350)

renterpasswordlbl = Label(windows, text='Confirm Password:', fg='#97FFFF', bg='grey', font=('Calibre', 15, 'bold'))
renterpasswordlbl.place(x=10, y=400)

renterpasswordEntry=Entry(windows, width=30, borderwidth=2)
renterpasswordEntry.place(x=240, y=400)

# clearData = Button(frame, text='Clear Data', width=15, height=2, bg='grey',fg='grey', cursor='hand2', border=2)
# clearData.place(x=6, y=450)

# lblchkterms = Label(frame, text='Agree to Terms and Conditions', fg='#97FFFF', bg='grey', font=('Calibre', 15, 'bold'))
# lblchkterms.place(x=35, y=450)

bckbtn = Button(windows, text='<<', width=7, borderwidth=5, height=2, bg='black', fg='grey', cursor='hand2', border=2,
                command=back)
bckbtn.place(x=10, y=580)

submit1btn = Button(windows, text='Submit', width=15, borderwidth=5, height=2, bg='#7f7fff',fg='grey', cursor='hand2',
                    border=2,font=('#57a1f8', 16, 'bold'), command=submit)
submit1btn.place(x=150, y=500)

#to show and hide password
check1 = Checkbutton(windows, text='',
        command=show, bg='grey')
check1.place(x=420, y=350)

check2 = Checkbutton(windows, text='',
        command=show1, bg='grey')
check2.place(x=420, y=400)


windows.mainloop()