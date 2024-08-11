import tkinter as tk
from tkinter import ttk
from sympy import Matrix

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

class MatrixOperations:
    def __init__(self):
        self.window = tk.Toplevel()
        self.window.title("Matrix Operations")
        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.window, text="Matrix A:").pack()
        self.matrix_a = tk.Entry(self.window)
        self.matrix_a.pack()

        tk.Label(self.window, text="Matrix B:").pack()
        self.matrix_b = tk.Entry(self.window)
        self.matrix_b.pack()

        tk.Button(self.window, text="Add Matrices", command=self.add_matrices).pack()
        tk.Button(self.window, text="Multiply Matrices", command=self.multiply_matrices).pack()

    def add_matrices(self):
        try:
            mat_a = Matrix(eval(self.matrix_a.get()))
            mat_b = Matrix(eval(self.matrix_b.get()))
            result = mat_a + mat_b
            tk.messagebox.showinfo("Result", f"Sum:\n{result}")
        except Exception as e:
            tk.messagebox.showerror("Error", str(e))

    def multiply_matrices(self):
        try:
            mat_a = Matrix(eval(self.matrix_a.get()))
            mat_b = Matrix(eval(self.matrix_b.get()))
            result = mat_a * mat_b
            tk.messagebox.showinfo("Result", f"Product:\n{result}")
        except Exception as e:
            tk.messagebox.showerror("Error", str(e))

    def run(self):
        self.window.mainloop()

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
