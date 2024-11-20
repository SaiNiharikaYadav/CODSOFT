import random
import string
import tkinter as tk
from tkinter import messagebox

# Function to generate the password based on user input
def generate_password(length, strength, include_numbers, include_symbols):
  # Define character sets
  letters = string.ascii_letters  # a-zA-Z
  digits = string.digits if include_numbers else ''  # Optional inclusion of digits
  punctuation = string.punctuation if include_symbols else ''  # Optional inclusion of symbols

  # Base character set based on strength
  if strength == 'Strong':
    characters = letters + digits + punctuation  # Full set for strong passwords
  elif strength == 'Average':
    characters = letters + digits  # Letters and numbers for average passwords
  else:  # Weak password (just letters)
    characters = string.ascii_lowercase  # Just lowercase letters

  # Ensure the character set is not empty
  if not characters:
    characters = letters  # Default to letters only if no other option is selected

  # Generate a random password
  password = ''.join(random.choice(characters) for _ in range(length))
  return password

# Function to handle the button click event
def on_generate_button_click():
  try:
    # Get user input from the GUI
    length = int(entry_length.get())
    strength = strength_var.get()  # Get the selected strength option
    include_numbers = var_numbers.get()  # Check if numbers should be included
    include_symbols = var_symbols.get()  # Check if symbols should be included

    # Generate and display the password
    password = generate_password(length, strength, include_numbers, include_symbols)
    text_password.delete('1.0', tk.END)  # Clear any previous password
    text_password.insert(tk.END, password)
  except ValueError:
    messagebox.showerror("Invalid Input", "Please enter a valid number for password length.")

# Create the main window
root = tk.Tk()
root.title("Password Generator")

# Create 1  and place widgets in the window
label_length = tk.Label(root, text="Enter Password Length:")
label_length.pack(pady=5)

entry_length = tk.Entry(root)
entry_length.pack(pady=5)

# Radio buttons for selecting password strength
label_strength = tk.Label(root, text="Select Password Strength:")
label_strength.pack(pady=5)

strength_var = tk.StringVar(value="Strong")  # Default value for radio buttons

radio_strong = tk.Radiobutton(root, text="Strong", variable=strength_var, value="Strong")
radio_strong.pack()

radio_average = tk.Radiobutton(root, text="Average", variable=strength_var, value="Average")
radio_average.pack()

radio_weak = tk.Radiobutton(root, text="Weak", variable=strength_var, value="Weak")
radio_weak.pack()

# Checkbutton for including numbers
var_numbers = tk.BooleanVar()
check_numbers = tk.Checkbutton(root, text="Include Numbers", variable=var_numbers)
check_numbers.pack(pady=5)

# **Fix: Define and initialize var_symbols**
var_symbols = tk.BooleanVar()  # Create a BooleanVar for symbols
check_symbols = tk.Checkbutton(root, text="Include Symbols", variable=var_symbols)
check_symbols.pack(pady=5)

# Create a button to generate the password
button_generate = tk.Button(root, text="Generate Password", command=on_generate_button_click)
button_generate.pack(pady=10)

# Text widget to display the generated password (bigger box)
label_password = tk.Label(root, text="Generated Password:")
label_password.pack(pady=5)

text_password = tk.Text(root, height=5, width=50)  # Bigger text box
text_password.pack(pady=5)

# Run the Tkinter event loop
root.mainloop()