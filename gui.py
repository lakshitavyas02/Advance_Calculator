import tkinter as tk
from tkinter import messagebox, filedialog
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from sympy import symbols, sympify
from db_manager import insert_calculation, fetch_history
from utils import UnitConverter, FinancialCalculator, MatrixOperations, EquationSolver
from voice_input import process_voice_input
import csv
import math

class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Advanced Calculator with Graph Plotting")
        self.root.geometry("800x700")  # Set the initial size of the window
        self.expression = ""
        self.result_var = tk.StringVar()
        self.scientific_mode = False
        self.current_theme = "default"
        self.themes = {
            "default": {"bg": "#FFFFFF", "fg": "#000000", "button_bg": "#DDDDDD", "button_fg": "#000000"},
            "dark": {"bg": "#333333", "fg": "#FFFFFF", "button_bg": "#555555", "button_fg": "#FFFFFF"},
            "light": {"bg": "#F0F0F0", "fg": "#000000", "button_bg": "#FFFFFF", "button_fg": "#000000"}
        }
        self.create_widgets()

    def create_widgets(self):
        # Clear existing widgets
        for widget in self.root.winfo_children():
            widget.destroy()

        # Result Display
        result_frame = tk.Frame(self.root, bg=self.themes[self.current_theme]["bg"], padx=10, pady=10)
        result_frame.pack(pady=10, fill=tk.X)
        result_entry = tk.Entry(result_frame, textvariable=self.result_var, font=("Arial", 24), bd=10, 
                                insertwidth=2, width=14, borderwidth=4, bg=self.themes[self.current_theme]["bg"], 
                                fg=self.themes[self.current_theme]["fg"], justify='right')
        result_entry.grid(row=0, column=0, sticky="nsew")

        # Button Layout
        button_frame = tk.Frame(self.root, bg=self.themes[self.current_theme]["bg"], padx=10, pady=10)
        button_frame.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

        buttons = [
            ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
            ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
            ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
            ("0", 4, 0), (".", 4, 1), ("+", 4, 2), ("=", 4, 3),
            ("C", 5, 0), ("(", 5, 1), (")", 5, 2), ("History", 5, 3),
            ("x", 6, 0), ("Plot Graph", 6, 1, 2), ("Scientific", 6, 3),
            ("Unit Convert", 7, 0), ("Financial", 7, 1), ("Matrix", 7, 2), ("Solve", 7, 3),
            ("Voice", 8, 0), ("Export History", 8, 1, 3)
        ]

        for button in buttons:
            if len(button) == 3:
                text, row, col = button
                colspan = 1
            elif len(button) == 4:
                text, row, col, colspan = button
            else:
                continue

            btn = tk.Button(button_frame, text=text, padx=20, pady=20, font=("Arial", 18),
                            bg=self.themes[self.current_theme]["button_bg"], fg=self.themes[self.current_theme]["button_fg"],
                            relief="raised", bd=5, command=lambda t=text: self.on_button_click(t))
            btn.grid(row=row, column=col, columnspan=colspan, sticky="nsew")
            btn.bind("<Enter>", lambda e, b=btn: b.config(bg="#AAAAAA"))  # Hover effect
            btn.bind("<Leave>", lambda e, b=btn: b.config(bg=self.themes[self.current_theme]["button_bg"]))  # Reset color

        # Configure grid rows and columns to expand properly
        for i in range(5):
            button_frame.grid_columnconfigure(i, weight=1)
            button_frame.grid_rowconfigure(i, weight=1)

        # Scientific Mode Buttons
        self.scientific_buttons = {
            'sin': tk.Button(button_frame, text='sin', padx=20, pady=20, font=("Arial", 18),
                             bg=self.themes[self.current_theme]["button_bg"], fg=self.themes[self.current_theme]["button_fg"],
                             relief="raised", bd=5, command=lambda: self.on_button_click('sin')),
            'cos': tk.Button(button_frame, text='cos', padx=20, pady=20, font=("Arial", 18),
                             bg=self.themes[self.current_theme]["button_bg"], fg=self.themes[self.current_theme]["button_fg"],
                             relief="raised", bd=5, command=lambda: self.on_button_click('cos')),
            'tan': tk.Button(button_frame, text='tan', padx=20, pady=20, font=("Arial", 18),
                             bg=self.themes[self.current_theme]["button_bg"], fg=self.themes[self.current_theme]["button_fg"],
                             relief="raised", bd=5, command=lambda: self.on_button_click('tan')),
            'log': tk.Button(button_frame, text='log', padx=20, pady=20, font=("Arial", 18),
                             bg=self.themes[self.current_theme]["button_bg"], fg=self.themes[self.current_theme]["button_fg"],
                             relief="raised", bd=5, command=lambda: self.on_button_click('log')),
            'sqrt': tk.Button(button_frame, text='sqrt', padx=20, pady=20, font=("Arial", 18),
                              bg=self.themes[self.current_theme]["button_bg"], fg=self.themes[self.current_theme]["button_fg"],
                              relief="raised", bd=5, command=lambda: self.on_button_click('sqrt')),
            '^': tk.Button(button_frame, text='^', padx=20, pady=20, font=("Arial", 18),
                           bg=self.themes[self.current_theme]["button_bg"], fg=self.themes[self.current_theme]["button_fg"],
                           relief="raised", bd=5, command=lambda: self.on_button_click('^'))
        }

        self.update_scientific_mode()

        # Add a menu for theme selection
        menu = tk.Menu(self.root)
        self.root.config(menu=menu)
        theme_menu = tk.Menu(menu, tearoff=0)
        menu.add_cascade(label="Themes", menu=theme_menu)
        for theme in self.themes.keys():
            theme_menu.add_command(label=theme.capitalize(), command=lambda t=theme: self.change_theme(t))

    def on_button_click(self, char):
        if char == '=':
            try:
                self.calculate_result()
            except Exception as e:
                self.result_var.set("Error")
                messagebox.showerror("Error", str(e))
        elif char == 'C':
            self.expression = ""
            self.result_var.set("")
        elif char == 'History':
            self.show_history()
        elif char == 'Plot Graph':
            self.plot_graph()
        elif char == 'Scientific':
            self.toggle_scientific_mode()
        elif char == 'Unit Convert':
            self.unit_conversion()
        elif char == 'Financial':
            self.financial_calculations()
        elif char == 'Matrix':
            self.matrix_operations()
        elif char == 'Solve':
            self.equation_solver()
        elif char == 'Voice':
            self.voice_input()
        elif char == 'Export History':
            self.export_history()
        else:
            self.expression += str(char)
            self.result_var.set(self.expression)

    def calculate_result(self):
        try:
            allowed_functions = {func: getattr(math, func) for func in dir(math) if not func.startswith("__")}
            result = str(eval(self.expression, {"__builtins__": None}, allowed_functions))
            self.result_var.set(result)
            insert_calculation(self.expression, result)
            self.expression = result
        except Exception as e:
            self.result_var.set("Error")
            messagebox.showerror("Error", f"Invalid expression: {e}")

    def show_history(self):
        history_window = tk.Toplevel(self.root)
        history_window.title("Calculation History")
        history_window.configure(bg=self.themes[self.current_theme]["bg"])

        history = fetch_history()
        history_listbox = tk.Listbox(history_window, font=("Arial", 14), width=50, height=10,
                                     bg=self.themes[self.current_theme]["bg"], fg=self.themes[self.current_theme]["fg"])
        history_listbox.pack(pady=10)

        for item in history:
            history_listbox.insert(tk.END, f"{item[2]}: {item[0]} = {item[1]}")

        def on_select(event):
            selected = history_listbox.get(history_listbox.curselection())
            self.expression = selected.split(": ")[1].split(" = ")[0]
            self.result_var.set(self.expression)

        history_listbox.bind("<<ListboxSelect>>", on_select)

    def plot_graph(self):
        try:
            x = symbols('x')
            expression = sympify(self.expression)

            x_vals = range(-10, 11)
            y_vals = [expression.subs(x, i) for i in x_vals]

            fig = plt.figure(figsize=(5, 4), dpi=100)
            plt.plot(x_vals, y_vals, label=str(expression))
            plt.axhline(0, color='black', linewidth=0.5)
            plt.axvline(0, color='black', linewidth=0.5)
            plt.grid(True)
            plt.legend()

            graph_window = tk.Toplevel(self.root)
            graph_window.title("Graph")
            graph_window.configure(bg=self.themes[self.current_theme]["bg"])

            canvas = FigureCanvasTkAgg(fig, master=graph_window)
            canvas.draw()
            canvas.get_tk_widget().pack()

        except Exception as e:
            messagebox.showerror("Error", f"Invalid expression for plotting: {e}")

    def update_scientific_mode(self):
        for text, button in self.scientific_buttons.items():
            if self.scientific_mode:
                button.grid(row=1, column=list(self.scientific_buttons.keys()).index(text), sticky="nsew")
            else:
                button.grid_forget()

        for button in self.scientific_buttons.values():
            button.config(bg=self.themes[self.current_theme]["button_bg"], fg=self.themes[self.current_theme]["button_fg"])

    def toggle_scientific_mode(self):
        self.scientific_mode = not self.scientific_mode
        self.update_scientific_mode()
        mode = "Scientific" if self.scientific_mode else "Basic"
        tk.messagebox.showinfo("Mode Changed", f"Switched to {mode} Mode")

    def unit_conversion(self):
        unit_converter = UnitConverter()
        unit_converter.run()

    def financial_calculations(self):
        financial_calculator = FinancialCalculator()
        financial_calculator.run()

    def matrix_operations(self):
        matrix_operations = MatrixOperations()
        matrix_operations.run()

    def equation_solver(self):
        equation_solver = EquationSolver()
        equation_solver.run()

    def voice_input(self):
        process_voice_input()

    def export_history(self):
        try:
            history = fetch_history()
            if not history:
                tk.messagebox.showinfo("Export", "No history to export.")
                return

            file_path = filedialog.asksaveasfilename(defaultextension=".csv",
                                                   filetypes=[("CSV files", "*.csv")])
            if not file_path:
                return

            with open(file_path, mode='w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(["Timestamp", "Expression", "Result"])
                for record in history:
                    writer.writerow(record)
            tk.messagebox.showinfo("Export", "History successfully exported.")
        except Exception as e:
            tk.messagebox.showerror("Error", f"An error occurred while exporting history: {e}")

    def change_theme(self, theme_name):
        if theme_name in self.themes:
            self.current_theme = theme_name
            self.apply_theme()

    def apply_theme(self):
        self.root.configure(bg=self.themes[self.current_theme]["bg"])
        self.create_widgets()  # Recreate widgets with new theme

if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()
