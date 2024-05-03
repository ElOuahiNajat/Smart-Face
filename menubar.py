import tkinter as tk
from tkinter import PhotoImage
import subprocess

# Dictionary of colors:
color = {"nero": "#252726", "lavender": "#E6E6FA", "black": "#000000", "white": "#FFFFFF", "green": "#008000"}

# Setting root window:
root = tk.Tk()
root.title("Tkinter Navbar")
root.config(bg="lavender")
root.geometry("400x600+850+50")

# Setting switch state:
btnState = False

# Loading Navbar icon image:
navIcon = PhotoImage(file="menu.png")
closeIcon = PhotoImage(file="close.png")

# Setting switch function:
def switch():
    global btnState
    if btnState is True:
        # Create animated Navbar closing:
        for x in range(301):
            navRoot.place(x=-x, y=0)
            topFrame.update()

        # Resetting widget colors:
        brandLabel.config(bg="lavender", fg="green")
        homeLabel.config(bg=color["lavender"])
        topFrame.config(bg=color["lavender"])
        root.config(bg="lavender")

        # Turning button OFF:
        btnState = False
    else:
        # Make root dim:
        brandLabel.config(bg=color["nero"], fg="#5F5A33")
        homeLabel.config(bg=color["nero"])
        topFrame.config(bg=color["nero"])
        root.config(bg=color["nero"])

        # Created animated Navbar opening:
        for x in range(-300, 0):
            navRoot.place(x=x, y=0)
            topFrame.update()

        # Turning button ON:
        btnState = True

# Function to open main.py
def open_main_py():
    subprocess.Popen(["python", "mainT.py"])  # Run main.py using subprocess

# Placeholder function for Detection Faciale
def detection_faciale():
    subprocess.Popen(["python", "main.py"])  # Run mainT.py using subprocess

# Placeholder function for Contact Us
def contact_us():
    subprocess.Popen(["python", "contactUs.py"])  # Run contactUs.py using subprocess

# Top Navigation bar:
topFrame = tk.Frame(root, bg=color["lavender"])
topFrame.place(x=0, y=0, relwidth=1)

# Header label text:
homeLabel = tk.Label(topFrame, text="Gestion des Employés avec précision et élégance", font="Bahnschrift 15", bg=color["lavender"], fg="silver", height=2)
homeLabel.pack(side="right")

# Main label text:
brandLabel = tk.Label(root, text="FaceSmart - Gestion des Employés", font="System 30", bg="lavender", fg=color["green"])
brandLabel.place(x=20, y=250)

# Navbar button:
navbarBtn = tk.Button(topFrame, image=navIcon, bg=color["lavender"], activebackground=color["lavender"], bd=0, padx=20, command=switch)
navbarBtn.place(x=10, y=10)

# Setting Navbar frame:
navRoot = tk.Frame(root, bg="lavender", height=1000, width=300)
navRoot.place(x=-300, y=0)
tk.Label(navRoot, font="Bahnschrift 15", bg=color["lavender"], fg="black", height=2, width=300, padx=20).place(x=0, y=0)

# Set y-coordinate of Navbar widgets:
y = 80
# Option in the navbar:
options = ["Gestion des Employés", "Detection Faciale", "Contact Us"]
# Navbar Option Buttons:
for i in range(3):
    if options[i] == "Gestion des Employés":
        # Open main.py when "Gestion des Employés" is clicked
        tk.Button(navRoot, text=options[i], font="BahnschriftLight 15", bg=color["black"], fg=color["white"], activebackground=color["black"], activeforeground=color["white"], bd=0, width=20, command=open_main_py).place(x=25, y=y)
    elif options[i] == "Detection Faciale":
        tk.Button(navRoot, text=options[i], font="BahnschriftLight 15", bg=color["black"], fg=color["white"], activebackground=color["black"], activeforeground=color["white"], bd=0, width=20, command=detection_faciale).place(x=25, y=y)
    else:
        tk.Button(navRoot, text=options[i], font="BahnschriftLight 15", bg=color["black"], fg=color["white"], activebackground=color["black"], activeforeground=color["white"], bd=0, width=20, command=contact_us).place(x=25, y=y)
    y += 40

# Navbar Close Button:
closeBtn = tk.Button(navRoot, image=closeIcon, bg=color["lavender"], activebackground=color["lavender"], bd=0, command=switch)
closeBtn.place(x=250, y=10)

# Adding a frame in the middle of the page:
middleFrame = tk.Frame(root, bg="lavender", width=300, height=200)
middleFrame.place(relx=0.5, rely=0.5, anchor="center")

# Adding text inside the frame:
text_label = tk.Label(middleFrame, text="Bienvenue à FaceSmart - Gérez vos employés avec précision et élégance", font="System 20", bg="lavender", fg=color["green"])
text_label.pack()

# Window in mainloop:
root.mainloop()
