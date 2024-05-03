from tkinter import *
from tkinter import ttk
from tkinter import messagebox, filedialog, simpledialog
from db import Database
from PIL import Image, ImageTk
import subprocess

# Initialize the database
db = Database(host="localhost", user="root", password="", database="face_smart")

# Main window configuration
root = Tk()
root.title('Employee Management System')
root.geometry('1440x615+0+0')  # Increased width to accommodate the image
root.resizable(True, True)
root.configure(bg='white')  # Change background color to white

def go_back():
    subprocess.Popen(["python", "menubar.py"])

# Create menubar
menubar = Menu(root)
root.config(menu=menubar)

# Create a menu item for navigating back
file_menu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Back", command=go_back)

# Define variables to store employee information
Nom = StringVar()
Performancre = StringVar()
Poste = StringVar()
Gender = StringVar()
Email = StringVar()
Department = StringVar()
IMAGE_path = StringVar()  # Updated variable name

def upload_IMAGE():  # Updated function name
    path = filedialog.askopenfilename()
    if path:
        IMAGE_path.set(path)
        load_IMAGE()  # Call load_IMAGE when an image is uploaded

# Function to load and display the image
def load_IMAGE():  # Updated function name
    global img_label
    img_path = IMAGE_path.get()  # Updated variable name
    if img_path:
        img = Image.open(img_path)
        img = img.resize((100, 100), Image.ANTIALIAS)  # Resize image as needed
        img = ImageTk.PhotoImage(img)
        if img_label:
            img_label.config(image=img)
            img_label.image = img  # Keep a reference to the image
        else:
            img_label = Label(root, image=img, bg='white')
            img_label.place(x=1180, y=290)  # Adjust position as needed

# Call load_IMAGE initially to display any existing image path
load_IMAGE()  # Updated function name

entries_frame = Frame(root, bg='white')
entries_frame.place(x=1, y=1, width=360, height=470)
title = Label(entries_frame, text='Employee Company', font=('Calibri', 18, 'bold'), bg='white', fg='black')
title.place(x=10, y=1)

lblNom = Label(entries_frame, text="Nom", font=('Calibri', 16), bg='white', fg='black')
lblNom.place(x=10, y=50)
txtNom = Entry(entries_frame, textvariable=Nom, width=20, font=('Calibri', 16))
txtNom.place(x=120, y=50)

lblPerformancre = Label(entries_frame, text="Performancre", font=('Calibri', 16), bg='white', fg='black')
lblPerformancre.place(x=10, y=90)
txtPerformancre = Entry(entries_frame, textvariable=Performancre, width=20, font=('Calibri', 16))
txtPerformancre.place(x=120, y=90)

lblPoste = Label(entries_frame, text="Poste", font=('Calibri', 16), bg='white', fg='black')
lblPoste.place(x=10, y=130)
txtPoste = Entry(entries_frame, textvariable=Poste, width=20, font=('Calibri', 16))
txtPoste.place(x=120, y=130)

lblGender = Label(entries_frame, text="Gender", font=('Calibri', 16), bg='white', fg='black')
lblGender.place(x=10, y=170)
comboGender = ttk.Combobox(entries_frame, textvariable=Gender, width=18, font=('Calibri', 16))
comboGender['values'] = ("Male", "Female")
comboGender.place(x=120, y=170)
comboGender.config(state="readonly")

lblEmail = Label(entries_frame, text="Email", font=('Calibri', 16), bg='white', fg='black')
lblEmail.place(x=10, y=210)
txtEmail = Entry(entries_frame, textvariable=Email, width=20, font=('Calibri', 16))
txtEmail.place(x=120, y=210)

# Add label for image
lblIMAGE = Label(entries_frame, text="IMAGE", font=('Calibri', 16), bg='white', fg='black')  # Updated label name
lblIMAGE.place(x=10, y=250)  # Changed position for the "IMAGE" label
btnUploadIMAGE = Button(entries_frame, text='Upload IMAGE', bg='white', bd=1, relief=SOLID, cursor='hand2', command=upload_IMAGE)  # Updated button label
btnUploadIMAGE.place(x=120, y=250)  # Changed position for the "Upload IMAGE" button

