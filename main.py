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
mycurso = mydb.cursor()
xy = mycurso.execute("select*from Login")
for i in mycurso:
    print(i)

def clear():
    entrypass.delete(0, 'end')
    userentry.delete(0, 'end')
    identry.delete(0, 'end')


def close():
    mgbox = messagebox.askquestion("exit application", "are you sure you want to exit", icon="warning")
    if mgbox == "yes":
        window.destroy()
    else:
        messagebox.showinfo("return", "you'll return to your application")


def login():
    id = rsaidnumber.parse(identry.get())
    current_year = datetime.date.today().year
    year_of_birth = id.date_of_birth.year
    age = current_year - year_of_birth


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

next = Label(window, text="Enter your name (next of kin)")
next.place(x=50, y=220)
nextentry = Entry(window, width=25)
nextentry.place(x=280, y=220)

kin = Label(window, text="Enter contact No(next of kin)")
kin.place(x=50, y=250)
kinentry = Entry(window, width=25)
kinentry.place(x=280, y=250)


# buttons

reset_btn = Button(window, text='clear', bg='#8DC63F', pady=10, width=10, command=clear)
reset_btn.place(x=430, y=370)

exit_btn = Button(window, text='Exit', bg='#8DC63F', pady=10, width=10, command=close)
exit_btn.place(x=430, y=420)

cal_btn = Button(window, text='register', bg='#8DC63F', pady=10, width=10)
cal_btn.place(x=120, y=370)


window.mainloop()

