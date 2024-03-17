from tkinter.ttk import *
from tkinter import *
from tkinter import messagebox
from basa import Database
import os

windows = Tk()
windows.configure(bg="#569246")
width = windows.winfo_screenwidth()
height = windows.winfo_screenheight()
center_x = int(width / 2 - 500 / 2)
center_y = int(height / 2 - 550 / 2)
windows.geometry(f"500x550+{center_x}+{center_y}")
db = Database()


def login_open():
    os.system("python login.py")



def register():
    username = username_entry.get()
    password = password_entry.get()
    email = email_entry.get()
    country = country_entry.get()
    age = age_entry.get()
    phone_number = phone_entry.get()
    if username and password and phone_number:
        messagebox.showinfo(title="Success",
                            message="Successfully Registered")
        db.insert_user(username=username.lower(), password=password, email=email,
                       country=country, age=age, phone_number=phone_number)
        windows.destroy()
        login_open()
    else:
        messagebox.showerror(title="Xato",
                             message="Username va Password ")
        login_open()


frame = Frame(bg="white")
frame.grid(padx=60, pady=45)

user_frame = LabelFrame(frame)
user_frame.grid(row=0, column=0, padx=30, pady=30)

register_label = Label(user_frame,
                       text="Registration",
                       fg="#569246",
                       font=("gill sans", 20, "bold"))
register_label.grid(row=0, column=0, columnspan=2)

username_label = Label(user_frame,
                         text="Username",
                         fg="#569246",
                         font=("gill sans", 10))
username_label.grid(row=1, column=0)
username_entry = Entry(user_frame, bg="#569246")
username_entry.grid(row=2, column=0, ipady=5)

password_label = Label(user_frame,
                        text="Password",
                        fg="#569246",
                        font=("gill sans", 10))
password_label.grid(row=1, column=1)
password_entry = Entry(user_frame, bg="#569246")
password_entry.grid(row=2, column=1, ipady=5)

email_label = Label(user_frame,
                    text="Email",
                    fg="#569246",
                    font=("gill sans", 10))
email_label.grid(row=3, column=0)
email_entry = Entry(user_frame, bg="#569246", width=45)
email_entry.grid(row=4, column=0, ipady=5, columnspan=2)

country_label = Label(user_frame,
                      text="Country",
                      fg="#569246",
                      font=("gill sans", 10))
country_label.grid(row=5, column=0)
country_entry = Combobox(user_frame,
                         background="#569246",
                         width=42,
                         values=["Uzbekistan", "Russian", "Turkiye",
                                 "USA", "Brazil"])
country_entry.grid(row=6, column=0, ipady=5, columnspan=2)

age_label = Label(user_frame,
                  text="Age",
                  fg="#569246",
                  font=("gill sans", 10))
age_label.grid(row=7, column=0)
age_entry = Spinbox(user_frame, bg="#569246", from_=0, to=20)
age_entry.grid(row=8, column=0, ipady=5)

phone_label = Label(user_frame,
                    text="Phone Number",
                    fg="#569246",
                    font=("gill sans", 10))
phone_label.grid(row=7, column=1)
phone_entry = Entry(user_frame, bg="#569246")
phone_entry.grid(row=8, column=1, ipady=5)

button = Button(user_frame,
                text="Register",
                fg="#569246",
                font=("gill sans", 10, "bold"),
                command=register)
button.grid(row=9, column=0, columnspan=2, sticky="news")

for widget in user_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)

windows.mainloop()