lblDepartment = Label(entries_frame, text="Department", font=('Calibri', 16), bg='white', fg='black')
lblDepartment.place(x=10, y=290)  # Changed position for the "Department" label
txtDepartment = Entry(entries_frame, textvariable=Department, width=20, font=('Calibri', 16))
txtDepartment.place(x=120, y=290)  # Changed position for the "Department" entry widget

def hide():
    root.geometry("360x515+0+0")

def show():
    root.geometry('1440x615+0+0')

btnhide = Button(entries_frame, text='HIDE', bg='white', bd=1, relief=SOLID, cursor='hand2', command=hide)
btnhide.place(x=270, y=10)
btnshow = Button(entries_frame, text='SHOW', bg='white', bd=1, relief=SOLID, cursor='hand2', command=show)
btnshow.place(x=310, y=10)

def getData(event):
    selected_row = tv.focus()
    data = tv.item(selected_row)
    if data:
        global row
        row = data["values"]
        Nom.set(row[1])
        Performancre.set(row[2])
        Poste.set(row[3])
        Email.set(row[4])
        Gender.set(row[5])
        Department.set(row[6])
        IMAGE_path.set(row[7])  # Set the IMAGE path in the entry field
        load_IMAGE()  # Call load_IMAGE to display the IMAGE
    else:
        clear_fields()

def displayAll():
    tv.delete(*tv.get_children())
    for row in db.fetch():
        # Add the IMAGE column to the data
        row_with_IMAGE = list(row)
        row_with_IMAGE.append("")  # Placeholder for the IMAGE
        tv.insert("", END, values=row_with_IMAGE)

def search():
    selected_value = simpledialog.askstring("Search Criteria", "Enter search criteria (Nom, Performancre, Poste, Email, Gender, Department):")
    if not selected_value:
        return  # User canceled the dialog

    searched_value = simpledialog.askstring("Search Value", f"Enter value to search for in {selected_value}:")
    if not searched_value:
        return  # User canceled the dialog

    result = db.search(selected_value.lower(), searched_value)
    if not result:
        messagebox.showinfo("Search Result", "No matching records found.")
    else:
        tv.delete(*tv.get_children())
        for row in result:
            # Add the IMAGE column to the data
            row_with_IMAGE = list(row)
            row_with_IMAGE.append("")  # Placeholder for the IMAGE
            tv.insert("", END, values=row_with_IMAGE)

def delete():
    if not tv.selection():
        messagebox.showwarning("Warning", "Please select a record.")
        return
    response = messagebox.askyesno("Delete record", "Do you want to delete this record?")
    if response:
        selected_item = tv.selection()[0]
        selected_id = tv.item(selected_item)['values'][0]
        db.remove(selected_id)
        displayAll()
        clear_fields()

def clear_fields():
    Nom.set("")
    Performancre.set("")
    Poste.set("")
    Gender.set("")
    Email.set("")
    Department.set("")
    IMAGE_path.set("")  # Clear the IMAGE path field

def is_valid_email(email):
    return re.match(r"[^@]+@[^@]+\.[^@]+", email) and email.endswith("@gmail.com")

def add_employee():
    try:
        if txtNom.get() == "" or txtPerformancre.get() == "" or txtPoste.get() == "" or txtEmail.get() == "" or comboGender.get() == "" or txtDepartment.get() == "":
            messagebox.showerror("Error", "Please fill all the entries")
            return
        if not is_valid_email(txtEmail.get()):
            messagebox.showerror("Error", "Please enter a valid email ending with '@gmail.com'")
            return
        db.insert(
            txtNom.get(),
            txtPerformancre.get(),
            txtPoste.get(),
            txtEmail.get(),
            comboGender.get(),
            txtDepartment.get(),
            IMAGE_path.get()  # Get the IMAGE path from the entry field
        )
        messagebox.showinfo("Success", "Added new employee")
        displayAll()
        clear_fields()
    except Exception as e:
        messagebox.showerror("Error", str(e))
        clear_fields()
        displayAll()

