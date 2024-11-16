import tkinter as tk
from tkinter import messagebox
import cmath
import math

# Function to handle button press events
def button_click(value):
    current_text = entry_display.get()
    entry_display.delete(0, tk.END)  # Clear current entry
    entry_display.insert(tk.END, current_text + str(value))  # Append the button value

# Function to perform calculation
def calculate():
    try:
        expression = entry_display.get()

        # Check if the expression contains 'j' (for complex numbers)
        if 'j' in expression or 'J' in expression:
            result = complex(expression)
        else:
            result = eval(expression)  # Evaluate the mathematical expression (safe for numbers)
        
        # Display the result in the entry box
        entry_display.delete(0, tk.END)
        entry_display.insert(tk.END, str(result))

        # Store the calculation in history
        history_list.insert(tk.END, f"{expression} = {result}")

    except ZeroDivisionError:
        messagebox.showerror("Error", "Division by zero is not allowed!", icon='warning')
    except Exception as e:
        messagebox.showerror("Error", "Invalid input or operation!", icon='warning')

# Function to clear the display
def clear_display():
    entry_display.delete(0, tk.END)

# Function to delete the last character
def delete_last():
    current_text = entry_display.get()
    entry_display.delete(len(current_text) - 1, tk.END)

# Function to clear the history
def clear_history():
    history_list.delete(0, tk.END)

# Function to clear both display and history
def clear_all():
    clear_display()
    clear_history()

# Function to create small buttons with black and white background
def create_button(parent, text, row, col, command=None):
    button = tk.Button(parent, text=text, font=("Arial", 10), command=command, width=4, height=2, relief="solid", 
                       bg="white", fg="black", borderwidth=2, padx=10, pady=10, 
                       bd=1, highlightthickness=0, activebackground="gray", 
                       activeforeground="white")
    button.grid(row=row, column=col, padx=5, pady=5)
    return button

# Create the main window
root = tk.Tk()
root.title("Interactive Mobile Calculator")

# Create the display text entry box (larger size)
entry_display = tk.Entry(root, width=30, font=("Arial", 15), borderwidth=1, relief="solid", justify="right", bg="white", fg="black")
entry_display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Create the history listbox
history_label = tk.Label(root, text="History", font=("Arial", 12), bg="white", fg="black")
history_label.grid(row=0, column=4)
history_list = tk.Listbox(root, height=20, width=20, font=("Arial", 10), bg="white", fg="black")
history_list.grid(row=1, column=4, rowspan=5, padx=10, pady=10)

# Button layout for the calculator
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3),
    ('Clear', 5, 0), ('Delete', 5, 1), ('√', 5, 2), ('^', 5, 3),
    ('π', 6, 0), ('e', 6, 1), ('Conj', 6, 2), ('|z|', 6, 3),
    ('Clear All', 7, 0), ('(', 7, 1), (')', 7, 2)
]

# Add the small buttons with large font to the GUI
for (text, row, col) in buttons:
    if text == '=':
        create_button(root, text, row, col, command=calculate)
    elif text == 'Clear':
        create_button(root, text, row, col, command=clear_display)
    elif text == 'Delete':
        create_button(root, text, row, col, command=delete_last)
    elif text == '√':
        create_button(root, text, row, col, command=lambda: button_click('math.sqrt('))
    elif text == '^':
        create_button(root, text, row, col, command=lambda: button_click('**'))
    elif text == 'π':
        create_button(root, text, row, col, command=lambda: button_click(str(math.pi)))
    elif text == 'e':
        create_button(root, text, row, col, command=lambda: button_click(str(math.e)))
    elif text == 'Conj':
        create_button(root, text, row, col, command=lambda: button_click('.conjugate()'))
    elif text == '|z|':
        create_button(root, text, row, col, command=lambda: button_click('abs('))
    elif text == 'Clear All':
        create_button(root, text, row, col, command=clear_all)
    elif text == '(':
        create_button(root, text, row, col, command=lambda: button_click('('))
    elif text == ')':
        create_button(root, text, row, col, command=lambda: button_click(')'))
    else:
        create_button(root, text, row, col, command=lambda value=text: button_click(value))

# Start the main loop
root.mainloop()
