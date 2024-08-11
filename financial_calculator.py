import tkinter as tk
from tkinter import messagebox

class FinancialCalculator:
    def __init__(self):
        self.window = tk.Toplevel()
        self.window.title("Financial Calculator")
        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.window, text="Enter amount:").pack()
        self.amount = tk.Entry(self.window)
        self.amount.pack()

        tk.Label(self.window, text="Interest rate (%):").pack()
        self.rate = tk.Entry(self.window)
        self.rate.pack()

        tk.Label(self.window, text="Time (years):").pack()
        self.time = tk.Entry(self.window)
        self.time.pack()

        tk.Button(self.window, text="Calculate", command=self.calculate).pack()

    def calculate(self):
        amount = float(self.amount.get())
        rate = float(self.rate.get())
        time = float(self.time.get())
        # Simple interest calculation
        interest = (amount * rate * time) / 100
        tk.messagebox.showinfo("Result", f"Interest: {interest}")

    def run(self):
        self.window.mainloop()
