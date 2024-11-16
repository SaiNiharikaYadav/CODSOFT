import tkinter as tk
from tkinter import messagebox
import json

class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")
        self.root.geometry("400x500")
        
        # Set a white background for the window
        self.root.configure(bg="white")
        
        # Tasks list
        self.tasks = self.load_tasks()
        
        # Title Label
        self.title_label = tk.Label(root, text="To-Do List", font=("Arial", 16), bg="white", fg="black")
        self.title_label.pack(pady=10)
        
        # Task Entry
        self.task_entry = tk.Entry(root, width=40, bg="white", fg="black", highlightthickness=1, relief="solid")
        self.task_entry.pack(pady=10)
        
        # Add Task Button (Sky Blue color)
        self.add_button = tk.Button(root, text="Add Task", command=self.add_task, bg="#87CEEB", fg="black", font=("Arial", 12))
        self.add_button.pack(pady=5)
        
        # Listbox for tasks (White background)
        self.task_listbox = tk.Listbox(root, width=50, height=15, bg="white", fg="black", selectmode=tk.SINGLE, font=("Arial", 12))
        self.task_listbox.pack(pady=10)
        self.update_task_listbox()
        
        # Buttons to manage tasks (Sky Blue color)
        button_frame = tk.Frame(root, bg="white")
        button_frame.pack(pady=10)
        
        self.done_button = tk.Button(button_frame, text="Mark as Done", command=self.mark_done, bg="#87CEEB", fg="black")
        self.done_button.pack(side=tk.LEFT, padx=20)
        
        self.delete_button = tk.Button(button_frame, text="Delete Task", command=self.delete_task, bg="#87CEEB", fg="black")
        self.delete_button.pack(side=tk.LEFT, padx=20)
    
    # Load tasks from a JSON file
    def load_tasks(self, filename="tasks.json"):
        try:
            with open(filename, "r") as f:
                return json.load(f)
        except FileNotFoundError:
            return []
    
    # Save tasks to a JSON file
    def save_tasks(self, filename="tasks.json"):
        with open(filename, "w") as f:
            json.dump(self.tasks, f)
    
    # Update the Listbox with current tasks
    def update_task_listbox(self):
        self.task_listbox.delete(0, tk.END)
        for idx, task in enumerate(self.tasks):
            status = "(Done)" if task["done"] else "(Pending)"
            self.task_listbox.insert(tk.END, f"{idx + 1}. {task['task']} {status}")
    
    # Add a new task
    def add_task(self):
        task_text = self.task_entry.get()
        if task_text.strip():
            self.tasks.append({"task": task_text, "done": False})
            self.update_task_listbox()
            self.task_entry.delete(0, tk.END)
            self.save_tasks()
        else:
            messagebox.showwarning("Input Error", "Task cannot be empty.")
    
    # Mark a task as done
    def mark_done(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            index = selected_task_index[0]
            self.tasks[index]["done"] = True
            self.update_task_listbox()
            self.save_tasks()
        else:
            messagebox.showwarning("Selection Error", "No task selected.")
    
    # Delete a selected task
    def delete_task(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            index = selected_task_index[0]
            del self.tasks[index]
            self.update_task_listbox()
            self.save_tasks()
        else:
            messagebox.showwarning("Selection Error", "No task selected.")

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()
