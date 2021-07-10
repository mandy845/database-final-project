from tkinter import *
from tkinter import messagebox
window = Tk()
window.geometry("400x300")
window.title("lifechoices online Login Page")

canvas = Canvas(window, width=593, height=176)
canvas.place(x=0, y=0)
img = PhotoImage(file="lifechoices.png")
canvas.create_image(0, 0, anchor=NW, image=img)

# definitions


def asign():
    mgbox = messagebox.askquestion("Welcome to Lifechoices", "Are you an Admin?")

    if mgbox == "yes":
        messagebox.showinfo("Welcome back Admin,", "you will return to your log in screen")
        window.destroy()
        import admin
    else:
        messagebox.showinfo("welcome to Lifechoices", "you will get to log in screen if you are registered,if you are not please click the register button")
        window.destroy()
        import signin


def exit():
    mgbox = messagebox.askquestion("exit application", "are you sure you want to exit", icon="warning")

    if mgbox == "yes":
        window.destroy()
    else:
        messagebox.showinfo("return", "you'll return to your application")


# Labels


# button
reset_btn = Button(window, text='Login', bg='#8DC63F', pady=10, width=10, command=asign)
reset_btn.place(x=0, y=150)

exit_btn = Button(window, text='Exit', bg='#8DC63F', pady=10, width=10, command=exit)
exit_btn.place(x=120, y=150)


window.mainloop()