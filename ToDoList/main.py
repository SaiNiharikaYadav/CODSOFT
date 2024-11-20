import tkinter as tk
from tkinter import messagebox, ttk
from tkcalendar import Calendar
import json
from datetime import datetime, timedelta
import calendar

class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("🌟 To-Do List 🌟")
        self.root.geometry("800x800")  # Adjusted size for extra widgets
        self.root.configure(bg="white")

        # Load tasks from JSON
        self.tasks = self.load_tasks()

        # Title Label
        self.title_label = tk.Label(root, text="🌸 My To-Do List 🌸", font=("Arial", 16, "bold"), bg="white", fg="skyblue")
        self.title_label.pack(pady=10)

        # Task Entry
        self.task_entry = tk.Entry(root, width=40, bg="white", fg="black", highlightthickness=1, relief="solid")
        self.task_entry.pack(pady=10)

        # Calendar for Due Date Selection
        self.due_date_calendar = Calendar(root, date_pattern="yyyy-mm-dd", background="#D3D3D3", foreground="black")
        self.due_date_calendar.pack(pady=10)

        # Time Dropdown for task time (Optional)
        self.time_var = tk.StringVar(value="Select Time (Optional)")  # Default value set to "Select Time (Optional)"
        self.time_menu = ttk.Combobox(root, textvariable=self.time_var, values=["Select Time (Optional)"] + [f"{hour:02d}:00" for hour in range(24)], state="readonly")
        self.time_menu.pack(pady=10)

        # Repeat Task Dropdown
        self.repeat_var = tk.StringVar(value="No Repeat")
        self.repeat_menu = ttk.Combobox(root, textvariable=self.repeat_var, values=["No Repeat", "Hourly", "Daily", "Monthly", "Yearly"], state="readonly")
        self.repeat_menu.pack(pady=10)

        # Priority Dropdown
        self.priority_var = tk.StringVar(value="High")  # Default to "High"
        self.priority_menu = ttk.Combobox(root, textvariable=self.priority_var, values=["High", "Average", "Low"], state="readonly")
        self.priority_menu.pack(pady=10)

        # Buttons to manage tasks
        button_frame = tk.Frame(root, bg="white")
        button_frame.pack(pady=10)

        self.add_button = tk.Button(button_frame, text="➕ Add Task", command=self.add_task, bg="skyblue", fg="black", font=("Arial", 12))
        self.add_button.pack(side=tk.LEFT, padx=10)

        self.update_button = tk.Button(button_frame, text="✏️ Update Task", command=self.update_task, bg="skyblue", fg="black", font=("Arial", 12))
        self.update_button.pack(side=tk.LEFT, padx=10)

        self.delete_button = tk.Button(button_frame, text="❌ Delete Task", command=self.delete_task, bg="skyblue", fg="black", font=("Arial", 12))
        self.delete_button.pack(side=tk.LEFT, padx=10)

        self.done_button = tk.Button(button_frame, text="✅ Mark as Done", command=self.mark_done, bg="skyblue", fg="black", font=("Arial", 12))
        self.done_button.pack(side=tk.LEFT, padx=10)

        # Listbox for tasks (White background)
        self.task_listbox = tk.Listbox(root, width=50, height=15, bg="white", fg="black", font=("Arial", 12), selectmode=tk.SINGLE)
        self.task_listbox.pack(pady=10)

        self.update_task_listbox()

    # Load tasks from a JSON file
    def load_tasks(self, filename="tasks.json"):
        try:
            with open(filename, "r") as f:
                tasks = json.load(f)
                # Ensure all tasks have a priority key, assigning default "Low" if missing
                for task in tasks:
                    if "priority" not in task:
                        task["priority"] = "Low"
                    if "due_date" not in task:
                        task["due_date"] = "N/A"  # Default to "N/A" if no due date
                return tasks
        except FileNotFoundError:
            return []

    # Save tasks to a JSON file
    def save_tasks(self, filename="tasks.json"):
        with open(filename, "w") as f:
            json.dump(self.tasks, f)

    # Update the Listbox with current tasks
    def update_task_listbox(self):
        self.task_listbox.delete(0, tk.END)

        # Sorting tasks based on priority
        priority_order = {"High": 0, "Average": 1, "Low": 2}
        sorted_tasks = sorted(self.tasks, key=lambda x: priority_order.get(x["priority"], 3))

        for idx, task in enumerate(sorted_tasks):
            status = "✅" if task["done"] else "🕒"  # Mark as Done icon is only visible once task is marked done
            due_date = task["due_date"] if task["due_date"] != "N/A" else "No Due Date"
            task_display = f"{task['task']} {status} - {task['priority']} Priority - Due: {due_date}"  # Display due date
            self.task_listbox.insert(tk.END, f"{task_display}")

    # Add a new task
    def add_task(self):
        task_text = self.task_entry.get()
        task_due_date = self.due_date_calendar.get_date()
        task_time = self.time_var.get() if self.time_var.get() != "Select Time (Optional)" else None
        task_repeat = self.repeat_var.get()
        task_priority = self.priority_var.get()

        if task_text.strip():
            # Handle repetitive tasks with the correct due date
            if task_repeat != "No Repeat":
                task_due_date = self.calculate_repeat_due_date(task_due_date, task_repeat)

            self.tasks.append({
                "task": task_text, 
                "done": False, 
                "due_date": task_due_date,  
                "time": task_time,  
                "repeat": task_repeat, 
                "priority": task_priority  # Save the priority
            })
            self.task_entry.delete(0, tk.END)
            self.save_tasks()
            self.update_task_listbox()
        else:
            messagebox.showwarning("Input Error", "Please enter a task.")

    # Calculate due date based on repeat option
    def calculate_repeat_due_date(self, due_date, repeat_type):
        current_date = datetime.strptime(due_date, "%Y-%m-%d")

        if repeat_type == "Hourly":
            due_date = current_date + timedelta(hours=1)
        elif repeat_type == "Daily":
            due_date = current_date + timedelta(days=1)
        elif repeat_type == "Monthly":
            month = current_date.month % 12 + 1
            year = current_date.year if month > current_date.month else current_date.year + 1
            day = min(current_date.day, calendar.monthrange(year, month)[1])
            due_date = current_date.replace(year=year, month=month, day=day)
        elif repeat_type == "Yearly":
            due_date = current_date.replace(year=current_date.year + 1)
        
        return due_date.strftime("%Y-%m-%d")

    # Update an existing task
    def update_task(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            idx = selected_task_index[0]
            task_text = self.task_entry.get()
            task_due_date = self.due_date_calendar.get_date()
            task_time = self.time_var.get() if self.time_var.get() != "Select Time (Optional)" else None
            task_repeat = self.repeat_var.get()
            task_priority = self.priority_var.get()

            if task_text.strip():
                # Handle repetitive tasks with the correct due date
                if task_repeat != "No Repeat":
                    task_due_date = self.calculate_repeat_due_date(task_due_date, task_repeat)

                self.tasks[idx] = {
                    "task": task_text,
                    "done": self.tasks[idx]["done"],
                    "due_date": task_due_date,
                    "time": task_time,
                    "repeat": task_repeat,
                    "priority": task_priority  # Update the priority
                }
                self.task_entry.delete(0, tk.END)
                self.save_tasks()
                self.update_task_listbox()
            else:
                messagebox.showwarning("Input Error", "Please enter valid task details.")
        else:
            messagebox.showwarning("Selection Error", "No task selected.")

    # Delete a selected task
    def delete_task(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            idx = selected_task_index[0]
            del self.tasks[idx]
            self.save_tasks()
            self.update_task_listbox()
        else:
            messagebox.showwarning("Selection Error", "No task selected.")

    # Mark a task as done
    def mark_done(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            idx = selected_task_index[0]
            self.tasks[idx]["done"] = True
            self.save_tasks()
            self.update_task_listbox()
        else:
            messagebox.showwarning("Selection Error", "No task selected.")

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()
