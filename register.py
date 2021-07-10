import mysql.connector
from tkinter import *
from tkinter import messagebox
import datetime
from validate_email import validate_email
import rsaidnumber


window = Tk()
window.geometry("500x500")
window.title("lifechoices online Login Page")

# definition
mydb = mysql.connector.connect(user="lifechoices",
                               password="@Lifechoices1234", host="127.0.0.1", database="LS_Login",
                               auth_plugin="mysql_native_password")
mycursor = mydb.cursor()
xy = mycursor.execute("select*from Login")
for i in mycursor:
    print(i)


def registration():
    global mydb
    sql = "INSERT INTO Login(Name, Surname, ID_number, Contact_number, Next_of_kin_name, " \
          "Next_of_kin_number, username, Password) VALUES(%s, %s, %s, %s, %s, %s, %s, %s)"
    val = (userentry.get(), entrypass.get(), identry.get(), numbentry.get(), nextentry.get(), kinentry.get(), username_en.get(), pass_en.get())
    mycursor.execute(sql, val)
    mydb.commit()
    mycursor.execute("Select * from Login")
    for i in mycursor:
        print(i)
    messagebox.showinfo("Congradulations", "you are part of lifechoices academy")
    window.destroy()
    import signin


def clear():
    entrypass.delete(0, 'end')
    userentry.delete(0, 'end')
    identry.delete(0, 'end')
    numbentry.delete(0, 'end')
    nextentry.delete(0, 'end')
    kinentry.delete(0, 'end')
    username_en.delete(0, 'end')
    pass_en.delete(0, 'end')






def close():
    mgbox = messagebox.askquestion("exit application", "are you sure you want to exit", icon="warning")
    if mgbox == "yes":
        window.destroy()
    else:
        messagebox.showinfo("return", "you'll return to your application")


# Defining the first row
heading = Label(window, text="Life choices Registration", font=100, bg="#8DC63F")
heading.place(x=100, y=10)

lbluser = Label(window, text="Enter your Surname", font=20)
lbluser.place(x=50, y=100)
userentry = Entry(window, width=25)
userentry.place(x=280, y=100)

lblpass = Label(window, text="Enter your Name", font=20,)
lblpass.place(x=50, y=130)
entrypass = Entry(window, width=25)
entrypass.place(x=280, y=130)

lbluser = Label(window, text="Enter your Id number", font=20)
lbluser.place(x=50, y=160)
identry = Entry(window, width=25)
identry.place(x=280, y=160)

numb = Label(window, text="Enter your number", font=20)
numb.place(x=50, y=190)
numbentry = Entry(window, width=25)
numbentry.place(x=280, y=190)

next = Label(window, text="Enter next of kin name", font=20)
next.place(x=50, y=220)
nextentry = Entry(window, width=25)
nextentry.place(x=280, y=220)

kin = Label(window, text="Enter next of kin contacts", font=20)
kin.place(x=50, y=250)
kinentry = Entry(window, width=25)
kinentry.place(x=280, y=250)

username_lbl = Label(window, text="Create username", font=20)
username_lbl.place(x=50, y=280)
username_en = Entry(window, width=25)
username_en.place(x=280, y=280)

pass_lbl = Label(window, text="Create password", font=20)
pass_lbl.place(x=50, y=320)
pass_en = Entry(window, width=25)
pass_en.place(x=280, y=320)


# buttons

reset_btn = Button(window, text='clear', bg='#8DC63F', pady=10, width=10, command=clear)
reset_btn.place(x=380, y=370)

exit_btn = Button(window, text='Exit', bg='#8DC63F', pady=10, width=10, command=close)
exit_btn.place(x=380, y=420)

cal_btn = Button(window, text='register', bg='#8DC63F', pady=10, width=10, command=registration)
cal_btn.place(x=120, y=370)


window.mainloop()

