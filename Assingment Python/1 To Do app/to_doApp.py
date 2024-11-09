import tkinter as tk
from tkinter import messagebox, simpledialog
import datetime

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List Application")
        
        self.tasks = []
        
        frame = tk.Frame(self.root)
        frame.pack(pady=10)

        self.task_listbox = tk.Listbox(frame, width=50, height=10, selectmode=tk.SINGLE)
        self.task_listbox.pack(side=tk.LEFT)

        # Scrollbar for listbox
        scrollbar = tk.Scrollbar(frame, orient=tk.VERTICAL, command=self.task_listbox.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.task_listbox.config(yscrollcommand=scrollbar.set)

        # Entry field to add new tasks
        self.task_entry = tk.Entry(self.root, width=52)
        self.task_entry.pack(pady=10)

        # Buttons to add, delete, and mark tasks as done
        self.add_button = tk.Button(self.root, text="Add Task", width=20, command=self.add_task)
        self.add_button.pack(pady=5)

        self.delete_button = tk.Button(self.root, text="Delete Task", width=20, command=self.delete_task)
        self.delete_button.pack(pady=5)

        self.complete_button = tk.Button(self.root, text="Mark as Completed", width=20, command=self.complete_task)
        self.complete_button.pack(pady=5)

        # Load tasks from file
        self.load_tasks()

    def add_task(self):
        task = self.task_entry.get()
        if task != "":
            # Ask user for a completion date
            due_date = simpledialog.askstring("Set Completion Date", "Enter due date for the task (YYYY-MM-DD):")
            if due_date:
                try:
                    # Convert due date string to datetime object
                    due_date = datetime.datetime.strptime(due_date, "%Y-%m-%d")
                    self.tasks.append({"task": task, "due_date": due_date, "completed": False})
                    self.update_task_list()
                    self.task_entry.delete(0, tk.END)
                except ValueError:
                    messagebox.showerror("Date Error", "Invalid date format. Please enter in YYYY-MM-DD format.")
            else:
                messagebox.showwarning("Input Error", "Please enter a valid completion date.")
        else:
            messagebox.showwarning("Input Error", "Please enter a task.")

    def delete_task(self):
        try:
            selected_task_index = self.task_listbox.curselection()[0]
            self.tasks.pop(selected_task_index)
            self.update_task_list()
        except IndexError:
            messagebox.showwarning("Selection Error", "Please select a task to delete.")

    def complete_task(self):
        try:
            selected_task_index = self.task_listbox.curselection()[0]
            task = self.tasks[selected_task_index]
            if not task['completed']:
                task['completed'] = True
                self.tasks[selected_task_index] = task
                self.update_task_list()
            else:
                messagebox.showinfo("Task Completed", "This task is already marked as completed.")
        except IndexError:
            messagebox.showwarning("Selection Error", "Please select a task to mark as completed.")

    def update_task_list(self):
        # Clear the listbox before updating
        self.task_listbox.delete(0, tk.END)

        # Add each task to the listbox with the due date and remaining time
        for task in self.tasks:
            task_description = task['task']
            due_date = task['due_date'].strftime("%Y-%m-%d")
            remaining_time = self.get_remaining_time(task['due_date'])
            completed_status = "(Completed)" if task['completed'] else f"Due: {due_date} - {remaining_time}"
            display_text = f"{task_description} - {completed_status}"
            self.task_listbox.insert(tk.END, display_text)

        # Save the tasks to a file after every update
        self.save_tasks()

    def get_remaining_time(self, due_date):
        # Calculate the remaining time in days
        now = datetime.datetime.now()
        remaining_time = due_date - now
        if remaining_time.days > 0:
            return f"{remaining_time.days} days left"
        elif remaining_time.days == 0:
            return "Today"
        else:
            return f"Overdue by {-remaining_time.days} days"

    def save_tasks(self):
        with open("tasks.txt", "w") as f:
            for task in self.tasks:
                task_str = f"{task['task']}|{task['due_date'].strftime('%Y-%m-%d')}|{task['completed']}\n"
                f.write(task_str)

    def load_tasks(self):
        try:
            with open("tasks.txt", "r") as f:
                self.tasks = []
                for line in f.readlines():
                    # Skip empty lines or lines that don't have 3 parts
                    line = line.strip()
                    if not line:  # Skip empty lines
                        continue
                    parts = line.split('|')
                    if len(parts) != 3:  # Skip lines that don't have exactly 3 parts
                        continue
                    
                    task_str, due_date_str, completed_str = parts
                    try:
                        due_date = datetime.datetime.strptime(due_date_str, "%Y-%m-%d")
                        completed = completed_str == "True"
                        self.tasks.append({"task": task_str, "due_date": due_date, "completed": completed})
                    except ValueError:
                        continue  # Skip any lines with invalid date format
                self.update_task_list()
        except FileNotFoundError:
            self.tasks = []

# Main function to run the app
if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()
