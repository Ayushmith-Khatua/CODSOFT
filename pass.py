import customtkinter
import random
import string
from tkinter import messagebox

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

def generate_password():
    try:
        length = int(length_entry.get())
        if length < 4:
            messagebox.showwarning("Warning", "Password length must be at least 4.")
            return
        if length > 25:
            messagebox.showwarning("Warning", "Password length must not exceed 25.")
            return
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for _ in range(length))
        result_entry.configure(state="normal")
        result_entry.delete(0, customtkinter.END)
        result_entry.insert(0, password)
        result_entry.configure(state="readonly")
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number.")

app = customtkinter.CTk()
app.title("Password Generator")
app.geometry("500x300")

title_label = customtkinter.CTkLabel(app, text="Password Generator", font=("Saira", 20, "bold"))
title_label.pack(pady=20)

length_entry = customtkinter.CTkEntry(app, placeholder_text="Enter length", width=150, font=("Saira", 14), justify="center")
length_entry.pack(pady=10)

generate_button = customtkinter.CTkButton(
    app,
    text="Generate",
    corner_radius=20,
    font=("Saira", 14, "bold"),
    fg_color="#007FFF",
    hover_color="#0059b3",
    text_color="white",
    command=generate_password
)
generate_button.pack(pady=15)

result_entry = customtkinter.CTkEntry(app, width=300, font=("Saira", 14), justify="center", state="readonly")
result_entry.pack(pady=10)

app.mainloop()
