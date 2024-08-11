import tkinter as tk
from tkinter import simpledialog
import matplotlib.pyplot as plt
import numpy as np

class PlotGraph:
    def __init__(self):
        self.window = tk.Toplevel()
        self.window.title("Plot Graph")
        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.window, text="Enter equation (e.g., x**2 - 4):").pack()
        self.equation_entry = tk.Entry(self.window)
        self.equation_entry.pack()

        tk.Button(self.window, text="Plot", command=self.plot_graph).pack()

    def plot_graph(self):
        equation = self.equation_entry.get()
        try:
            x = np.linspace(-10, 10, 400)
            y = eval(equation)
            plt.figure()
            plt.plot(x, y)
            plt.title(f'Plot of {equation}')
            plt.xlabel('x')
            plt.ylabel('y')
            plt.grid(True)
            plt.show()
        except Exception as e:
            tk.messagebox.showerror("Error", f"Failed to plot graph: {e}")

    def run(self):
        self.window.mainloop()
