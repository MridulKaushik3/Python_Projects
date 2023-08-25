import tkinter as tk
from tkinter import messagebox
import random

def generate_password(length):
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_-+=<>?"
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def copy_to_clipboard(password):
    root.clipboard_clear()
    root.clipboard_append(password)
    root.update()

def generate_button_click():
    try:
        user_id = user_id_entry.get().strip()
        length = int(length_entry.get())
        
        if length < 6:
            messagebox.showwarning("Invalid Length", "Password length should be at least 6 characters.")
        elif not user_id:
            messagebox.showwarning("Missing User ID", "Please enter a user ID.")
        else:
            password = generate_password(length)
            password_label.config(text="Generated Password: " + password)
            copy_button.config(state=tk.NORMAL)
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number for password length.")

root = tk.Tk()
root.title("Password Generator")

root.configure(bg="Peach Puff2")
root.geometry("350x350")

user_id_label = tk.Label(root, text="User ID:", bg="Snow")
user_id_label.pack(pady=10)

user_id_entry = tk.Entry(root)
user_id_entry.pack(pady=5)

length_label = tk.Label(root, text="Password Length:", bg="Snow")
length_label.pack(pady=5)

length_entry = tk.Entry(root)
length_entry.pack(pady=5)

generate_button = tk.Button(root, text="Generate Password", command=generate_button_click, bg="SkyBlue2", fg="white")
generate_button.pack(pady=10)

password_label = tk.Label(root, text="", font=("Helvetica", 12, "bold"), bg="Peach Puff2")
password_label.pack(pady=10)

copy_button = tk.Button(root, text="Copy Password", state=tk.DISABLED, command=lambda: copy_to_clipboard(password_label.cget("text")[19:]),
                        bg="SkyBlue2", fg="white")
copy_button.pack(pady=5)

root.mainloop()
