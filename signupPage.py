from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
import os

class SignUpPage:
    def __init__(self, window):
        self.window = window
        self.window.geometry('1166x718')
        self.window.resizable(0, 0)
        self.window.state('zoomed')
        self.window.title('Sign Up Page')

        # Background Image
        self.bg_frame = Image.open('background1.png')
        self.bg_photo = ImageTk.PhotoImage(self.bg_frame)
        self.bg_panel = Label(self.window, image=self.bg_photo)
        self.bg_panel.image = self.bg_photo
        self.bg_panel.pack(fill='both', expand='yes')

        # Sign Up Frame
        self.signup_frame = Frame(self.window, bg='#040405', width=950, height=600)
        self.signup_frame.place(x=200, y=70)

        # Heading
        self.heading = Label(self.signup_frame, text="SIGN UP", font=('yu gothic ui', 25, "bold"), bg="#040405",
                             fg='white', bd=5, relief=FLAT)
        self.heading.place(x=80, y=30, width=300, height=30)

        # First Name
        self.first_name_label = Label(self.signup_frame, text="First Name", bg="#040405", fg="#4f4e4d",
                                      font=("yu gothic ui", 13, "bold"))
        self.first_name_label.place(x=100, y=100)

        self.first_name_entry = Entry(self.signup_frame, highlightthickness=0, relief=FLAT, bg="#040405", fg="#6b6a69",
                                      font=("yu gothic ui ", 12, "bold"), insertbackground='#6b6a69')
        self.first_name_entry.place(x=230, y=100, width=270)

        self.first_name_line = Canvas(self.signup_frame, width=300, height=2.0, bg="#bdb9b1", highlightthickness=0)
        self.first_name_line.place(x=100, y=124)

        # Last Name
        self.last_name_label = Label(self.signup_frame, text="Last Name", bg="#040405", fg="#4f4e4d",
                                     font=("yu gothic ui", 13, "bold"))
        self.last_name_label.place(x=100, y=150)

        self.last_name_entry = Entry(self.signup_frame, highlightthickness=0, relief=FLAT, bg="#040405", fg="#6b6a69",
                                     font=("yu gothic ui", 12, "bold"), insertbackground='#6b6a69')
        self.last_name_entry.place(x=230, y=150, width=270)

        self.last_name_line = Canvas(self.signup_frame, width=300, height=2.0, bg="#bdb9b1", highlightthickness=0)
        self.last_name_line.place(x=100, y=174)

        # Username
        self.username_label = Label(self.signup_frame, text="Username", bg="#040405", fg="#4f4e4d",
                                    font=("yu gothic ui", 13, "bold"))
        self.username_label.place(x=100, y=200)

        self.username_entry = Entry(self.signup_frame, highlightthickness=0, relief=FLAT, bg="#040405", fg="#6b6a69",
                                    font=("yu gothic ui ", 12, "bold"), insertbackground='#6b6a69')
        self.username_entry.place(x=230, y=200, width=270)

        self.username_line = Canvas(self.signup_frame, width=300, height=2.0, bg="#bdb9b1", highlightthickness=0)
        self.username_line.place(x=100, y=224)

        # Password
        self.password_label = Label(self.signup_frame, text="Password", bg="#040405", fg="#4f4e4d",
                                    font=("yu gothic ui", 13, "bold"))
        self.password_label.place(x=100, y=250)

        self.password_entry = Entry(self.signup_frame, highlightthickness=0, relief=FLAT, bg="#040405", fg="#6b6a69",
                                    font=("yu gothic ui", 12, "bold"), show="*", insertbackground='#6b6a69')
        self.password_entry.place(x=230, y=250, width=270)

        self.password_line = Canvas(self.signup_frame, width=300, height=2.0, bg="#bdb9b1", highlightthickness=0)
        self.password_line.place(x=100, y=274)

        # Confirm Password
        self.confirm_password_label = Label(self.signup_frame, text="Confirm Password", bg="#040405", fg="#4f4e4d",
                                             font=("yu gothic ui", 13, "bold"))
        self.confirm_password_label.place(x=100, y=300)

        self.confirm_password_entry = Entry(self.signup_frame, highlightthickness=0, relief=FLAT, bg="#040405",
                                            fg="#6b6a69", font=("yu gothic ui", 12, "bold"), show="*",
                                            insertbackground='#6b6a69')
        self.confirm_password_entry.place(x=230, y=300, width=270)

        self.confirm_password_line = Canvas(self.signup_frame, width=300, height=2.0, bg="#bdb9b1",
                                             highlightthickness=0)
        self.confirm_password_line.place(x=100, y=324)
        # Sign Up Button
        self.signup_button = Image.open('btn1.png')
        self.signup_button_photo = ImageTk.PhotoImage(self.signup_button)
        self.signup_button_label = Label(self.signup_frame, image=self.signup_button_photo, bg='#040405')
        self.signup_button_label.image = self.signup_button_photo
        self.signup_button_label.place(x=200, y=450)
        self.signup = Button(self.signup_button_label, text='SIGN UP', font=("yu gothic ui", 13, "bold"), width=25,
                             bd=0, bg='#3047ff', cursor='hand2', activebackground='#3047ff', fg='white',
                             command=self.sign_up_clicked)
        self.signup.place(x=20, y=10)

        # Vector Image
        self.vector_image = Image.open('vector.png')
        self.vector_photo = ImageTk.PhotoImage(self.vector_image)
        self.vector_label = Label(self.signup_frame, image=self.vector_photo, bg='#040405')
        self.vector_label.image = self.vector_photo
        self.vector_label.place(x=600, y=100)

    def sign_up_clicked(self):
        # Retrieve entered values
        first_name = self.first_name_entry.get()
        last_name = self.last_name_entry.get()
        username = self.username_entry.get()
        password = self.password_entry.get()
        confirm_password = self.confirm_password_entry.get()

        # Perform validation here
        if not all([first_name, last_name, username, password, confirm_password]):
            messagebox.showerror("Error", "Please fill in all fields.")
            return

        if password != confirm_password:
            messagebox.showerror("Error", "Passwords do not match. Please try again.")
            return

        # Perform sign up process here
        # For now, let's just print the values
        print("First Name:", first_name)
        print("Last Name:", last_name)
        print("Username:", username)
        print("Password:", password)
        print("Confirm Password:", confirm_password)

        # Close current window
        self.window.destroy()

        # Open login page
        os.system("python LoginPage.py")


def page():
    window = Tk()
    SignUpPage(window)
    window.mainloop()


if __name__ == '__main__':
    page()
