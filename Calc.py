import tkinter as tk
import math

class Calc:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Calculator")
        self.window.geometry("375x667")
        self.window.configure(bg="#222222")
        self.window.resizable(False, False)
        self.input_expression = ""
        self.last_result_displayed = False
        self.create_display_area()
        self.create_buttons()

    def create_display_area(self):
        self.display_label = tk.Label(
            self.window,
            text="",
            anchor="e",
            bg="#222222",
            fg="white",
            font=("Times New Roman", 32, "bold"),
            padx=16
        )
        self.display_label.pack(expand=True, fill="both")

    def create_buttons(self):
        button_frame = tk.Frame(self.window, bg="#333333")
        button_frame.pack(expand=True, fill="both")
        button_layout = [
            ["7", "8", "9", "/", "CE"],
            ["4", "5", "6", "*", "√"],
            ["1", "2", "3", "-", "x²"],
            ["0", ".", "=", "+", "C"]
        ]
        for row_index, row in enumerate(button_layout):
            for col_index, button_text in enumerate(row):
                button = tk.Button(
                    button_frame,
                    text=button_text,
                    font=("Times New Roman", 18, "bold"),
                    bg="#444444",
                    fg="white",
                    activebackground="#1E1E1E",
                    command=lambda text=button_text: self.on_button_click(text),
                    borderwidth=0
                )
                button.grid(row=row_index, column=col_index, sticky="nsew", ipadx=10, ipady=20)
        for i in range(4):
            button_frame.rowconfigure(i, weight=1)
        for i in range(5):
            button_frame.columnconfigure(i, weight=1)

    def on_button_click(self, button_value):
        if button_value == "CE":
            self.input_expression = ""
        elif button_value == "C":
            self.input_expression = self.input_expression[:-1]
        elif button_value == "=":
            self.calculation()
        elif button_value == "x²":
            self.square()
        elif button_value == "√":
            self.root()
        else:
            if self.last_result_displayed and button_value not in "+-*/":
                self.input_expression = ""
            self.input_expression += str(button_value)
            self.last_result_displayed = False
        self.update_display()

    def calculation(self):
        try:
            result = str(eval(self.input_expression))
            self.input_expression = result
        except:
            self.input_expression = "ERROR"
        self.last_result_displayed = True

    def square(self):
        try:
            number = float(self.input_expression)
            self.input_expression = str(number ** 2)
        except:
            self.input_expression = "ERROR"
        self.last_result_displayed = True

    def root(self):
        try:
            number = float(self.input_expression)
            if number < 0:
                raise ValueError("Cannot take square root of negative number")
            self.input_expression = str(math.sqrt(number))
        except:
            self.input_expression = "ERROR"
        self.last_result_displayed = True

    def update_display(self):
        text_display = self.input_expression[-16:]
        self.display_label.config(text=text_display)

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    calculator = Calc()
    calculator.run()
