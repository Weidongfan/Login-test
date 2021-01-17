from tkinter import *
import random
import os

def register_user():
    username_info = username.get()
    password_info = password.get()

    with open("newuser_info", "w") as userinfo:
        userinfo.write(username_info + ":" + password_info)

    username_entry.delete(0, END)
    password_entry.delete(0, END)
    Label(screen1, text="Registration is successful!", fg="green", font=("Calibre", 16)).pack()

def delete3():
    screen3.destroy()

def delete4():
    screen4.destroy()

def delete5():
    screen5.destroy()

def success():
    global screen3
    screen3 = Toplevel(screen)
    screen3.title("Login Info")
    screen3.geometry("200x200")
    Label(screen3, text="Login success!", bg="red", font=("Calibre", 16)).pack()
    Button(screen3, text="OK", bg="grey", font=("Calibre", 18), command=delete3).pack()

def wrong_password():
    global screen4
    screen4 = Toplevel(screen)
    screen4.title("Login Info")
    screen4.geometry("200x200")
    Label(screen4, text="Password is not correct, please try again!", bg="red", font=("Calibre", 16)).pack()
    Button(screen4, text="OK", bg="grey", font=("Calibre", 18), command=delete4).pack()

def user_notexist():
    global screen5
    screen5 = Toplevel(screen)
    screen5.title("Login Info")
    screen5.geometry("200x200")
    Label(screen5, text="User not found!", bg="red", font=("Calibre", 16)).pack()
    Button(screen5, text="OK", bg="grey", font=("Calibre", 18), command=delete5).pack()

def login_verify():
    username1 = username_verify.get()
    password1 = password_verify.get()
    username_entry1.delete(0, END)
    password_entry1.delete(0, END)

    list_of_file = os.listdir()
    if username1 in list_of_file:
        file1 = open(usename1, "r")
        verify = file1.read().splitlines()
        if password1 in verify:
            success()
        else:
            wrong_password()
    else:
        user_notexist()


def generate_password():
    passwordbase = "ABCDEFGHabcdefgh!@(*$&*(!127384"
    randompassword = "".join(random.choice(passwordbase) for i in range(8))
    Label(screen1, text=randompassword, bg="grey", font=("Calibre", 18)).pack()


def register():
    global screen1
    global username
    global password
    global username_entry
    global password_entry

    screen1 = Toplevel(screen)
    screen1.title("Register Page")
    screen1.geometry("300x300")

    username = StringVar()
    password = StringVar()

    Label(screen1, text="Please input your username here: ").pack()
    Label(screen1, text="User name: ").pack()
    username_entry = Entry(screen1, textvariable=username)
    username_entry.pack()
    Label(screen1, text="Please input your password here: ").pack()
    Label(screen1, text="Password: ").pack()
    password_entry = Entry(screen1, textvariable=password)
    password_entry.pack()
    Button(screen1, text="Register", bg="grey", font=("Calibre", 18), command=register_user).pack()
    Label(screen1, text="").pack()
    Label(screen1, text="Password Generator", bg="green", font=("Calibre", 18)).pack()
    Button(screen1, text="Generate", bg="grey", font=("Calibre", 18), command=generate_password).pack()


def login():
    global screen2
    global username_verify, password_verify, username_entry1, password_entry1

    screen2 = Toplevel(screen)
    screen2.title("Login Page")
    screen2.geometry("300x300")

    username_verify = StringVar()
    password_verify = StringVar()

    Label(screen2, text="Please input your username here: ").pack()
    Label(screen2, text="User name: ").pack()
    username_entry1 = Entry(screen2, textvariable=username_verify)
    username_entry1.pack()
    Label(screen2, text="Please input your password here: ").pack()
    Label(screen2, text="Password: ").pack()
    password_entry1 = Entry(screen2, textvariable=password_verify)
    password_entry1.pack()
    Button(screen2, text="Login", bg="grey", font=("Calibre", 18), command=login_verify).pack()
    Label(screen2, text="").pack()


def main_screen():
    global screen
    screen = Tk()
    screen.geometry("400x400")
    screen.title("Login Window")
    Label(text="User Page", bg="yellow", font=("Calibre", 20)).pack()
    Label(text="").pack()
    Button(text="Login", bg="grey", font=("Calibre", 16), command=login).pack()
    Label(text="").pack()
    Button(text="Register New User", bg="grey", font=("Calibre", 16), command=register).pack()

    screen.mainloop()

main_screen()