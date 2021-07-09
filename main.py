from tkinter import *
from tkinter import messagebox
window = Tk()
window.geometry("400x400")
window.title("lifechoices online Login Page")

canvas = Canvas(window, width=593, height=176)
canvas.place(x=0, y=0)
img = PhotoImage(file="download.png")
canvas.create_image(0, 0, anchor=NW, image=img)

# definitions

def asign():
    mgbox = messagebox.askquestion("Welcome to Lifechoices", "do you want to log in as User")

    if mgbox == "yes":
        messagebox.showinfo("Welcome to Life choices!", "Enjoy being part of us")
        window.destroy()
        import signin
    else:
        messagebox.showinfo("welcome back admin", "you will get to admin user screen")
        window.destroy()
        import admin

def exit():
    mgbox = messagebox.askquestion("exit application", "are you sure you want to exit", icon="warning")

    if mgbox == "yes":
        window.destroy()
    else:
        messagebox.showinfo("return", "you'll return to your application")


# Labels


# button
reset_btn = Button(window, text='Login', bg='#8DC63F', pady=10, width=10, command=asign)
reset_btn.place(x=100, y=210)

exit_btn = Button(window, text='Exit', bg='#8DC63F', pady=10, width=10, command=exit)
exit_btn.place(x=200, y=210)


window.mainloop()