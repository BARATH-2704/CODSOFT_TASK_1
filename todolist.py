import tkinter as tk
from tkinter import messagebox

class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List Application")
        self.tasks = []
        
        self.frame = tk.Frame(self.root)
        self.frame.pack(pady=10)
        
        self.label1= tk.Label(self.root,text="New Task")
        self.label1.pack()
        self.entry_task = tk.Entry(self.root, width=55)
        self.entry_task.pack()
        
        self.button_frame = tk.Frame(self.root)
        self.button_frame.pack(pady=10)
        
        self.add_task_button = tk.Button(self.button_frame, text="Add Task", command=self.add_task)
        self.add_task_button.pack(side=tk.LEFT, padx=10)
        
        self.update_task_button = tk.Button(self.button_frame, text="Update Task", command=self.update_task)
        self.update_task_button.pack(side=tk.LEFT, padx=10)
        
        self.delete_task_button = tk.Button(self.button_frame, text="Delete Task", command=self.delete_task)
        self.delete_task_button.pack(side=tk.LEFT, padx=10)
        
        self.mark_completed_button = tk.Button(self.button_frame, text="Mark Completed", command=self.mark_completed)
        self.mark_completed_button.pack(side=tk.LEFT, padx=10)
        
        self.label=tk.Label(self.root,text="To Do List")
        self.label.pack()

        self.frame = tk.Frame(self.root)
        self.frame.pack(pady=10)

        self.task_listbox = tk.Listbox(self.frame, width=55, height=10, selectmode=tk.SINGLE)
        self.task_listbox.pack(side=tk.LEFT, fill=tk.BOTH)
        
        self.scrollbar = tk.Scrollbar(self.frame)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.BOTH)
        
        self.task_listbox.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.task_listbox.yview)

    def add_task(self):
        task = self.entry_task.get()
        if task != "":
            self.tasks.append(task)
            self.update_task_listbox()
        else:
            messagebox.showwarning("Warning", "You must enter a task.")
        self.entry_task.delete(0, tk.END)
    
    def update_task_listbox(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            self.task_listbox.insert(tk.END, task)
    
    def delete_task(self):
        try:
            selected_task_index = self.task_listbox.curselection()[0]
            self.tasks.pop(selected_task_index)
            self.update_task_listbox()
        except:
            messagebox.showwarning("Warning", "You must select a task to delete.")
    
    def update_task(self):
        try:
            selected_task_index = self.task_listbox.curselection()[0]
            new_task = self.entry_task.get()
            if new_task != "":
                self.tasks[selected_task_index] = new_task
                self.update_task_listbox()
            else:
                messagebox.showwarning("Warning", "You must enter a task.")
        except:
            messagebox.showwarning("Warning", "You must select a task to update.")
        self.entry_task.delete(0, tk.END)
    
    def mark_completed(self):
        try:
            selected_task_index = self.task_listbox.curselection()[0]
            self.tasks[selected_task_index] = self.tasks[selected_task_index] + " (Completed)"
            self.update_task_listbox()
        except:
            messagebox.showwarning("Warning", "You must select a task to mark as completed.")
    
if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()
