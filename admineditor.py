from tkinter import *
from tkinter import messagebox
import mysql.connector

window = Tk()
window.geometry("500x400")
window.title("lifechoices online Login Page")


# definitions

def exit():
    mgbox = messagebox.askquestion("exit application", "are you sure you want to exit", icon="warning")

    if mgbox == "yes":
        window.destroy()
    else:
        messagebox.showinfo("return", "you'll return to your application")


delete_add = mysql.connector.connect(user="lifechoices", password="@Lifechoices1234", host="127.0.0.1",
                                     database="LS_Login", auth_plugin="mysql_native_password")

mycursor = delete_add.cursor(buffered=True)


def delete_user():
    mycursor.execute('DELETE FROM Login WHERE Name="' + namentry.get() + '"')
    delete_add.commit()
    messagebox.showinfo("successful", "you have successfully deleted a user")


def make_admin():
    mycursor.execute("SELECT username, password from Login WHERE Name='" + namentry.get() + "'")
    val = mycursor.fetchall()
    tpt = ""
    for i in val:
        tpt = i
        print(tpt)
    print("INSERT INTO Admin_user(username, password) VALUES(" + tpt[0] + ", " + tpt[1] + ")")
    mycursor.execute("INSERT INTO Admin_user(username, password) VALUES('"+ tpt[0] + "', '" + tpt[1] + "')")
    delete_add.commit()
    messagebox.showinfo("successful", "you have successfully a user")


# labels


heading = Label(window, text="Life choices Admin user", font=100, bg="#8DC63F")
heading.place(x=100, y=10)

name = Label(window, text="Enter your name", font=20)
name.place(x=50, y=100)
namentry = Entry(window, width=25)
namentry.place(x=200, y=100)

# buttons

exit_btn = Button(window, text='Make admin', bg='#8DC63F', pady=10, width=10, command=make_admin)
exit_btn.place(x=380, y=260)

delete = Button(window, text="exit", bg='#8DC63F', pady=10, width=10, command=exit)
delete.place(x=120, y=260)

makeadmin = Button(window, text='Delete user', bg='#8DC63F', pady=10, width=10,command=delete_user)
makeadmin.place(x=380, y=210)

window.mainloop()