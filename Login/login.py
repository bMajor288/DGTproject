from tkinter import *
from tkinter import messagebox

root = Tk()

root.title("Login")
root.geometry("200x200")

#Functions
#Makes temporary text in entry boxes
def temp_text_u(e):
    if username_box.get() == "Enter your username":
        username_box.delete(0, "end")
def return_text_u(e):
    if username_box.get() == "":
        username_box.insert(0, "Enter your username")
def temp_text_p(e):
    if password_box.get() == "Enter your password":
        password_box.delete(0, "end")
def return_text_p(e):
    if password_box.get() == "":
        password_box.insert(0, "Enter your password")
#Account
def signup():
    db = open("credentials.txt", "r")
    username = username_box.get()
    password = password_box.get()
    if len(password) < 6:
        db.close()
        messagebox.showwarning("Try again", "Password must be at least 6 characters long")
        return
    else:

        messagebox.showinfo("Success", f"Password is {password}\nIt is {len(password)} characters")
    if " " in username or password:
        db.close()
        messagebox.showerror("Try again", "Username and password cannot contain spaces")
        return

def login():
    username = username_box.get()
    password = password_box.get()
    with open("credentials.txt", "r") as file:
        for i in file:
            if username in file:
                print("user found")
                break
            elif username not in file: 
                print(i)
                print("wrong")
                continue

    # if username_box.get()==username and password_box.get()==password:
    #     pass

def generate_UUID():
    pass

#Creating frames
entry_frame = Frame(root)
entry_frame.grid(row=0, column=0)
button_frame = Frame(root)
button_frame.grid(row=1, column=0)

#Creating entry boxes
username_box = Entry(entry_frame, bg="black", fg="white")
username_box.insert(0, "Enter your username")
username_box.grid(row=1, column=1, pady=20)
password_box = Entry(entry_frame, bg="black", fg="white")
password_box.insert(0, "Enter your password")
password_box.grid(row=2, column=1)
#Binding entry boxes to commands
username_box.bind("<FocusIn>", temp_text_u)
username_box.bind("<FocusOut>", return_text_u)
password_box.bind("<FocusIn>", temp_text_p)
password_box.bind("<FocusOut>", return_text_p)

#Buttons
signup_button = Button(button_frame, text="Sign up", command=signup)
signup_button.grid(row=0, column=0, pady=15)
login_button = Button(button_frame, text="Login", command=login)
login_button.grid(row=0, column=1)
remember_button = Radiobutton(button_frame, text="Remember me")
remember_button.grid(row=1, column=0)



root.mainloop()