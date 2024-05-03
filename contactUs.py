import tkinter as tk
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from PIL import Image, ImageTk  # Import Image and ImageTk from PIL library

def submit_form():
    try:
        name = name_entry.get()
        email = email_entry.get()
        message = message_text.get("1.0", "end-1c")

        # Set up email server and credentials
        smtp_server = "smtp.example.com"  # Update with your SMTP server
        smtp_port = 587  # Update with your SMTP port
        sender_email = "your_email@example.com"  # Update with your email address
        password = "your_password"  # Update with your email password

        # Create email message
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = email
        msg['Subject'] = "Message from Contact Form"

        # Add message body
        body = f"Hello {name},\n\nThank you for contacting us.\n\nYour message:\n{message}"
        msg.attach(MIMEText(body, 'plain'))

        # Connect to SMTP server and send email
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(sender_email, password)
            server.send_message(msg)

        print("Email sent successfully!")
    except Exception as e:
        print("An error occurred while sending the email:", e)

root = tk.Tk()
root.title("Contact Form")

container = tk.Frame(root, bg="#f3f3f3", padx=20, pady=20)
container.pack(fill=tk.BOTH, expand=True)

left_frame = tk.Frame(container, bg="#fff", padx=20, pady=20)
left_frame.pack(side="left", fill=tk.BOTH, expand=True)

tk.Label(left_frame, text="Contact Us", font=("Arial", 20), bg="#fff", fg="#007BFF").pack(pady=10)

tk.Label(left_frame, text="Name:", font=("Arial", 12), bg="#fff").pack(pady=5)
name_entry = tk.Entry(left_frame, font=("Arial", 12))
name_entry.pack(pady=5)

tk.Label(left_frame, text="Email:", font=("Arial", 12), bg="#fff").pack(pady=5)
email_entry = tk.Entry(left_frame, font=("Arial", 12))
email_entry.pack(pady=5)

tk.Label(left_frame, text="Message:", font=("Arial", 12), bg="#fff").pack(pady=5)
message_text = tk.Text(left_frame, font=("Arial", 12), height=6)
message_text.pack(pady=5)

submit_button = tk.Button(left_frame, text="Submit", font=("Arial", 12), bg="#007BFF", fg="#fff", command=submit_form)
submit_button.pack(pady=10)

right_frame = tk.Frame(container, bg="black", padx=20, pady=20)
right_frame.pack(side="right", fill=tk.BOTH, expand=True)

contact_info_label = tk.Label(right_frame, text="Contact Information", font=("Arial", 20), fg="#fff", bg="black")
contact_info_label.pack(pady=(0, 10))

# Inserting bitmoji for location followed by a line break
contact_info = "📍\n \nLocation: 123 Main St, City, Country\n🏠\n \nAddress: 123 Main St, City, Country\n🌐\n \n Website: www.example.com\n\nFeel free to contact us for any inquiries or assistance."

contact_info_text = tk.Label(right_frame, text=contact_info, font=("Arial", 12), fg="#fff", bg="black", justify="center")
contact_info_text.pack(pady=10)

# Create a frame for the icons
icons_frame = tk.Frame(right_frame, bg="black")
icons_frame.pack(pady=10)

# Load and display LinkedIn icon
linkedin_image = Image.open("linkedin.png")  # Replace "linkedin.png" with your LinkedIn icon file path
linkedin_image = linkedin_image.resize((30, 30))
linkedin_icon = ImageTk.PhotoImage(linkedin_image)
linkedin_label = tk.Label(icons_frame, image=linkedin_icon, bg="black")
linkedin_label.image = linkedin_icon
linkedin_label.pack(side="left", padx=5)

# Load and display Instagram icon
instagram_image = Image.open("instagram.png")  # Replace "instagram.png" with your Instagram icon file path
instagram_image = instagram_image.resize((30, 30))
instagram_icon = ImageTk.PhotoImage(instagram_image)
instagram_label = tk.Label(icons_frame, image=instagram_icon, bg="black")
instagram_label.image = instagram_icon
instagram_label.pack(side="left", padx=5)

# Load and display Facebook icon
facebook_image = Image.open("facebook.png")  # Replace "facebook.png" with your Facebook icon file path
facebook_image = facebook_image.resize((30, 30))
facebook_icon = ImageTk.PhotoImage(facebook_image)
facebook_label = tk.Label(icons_frame, image=facebook_icon, bg="black")
facebook_label.image = facebook_icon
facebook_label.pack(side="left", padx=5)

# Load and display WhatsApp icon
whatsapp_image = Image.open("whatsapp.png")  # Replace "whatsapp.png" with your WhatsApp icon file path
whatsapp_image = whatsapp_image.resize((30, 30))
whatsapp_icon = ImageTk.PhotoImage(whatsapp_image)
whatsapp_label = tk.Label(icons_frame, image=whatsapp_icon, bg="black")
whatsapp_label.image = whatsapp_icon
whatsapp_label.pack(side="left", padx=5)

root.mainloop()
