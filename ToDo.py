import tkinter as tk
from tkinter import messagebox, simpledialog
from datetime import datetime

class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Todo List")
        self.root.geometry("400x550")
        self.tasks = []

        self.root.configure(bg="#A8F1FF")

        title = tk.Label(root, text="Todo List", font=("Times New Roman", 24, "bold"), fg="#4b0082", bg="#A8F1FF")
        title.pack(pady=15)

        self.entry = tk.Entry(root, font=("Times New Roman", 14), width=30, bd=0, relief="flat", highlightthickness=2)
        self.entry.pack(pady=10)

        self.add_button = tk.Button(root, text="Add Task", bg="#1E90FF", fg="white", font=("Times New Roman", 12), width=20,
                                    relief="flat", command=self.add_task)
        self.add_button.pack(pady=10)

        self.task_frame = tk.Frame(root, bg="#7AE2CF")
        self.task_frame.pack(pady=10, fill=tk.BOTH, expand=True)

        self.canvas = tk.Canvas(self.task_frame)
        self.scrollbar = tk.Scrollbar(self.task_frame, orient="vertical", command=self.canvas.yview)
        self.task_list = tk.Frame(self.canvas, bg="#7AE2CF")

        self.task_list.bind("<Configure>", lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")))
        self.canvas.create_window((0, 0), window=self.task_list, anchor="nw")
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        self.canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        bottom_frame = tk.Frame(root, bg="#A8F1FF")
        bottom_frame.pack(pady=10)

        self.complete_button = tk.Button(bottom_frame, text="Complete Task", bg="#32CD32", fg="white", font=("Times New Roman", 12, "bold"),
                                         width=15, relief="flat", command=self.mark_done)
        self.complete_button.grid(row=0, column=0, padx=5)

        self.remove_button = tk.Button(bottom_frame, text="Remove Task", bg="#DC143C", fg="white", font=("Times New Roman", 12, "bold"),
                                       width=15, relief="flat", command=self.remove_Task)
        self.remove_button.grid(row=0, column=1, padx=5)

        self.update_button = tk.Button(root, text="Update Task", bg="#FF8C00", fg="white", font=("Times New Roman", 12, "bold"), width=32,
                                       relief="flat", command=self.update_task)
        self.update_button.pack(pady=5)

    def add_task(self):
        task_text = self.entry.get().strip()
        if task_text:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
            var = tk.BooleanVar()
            task_data = {
                "text": task_text,
                "timestamp": timestamp,
                "var": var,
            }
            cb = tk.Checkbutton(self.task_list, text=f"{task_text} - {timestamp}", variable=var, anchor='w', font=("Times New Roman", 12, "bold"),
                                width=40, justify='left', bg="#7AE2CF", relief="flat")
            cb.var = var
            cb.task_data = task_data
            cb.pack(anchor="w", pady=5)
            self.tasks.append(cb)
            self.entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Please enter a task.")

    def mark_done(self):
        for cb in self.tasks:
            if cb.var.get():
                cb.config(fg="#32CD32")

    def remove_Task(self):
        for cb in self.tasks[:]:
            if cb.var.get():
                cb.destroy()
                self.tasks.remove(cb)

    def update_task(self):
        updated = False
        for cb in self.tasks:
            if cb.var.get():
                new_title = simpledialog.askstring("Update Task", "Enter new task title:")
                if new_title:
                    cb.task_data["text"] = new_title.strip()
                    cb.task_data["timestamp"] = datetime.now().strftime("%Y-%m-%d %H:%M")
                    cb.config(text=f"{cb.task_data['text']} - {cb.task_data['timestamp']}")
                    cb.config(fg="black")
                    cb.var.set(False)
                    updated = True
                    break
        if not updated:
            messagebox.showinfo("Update Task", "Please select a task to update.")

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()
