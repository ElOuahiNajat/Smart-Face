import cv2
import tkinter as tk
from PIL import Image, ImageTk
import subprocess

# Function to update video frame
def update_frame():
    ret, frame = cap.read()
    if ret:
        # Convert the frame from BGR to RGB format
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        # Convert the frame to PIL format
        img = Image.fromarray(frame)
        # Convert PIL image to Tkinter PhotoImage
        imgtk = ImageTk.PhotoImage(image=img)
        # Update the label with the new image
        label.imgtk = imgtk
        label.config(image=imgtk)
    # Call update_frame after 15 milliseconds
    label.after(15, update_frame)

# Function to handle "Get Started" button click
def get_started():
    # Launch page1.py using subprocess
    subprocess.Popen(["python", "loginPage.py"])

# Create Tkinter window
root = tk.Tk()
root.title("Video Player")

# Open video file
cap = cv2.VideoCapture("video.mp4")

# Create label to display video
label = tk.Label(root)
label.pack()

# Call update_frame to start displaying video
update_frame()

# Create "Get Started" button
button = tk.Button(root, text="Get Started", command=get_started, font=("Helvetica", 16), bg="#3498db", fg="white", padx=20, pady=10)
button.place(relx=0.5, rely=0.5, anchor=tk.CENTER)  # Position the button in the center of the window

# Run the Tkinter event loop
root.mainloop()

# Release the video capture object and close the OpenCV window
cap.release()
cv2.destroyAllWindows()
