from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
import os
import random
import string

class LoginPage:
    def __init__(self, window):
        self.window = window
        self.window.title('Login Page')

        # Background frame
        self.bg_frame = Frame(self.window, bg="#040405")
        self.bg_frame.place(relx=0, rely=0, relwidth=1, relheight=1)

        # Background image
        self.bg_image = Image.open('background1.png')
        self.bg_photo = ImageTk.PhotoImage(self.bg_image)
        self.bg_panel = Label(self.bg_frame, image=self.bg_photo)
        self.bg_panel.place(x=0, y=0, relwidth=1, relheight=1)

        # Login Frame
        self.lgn_frame = Frame(self.window, bg='#040405', width=950, height=600)
        self.lgn_frame.place(x=200, y=70)

        # Welcome text
        self.txt = "WELCOME"
        self.heading = Label(self.lgn_frame, text=self.txt, font=('yu gothic ui', 25, "bold"), bg="#040405",
                             fg='white',
                             bd=5,
                             relief=FLAT)
        self.heading.place(x=80, y=30, width=300, height=30)

        # Left side image
        self.side_image = Image.open('vector.png')
        self.side_photo = ImageTk.PhotoImage(self.side_image)
        self.side_image_label = Label(self.lgn_frame, image=self.side_photo, bg='#040405')
        self.side_image_label.image = self.side_photo
        self.side_image_label.place(x=5, y=100)

        # Sign In Image
        self.sign_in_image = Image.open('hyy.png')
        self.sign_photo = ImageTk.PhotoImage(self.sign_in_image)
        self.sign_in_image_label = Label(self.lgn_frame, image=self.sign_photo, bg='#040405')
        self.sign_in_image_label.image = self.sign_photo
        self.sign_in_image_label.place(x=620, y=130)

        # Sign In label
        self.sign_in_label = Label(self.lgn_frame, text="Sign In", bg="#040405", fg="white",
                                    font=("yu gothic ui", 17, "bold"))
        self.sign_in_label.place(x=650, y=240)

        # Username entry
        self.username_label = Label(self.lgn_frame, text="Username", bg="#040405", fg="#4f4e4d",
                                    font=("yu gothic ui", 13, "bold"))
        self.username_label.place(x=550, y=300)

        self.username_entry = Entry(self.lgn_frame, highlightthickness=0, relief=FLAT, bg="#040405", fg="#6b6a69",
                                    font=("yu gothic ui ", 12, "bold"), insertbackground='#6b6a69')
        self.username_entry.place(x=580, y=335, width=270)

        self.username_line = Canvas(self.lgn_frame, width=300, height=2.0, bg="#bdb9b1", highlightthickness=0)
        self.username_line.place(x=550, y=359)

        # Username icon
        self.username_icon = Image.open('username_icon.png')
        self.username_icon_photo = ImageTk.PhotoImage(self.username_icon)
        self.username_icon_label = Label(self.lgn_frame, image=self.username_icon_photo, bg='#040405')
        self.username_icon_label.image = self.username_icon_photo
        self.username_icon_label.place(x=550, y=332)

        # Login button
        self.lgn_button = Image.open('btn1.png')
        self.lgn_button_photo = ImageTk.PhotoImage(self.lgn_button)
        self.lgn_button_label = Label(self.lgn_frame, image=self.lgn_button_photo, bg='#040405')
        self.lgn_button_label.image = self.lgn_button_photo
        self.lgn_button_label.place(x=550, y=450)
        self.login = Button(self.lgn_button_label, text='LOGIN', font=("yu gothic ui", 13, "bold"), width=25, bd=0,
                            bg='#3047ff', cursor='hand2', activebackground='#3047ff', fg='white',
                            command=self.login_clicked)
        self.login.place(x=20, y=10)

        # Forgot password button
        self.forgot_button = Button(self.lgn_frame, text="Forgot Password ?",
                                    font=("yu gothic ui", 13, "bold underline"), fg="white", relief=FLAT,
                                    activebackground="#040405", borderwidth=0, background="#040405",
                                    cursor="hand2", command=self.forgot_password)
        self.forgot_button.place(x=630, y=510)

        # Password entry
        self.password_label = Label(self.lgn_frame, text="Password", bg="#040405", fg="#4f4e4d",
                                    font=("yu gothic ui", 13, "bold"))
        self.password_label.place(x=550, y=380)

        self.password_entry = Entry(self.lgn_frame, highlightthickness=0, relief=FLAT, bg="#040405", fg="#6b6a69",
                                    font=("yu gothic ui", 12, "bold"), show="*", insertbackground='#6b6a69')
        self.password_entry.place(x=580, y=416, width=244)

        self.password_line = Canvas(self.lgn_frame, width=300, height=2.0, bg="#bdb9b1", highlightthickness=0)
        self.password_line.place(x=550, y=440)

        # Password icon
        self.password_icon = Image.open('password_icon.png')
        self.password_icon_photo = ImageTk.PhotoImage(self.password_icon)
        self.password_icon_label = Label(self.lgn_frame, image=self.password_icon_photo, bg='#040405')
        self.password_icon_label.image = self.password_icon_photo
        self.password_icon_label.place(x=550, y=414)

        # Show/Hide password button
        self.show_image = ImageTk.PhotoImage(file='show.png')
        self.hide_image = ImageTk.PhotoImage(file='hide.png')
        self.show_button = Button(self.lgn_frame, image=self.show_image, command=self.show, relief=FLAT,
                                  activebackground="white", borderwidth=0, background="white", cursor="hand2")
        self.show_button.place(x=860, y=420)

    def show(self):
        self.hide_button = Button(self.lgn_frame, image=self.hide_image, command=self.hide, relief=FLAT,
                                  activebackground="white", borderwidth=0, background="white", cursor="hand2")
        self.hide_button.place(x=860, y=420)
        self.password_entry.config(show='')

    def hide(self):
        self.show_button = Button(self.lgn_frame, image=self.show_image, command=self.show, relief=FLAT,
                                  activebackground="white", borderwidth=0, background="white", cursor="hand2")
        self.show_button.place(x=860, y=420)
        self.password_entry.config(show='*')

    def login_clicked(self):
        # Perform login validation here (dummy validation for now)
        # Replace this with your actual login validation code
        username = self.username_entry.get()
        password = self.password_entry.get()
        if (username == "admin" and password == "admin") or (username == "admin" and password == self.new_password):
            messagebox.showinfo("Success", "Login Successful!")
            # Open main page
            os.system("python menubar.py")
        else:
            messagebox.showerror("Error", "Invalid username or password. Please try again.")

    def forgot_password(self):
        # Generate a new password
        self.new_password = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
        # Display the new password in a messagebox
        messagebox.showinfo("New Password", f"Your new password is: {self.new_password}")

def page():
    window = Tk()
    LoginPage(window)
    window.mainloop()

if __name__ == '__main__':
    page()
