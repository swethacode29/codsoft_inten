import tkinter as tk
from tkinter import messagebox

class TodoListApp:
    def __init__(self, master):
        self.master = master
        self.master.title("To-Do List App")
        self.master.config(bg="#3498db")  # Set background color to blue

        self.tasks = []

        self.task_entry = tk.Entry(master, width=40, font=('Helvetica', 12))
        self.task_entry.pack(pady=10)

        self.add_button = tk.Button(master, text="Add Task", command=self.add_task, bg="#2ecc71", fg="white", font=('Helvetica', 10, 'bold'))  # Set button color to green
        self.add_button.pack(side=tk.LEFT, padx=5)  # Align to left with some padding

        self.task_list = tk.Listbox(master, width=50, font=('Helvetica', 12))
        self.task_list.pack(pady=10)

        self.delete_button = tk.Button(master, text="Delete Task", command=self.delete_task, bg="#e74c3c", fg="white", font=('Helvetica', 10, 'bold'))  # Set button color to red
        self.delete_button.pack(side=tk.LEFT, padx=5)  # Align to left with some padding

        self.exit_button = tk.Button(master, text="Exit", command=self.master.destroy, bg="#f39c12", fg="white", font=('Helvetica', 10, 'bold'))  # Set button color to orange
        self.exit_button.pack(side=tk.LEFT, padx=5)  # Align to left with some padding

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append(task)
            self.task_list.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Please enter a task.")

    def delete_task(self):
        try:
            index = self.task_list.curselection()[0]
            self.task_list.delete(index)
            del self.tasks[index]
        except IndexError:
            messagebox.showwarning("Warning", "Please select a task to delete.")

def main():
    root = tk.Tk()
    app = TodoListApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
