import tkinter as tk
from PIL import ImageTk, Image
import os

# Function for the employee button
def employee_action():
    print("Employee button clicked")

# Function for the manager button
def manager_action():
    print("Manager button clicked")

# Function for exploring something
def explorer():
    print("Exploring something...")

# Function to return to the intro page
def retour_intro():
    root.destroy()  # Ferme la fenêtre actuelle
    os.system("python page1.py")  # Ouvre la page1.py

# Create Tkinter window
root = tk.Tk()
root.title("Employee Management System")
root.geometry("500x300")  # Adjust the window size

# Load background image
image = Image.open("i2.jpg")
photo = ImageTk.PhotoImage(image)

# Create a canvas for the background image
canvas = tk.Canvas(root, width=500, height=300)  # Adjust the canvas size
canvas.pack(fill="both", expand=True)
canvas.create_image(0, 0, image=photo, anchor="nw")

# Create a frame to enclose the content
content_frame = tk.Frame(canvas, bg="white", bd=2, relief="groove")
content_frame.place(relx=0.5, rely=0.5, anchor="center")

# Create a label for title
title_label = tk.Label(content_frame, text="Let's Get Started!", font=("Helvetica", 24), bg="white", fg="#333")
title_label.pack(pady=(20, 10))  # Add a small space below

# Create a frame for buttons
button_frame = tk.Frame(content_frame, bg="white")
button_frame.pack()

# Create Employee button
employee_button = tk.Button(button_frame, text="Employee", font=("Helvetica", 14), bg="#3498db", fg="white", padx=10, pady=5, command=employee_action)
employee_button.pack(side="left", padx=10)

# Create Manager button
manager_button = tk.Button(button_frame, text="Manager", font=("Helvetica", 14), bg="#2ecc71", fg="white", padx=10, pady=5, command=manager_action)
manager_button.pack(side="left", padx=10)

# Run the Tkinter event loop
root.mainloop()
