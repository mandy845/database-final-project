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

# labels
lbluser = Label(window, text="Enter your Username", bg='yellow', font=20)
lbluser.place(x=100, y=250)

userentry = Entry(window, width=25)
userentry.place(x=330, y=250)

lblpass = Label(window, text="Enter your email address", bg='yellow', font=20,)
lblpass.place(x=100, y=280)

entrypass = Entry(window, width=25)
entrypass.place(x=330, y=280)


window.mainloop()