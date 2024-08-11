import tkinter as tk
from tkinter import messagebox
from sympy import symbols, solve

class EquationSolver:
    def __init__(self):
        self.window = tk.Toplevel()
        self.window.title("Equation Solver")
        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.window, text="Enter equation (e.g., x**2 - 4 = 0):").pack()
        self.equation = tk.Entry(self.window)
        self.equation.pack()

        tk.Button(self.window, text="Solve", command=self.solve_equation).pack()

    def solve_equation(self):
        try:
            equation = self.equation.get()
            x = symbols('x')
            result = solve(equation, x)
            tk.messagebox.showinfo("Result", f"Solutions:\n{result}")
        except Exception as e:
            tk.messagebox.showerror("Error", str(e))

    def run(self):
        self.window.mainloop()
