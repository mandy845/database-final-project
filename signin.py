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

obj = {}
for i in mycurso:
    rcv = {i[6]: i[7]}
    keys = rcv.keys()
    entries = rcv.values()

    for key in keys:
        for entry in entries:
            obj[key] = entry

print(obj)


def register():
    window.destroy()
    import register


user_pass = obj


def clear_entry():
    userentry.delete(0, 'end')
    entrypass.delete(0, 'end')


def user_pass_search(username, _password, _dict):
    if username in _dict:
        if _password == _dict[username]:
            return 1
        else:
            return 0
    else:
        return -1



def verify():
    user = userentry.get()
    password = entrypass.get()

    x = int(user_pass_search(user, password, user_pass))
    print(" ")
    if x == 1:
        now = datetime.datetime.now()
        date = "{}".format(now.date())
        minute = now.minute
        hour = now.hour
        if minute <= 9:
            minute = "0" + str(minute)
        if hour <= 9:
            hour = "0" + str(hour)
        time = "{}:{}".format(hour, minute)
        mycurso.execute("UPDATE Login SET sign_in_time ='" + time + "' WHERE username='" + userentry.get() + "'")
        mydb.commit()
        messagebox.showinfo("successful", "you have successfully logged in")
        window.destroy()

    elif x == 0:
        messagebox.showinfo("Alert", "Incorrect password ")
        userentry.delete(0, 'end')
        entrypass.delete(0, 'end')
    elif x == -1:
        messagebox.showinfo("Alert", "Username Doesn't Exist")
        userentry.delete(0, 'end')
        entrypass.delete(0, 'end')


def sign_out():
    user = userentry.get()
    password = entrypass.get()

    x = int(user_pass_search(user, password, user_pass))
    print(" ")
    if x == 1:
        now = datetime.datetime.now()
        date = "{}".format(now.date())
        minute = now.minute
        hour = now.hour
        if minute <= 9:
            minute = "0" + str(minute)
        if hour <= 9:
            hour = "0" + str(hour)
        time = "{}:{}".format(hour, minute)
        mycurso.execute("UPDATE Login SET sign_out_time ='" + time + "' WHERE username='" + userentry.get() + "'")
        mydb.commit()
        messagebox.showinfo("successful", "you have successfully logged out")
        window.destroy()

    elif x == 0:
        messagebox.showinfo("Alert", "Incorrect password ")
        userentry.delete(0, 'end')
        entrypass.delete(0, 'end')
    elif x == -1:
        messagebox.showinfo("Alert", "Username Doesn't Exist")
        userentry.delete(0, 'end')
        entrypass.delete(0, 'end')


# labels

heading = Label(window, text="Life choices Registration", font=100, bg="#8DC63F")
heading.place(x=100, y=10)

lbluser = Label(window, text="Enter your username", font=20)
lbluser.place(x=50, y=100)
userentry = Entry(window, width=25)
userentry.place(x=280, y=100)

lblpass = Label(window, text="Enter your password", font=20,)
lblpass.place(x=50, y=130)
entrypass = Entry(window, width=25)
entrypass.place(x=280, y=130)

# buttons

reset_btn = Button(window, text='clear', bg='#8DC63F', pady=10, width=10, command=clear_entry)
reset_btn.place(x=380, y=210)

exit_btn = Button(window, text='Exit', bg='#8DC63F', pady=10, width=10, command=lambda: window.destroy())
exit_btn.place(x=380, y=260)

cal_btn = Button(window, text='register', bg='#8DC63F', pady=10, width=10, command=register)
cal_btn.place(x=120, y=210)

loginbtn= Button(window, text="Login", bg='#8DC63F', pady=10, width=10, command=verify)
loginbtn.place(x=120, y=260)

logoutbtn = Button(window, text="Logout", bg='#8DC63F', pady=10, width=10, command=sign_out)
logoutbtn.place(x=120, y=300)

window.mainloop()