import tkinter as tk
from PIL import Image, ImageTk, ImageFilter
import os

# Function to quit the application
def quit_app():
    root.destroy()

# Function to explore something
def explore_action():
    root.destroy()  # Close the current window
    os.system("python pagee2.py")  # Open page2.py

# Function to return to intro.py page
def back_to_intro():
    os.system("python intro.py")

# Create a Tkinter window
root = tk.Tk()
root.title("FaceSmart")

# Load the background image
image = Image.open("i1.jpg")
photo = ImageTk.PhotoImage(image)

# Add a label for the background image
label_image = tk.Label(root, image=photo)
label_image.place(relx=0, rely=0, relwidth=1, relheight=1)

# Add a styled title at the top of the window
title = tk.Label(root, text="Face Smart", font=("Helvetica", 30, "bold"), bg="#2c3e50", fg="white", padx=20, pady=10)
title.pack(side="top", fill="x")

# Create a frame for the text
text_frame = tk.Frame(root, bg="#ecf0f1", padx=20, pady=20)
text_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

# Apply a Gaussian blur effect to the background
image_blurred = image.filter(ImageFilter.GaussianBlur(radius=10))
photo_blurred = ImageTk.PhotoImage(image_blurred)
label_blurred_background = tk.Label(text_frame, image=photo_blurred)
label_blurred_background.place(x=0, y=0, relwidth=1, relheight=1)

# Add the text to the frame
text = """FaceSmart révolutionne la gestion des ressources humaines en combinant la puissance de la reconnaissance faciale avec d'autres fonctionnalités avancées pour offrir une solution complète et efficace. En automatisant les processus de suivi de la présence, de gestion des informations des employés et d'évaluation de la production, l'application permet aux entreprises de gagner du temps, d'optimiser leurs ressources et d'améliorer leur productivité globale."""
label_text = tk.Label(text_frame, text=text, font=("Arial", 14), justify="left", wraplength=800, bg="transparent", fg="#34495e")
label_text.pack()

# Create a frame for the buttons
button_frame = tk.Frame(root, bg="transparent")
button_frame.pack(pady=(0, 20), side="bottom", fill="x")

# Add a button to explore something
explore_button = tk.Button(button_frame, text="Explorer", command=explore_action, bg="#3498db", fg="white", padx=10, pady=5, font=("Arial", 12, "bold"), relief="flat")
explore_button.pack(side="left", padx=20, pady=10)

# Add a button to return to the intro.py page
back_button = tk.Button(button_frame, text="Back", command=back_to_intro, bg="#e74c3c", fg="white", padx=10, pady=5, font=("Arial", 12, "bold"), relief="flat")
back_button.pack(side="left", padx=20, pady=10)

# Add a button to quit the application
quit_button = tk.Button(button_frame, text="Quitter", command=quit_app, bg="#2ecc71", fg="white", padx=10, pady=5, font=("Arial", 12, "bold"), relief="flat")
quit_button.pack(side="right", padx=20, pady=10)

# Start the main loop of the application
root.mainloop()