def update_employee():
    try:
        if not tv.selection():
            messagebox.showwarning("Warning", "Please select a record.")
            return
        selected_item = tv.selection()[0]
        selected_id = tv.item(selected_item)['values'][0]
        if not is_valid_email(txtEmail.get()):
            messagebox.showerror("Error", "Please enter a valid email ending with '@gmail.com'")
            return
        db.update(
            selected_id,
            txtNom.get(),
            txtPerformancre.get(),
            txtPoste.get(),
            txtEmail.get(),
            comboGender.get(),
            txtDepartment.get(),
            IMAGE_path.get()  # Get the IMAGE path from the entry field
        )
        messagebox.showinfo("Success", "Employee details updated")
        displayAll()
    except Exception as e:
        messagebox.showerror("Error", str(e))
        clear_fields()
        displayAll()

def show_all():
    displayAll()

btnShowAll = Button(root, text='Show All', width=14, height=1, font=('Calibri', 16), fg='white', bg='#2ecc71', bd=0, command=show_all)
btnShowAll.place(x=150, y=520)

btn_frame = Frame(entries_frame, bg='white', bd=1, relief=SOLID)
btn_frame.place(x=10, y=380, width=335, height=220)

btnAdd = Button(btn_frame, text='Add Details', width=14, height=1, font=('Calibri', 16), fg='white', bg='#16a085', bd=0, command=add_employee)
btnAdd.grid(row=0, column=0, padx=5, pady=5)

btnEdit = Button(btn_frame, text='Update Details', width=14, height=1, font=('Calibri', 16), fg='white', bg='#2980b9', bd=0, command=update_employee)
btnEdit.grid(row=0, column=1, padx=5, pady=5)

btnDelete = Button(btn_frame, text='Delete Details', width=14, height=1, font=('Calibri', 16), fg='white', bg='#c0392b', bd=0, command=delete)
btnDelete.grid(row=1, column=0, padx=5, pady=5)

btnClear = Button(btn_frame, text='Clear Details', width=14, height=1, font=('Calibri', 16), fg='white', bg='#f39c12', bd=0, command=clear_fields)
btnClear.grid(row=1, column=1, padx=5, pady=5)

# Search button
btnSearch = Button(root, text='Search', width=14, height=1, font=('Calibri', 16), fg='white', bg='#34495e', bd=0, command=search)
btnSearch.place(x=10, y=520)

tree_frame = Frame(root, bg='white')
tree_frame.place(x=365, y=1, width=875, height=610)
style = ttk.Style()
style.configure("mystyle.Treeview", font=('Calibri', 13), rowheight=50)
style.configure("mystyle.Treeview.Heading", font=('Calibri', 13))

tv = ttk.Treeview(tree_frame, columns=(1, 2, 3, 4, 5, 6, 7, 8), style="mystyle.Treeview")
tv.heading("1", text="ID")
tv.column("1", width="40")
tv.heading("2", text="Nom")
tv.column("2", width="140")
tv.heading("3", text="Performancre")
tv.column("3", width="100")
tv.heading("4", text="Poste")
tv.column("4", width="120")
tv.heading("5", text="Email")
tv.column("5", width="150")
tv.heading("6", text="Gender")
tv.column("6", width="90")
tv.heading("7", text="Department")
tv.column("7", width="120")
tv.heading("8", text="IMAGE")  # Updated column name
tv.column("8", width="120")  # Adjust the width as needed

tv['show'] = 'headings'
tv.place(x=1, y=1, height=610, width=875)

displayAll()

tv.bind('<ButtonRelease-1>', getData)

root.mainloop()
