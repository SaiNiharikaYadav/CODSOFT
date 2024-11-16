import tkinter as tk
from tkinter import messagebox

# Create a dictionary to store contacts where key is contact name and value is a dictionary of contact details
contacts = {}

# Function to add a contact
def add_contact():
    name = name_entry.get()
    phone = phone_entry.get()
    email = email_entry.get()
    address = address_entry.get()

    if name and phone:  # Ensure that name and phone are provided
        contacts[name] = {
            'Phone': phone,
            'Email': email,
            'Address': address
        }
        messagebox.showinfo("Success", f"Contact '{name}' added successfully!")
        clear_fields()
        update_contact_list()
    else:
        messagebox.showwarning("Input Error", "Please provide both name and phone number!")

# Function to update the contact list display
def update_contact_list():
    contact_list.delete(0, tk.END)  # Clear the listbox
    for name, details in contacts.items():
        contact_list.insert(tk.END, f"{name} - {details['Phone']}")

# Function to search a contact by name or phone number
def search_contact():
    query = search_entry.get().lower()
    contact_list.delete(0, tk.END)
    for name, details in contacts.items():
        if query in name.lower() or query in details['Phone']:
            contact_list.insert(tk.END, f"{name} - {details['Phone']}")

# Function to update contact details
def update_contact():
    selected = contact_list.curselection()
    if selected:
        selected_name = contact_list.get(selected[0]).split(' - ')[0]
        name = name_entry.get()
        phone = phone_entry.get()
        email = email_entry.get()
        address = address_entry.get()

        if name and phone:  # Ensure name and phone are provided
            contacts[selected_name] = {
                'Phone': phone,
                'Email': email,
                'Address': address
            }
            messagebox.showinfo("Success", f"Contact '{selected_name}' updated successfully!")
            clear_fields()
            update_contact_list()
        else:
            messagebox.showwarning("Input Error", "Please provide both name and phone number!")
    else:
        messagebox.showwarning("Selection Error", "Please select a contact to update!")

# Function to delete a contact
def delete_contact():
    selected = contact_list.curselection()
    if selected:
        selected_name = contact_list.get(selected[0]).split(' - ')[0]
        del contacts[selected_name]
        messagebox.showinfo("Success", f"Contact '{selected_name}' deleted successfully!")
        update_contact_list()
    else:
        messagebox.showwarning("Selection Error", "Please select a contact to delete!")

# Function to clear the input fields
def clear_fields():
    name_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    address_entry.delete(0, tk.END)
    search_entry.delete(0, tk.END)

# Initialize the main window
root = tk.Tk()
root.title("Contact Manager")
root.geometry("600x600")

# Labels for contact details
tk.Label(root, text="Name:").pack(pady=5)
name_entry = tk.Entry(root, width=50)
name_entry.pack(pady=5)

tk.Label(root, text="Phone:").pack(pady=5)
phone_entry = tk.Entry(root, width=50)
phone_entry.pack(pady=5)

tk.Label(root, text="Email:").pack(pady=5)
email_entry = tk.Entry(root, width=50)
email_entry.pack(pady=5)

tk.Label(root, text="Address:").pack(pady=5)
address_entry = tk.Entry(root, width=50)
address_entry.pack(pady=5)

# Buttons for contact management
tk.Button(root, text="Add Contact", width=20, command=add_contact).pack(pady=5)
tk.Button(root, text="Update Contact", width=20, command=update_contact).pack(pady=5)
tk.Button(root, text="Delete Contact", width=20, command=delete_contact).pack(pady=5)

# Search feature
tk.Label(root, text="Search by Name or Phone:").pack(pady=5)
search_entry = tk.Entry(root, width=50)
search_entry.pack(pady=5)
tk.Button(root, text="Search", width=20, command=search_contact).pack(pady=5)

# Contact list display
contact_list_frame = tk.Frame(root)
contact_list_frame.pack(pady=10)

tk.Label(contact_list_frame, text="Contact List:", font=("Helvetica", 14)).pack(pady=5)
contact_list = tk.Listbox(contact_list_frame, width=50, height=10)
contact_list.pack()

# Refresh the contact list
update_contact_list()

# Run the Tkinter event loop
root.mainloop()
