import tkinter as tk
from tkinter import messagebox
from sympy import Matrix

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
