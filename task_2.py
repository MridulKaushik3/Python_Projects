import tkinter as tk
from tkinter import messagebox

def add_task():
    task = task_entry.get()
    if task:
        tasks.append(task)
        update_tasks()

def update_tasks():
    for widget in tasks_frame.winfo_children():
        widget.destroy()

    for idx, task in enumerate(tasks):
        task_frame = tk.Frame(tasks_frame)
        task_frame.pack(fill="x", pady=10)

        task_label = tk.Label(task_frame, text=task, anchor="w", font=("Times New Roman", 14))
        task_label.pack(side="left")

        edit_button = tk.Button(task_frame, text="Edit", command=lambda t=task: edit_task(t), font=("Times New Roman", 12))
        edit_button.pack(side="left", padx=10)

        delete_button = tk.Button(task_frame, text="Delete", command=lambda t=task: delete_task(t), font=("Times New Roman", 12))
        delete_button.pack(side="left", padx=10)

def edit_task(task):
    edit_window = tk.Toplevel(root)
    edit_window.title("Edit Task")

    edited_task_entry = tk.Entry(edit_window, font=("Times New Roman", 14))
    edited_task_entry.pack(fill="x")

    save_button = tk.Button(edit_window, text="Save", command=lambda: save_edited_task(task, edited_task_entry.get(), edit_window), font=("Times New Roman", 12))
    save_button.pack()

def save_edited_task(old_task, new_task, window):
    if new_task:
        tasks[tasks.index(old_task)] = new_task
        update_tasks()
        window.destroy()

def delete_task(task):
    tasks.remove(task)
    update_tasks()

root = tk.Tk()
root.title("Todo List")
root.geometry("550x550")

tasks = []

add_label = tk.Label(root, text="Add Tasks:", font=("Times New Roman", 18))
add_label.pack(anchor="w")

task_entry = tk.Entry(root, font=("Times New Roman", 16))
task_entry.pack(fill="x")

add_button = tk.Button(root, text="Add Task", command=add_task, font=("Times New Roman", 14))
add_button.pack(anchor="w")

your_tasks_label = tk.Label(root, text="Your Tasks:", font=("Times New Roman", 18))
your_tasks_label.pack(anchor="w")

tasks_frame = tk.Frame(root)
tasks_frame.pack(fill="both", expand=True)

root.mainloop()


   