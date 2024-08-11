import tkinter as tk
from tkinter import messagebox

class UnitConverter:
    def __init__(self):
        self.window = tk.Toplevel()
        self.window.title("Unit Converter")
        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.window, text="Convert from:").pack()
        self.from_unit = tk.Entry(self.window)
        self.from_unit.pack()

        tk.Label(self.window, text="Convert to:").pack()
        self.to_unit = tk.Entry(self.window)
        self.to_unit.pack()

        tk.Label(self.window, text="Value:").pack()
        self.value = tk.Entry(self.window)
        self.value.pack()

        tk.Button(self.window, text="Convert", command=self.convert_units).pack()

    def convert_units(self):
        value = float(self.value.get())
        from_unit = self.from_unit.get()
        to_unit = self.to_unit.get()
        # Example conversion logic; extend as needed
        converted_value = value  # Apply actual conversion
        tk.messagebox.showinfo("Result", f"{value} {from_unit} = {converted_value} {to_unit}")

    def run(self):
        self.window.mainloop()
