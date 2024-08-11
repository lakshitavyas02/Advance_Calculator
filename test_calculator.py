import unittest
from tkinter import Tk
from db_manager import fetch_history
from financial_calculator import FinancialCalculator
from unit_converter import UnitConverter
from matrix_operations import MatrixOperations
from equation_solver import EquationSolver
from plot_graph import PlotGraph

class TestAdvancedCalculator(unittest.TestCase):
    
    def setUp(self):
        self.root = Tk()

    def test_financial_calculator(self):
        calculator = FinancialCalculator()
        calculator.amount.insert(0, '1000')
        calculator.rate.insert(0, '5')
        calculator.time.insert(0, '2')
        calculator.calculate()
        # Check for expected result, can be adjusted based on actual logic

    def test_unit_converter(self):
        converter = UnitConverter()
        converter.from_unit.insert(0, 'meters')
        converter.to_unit.insert(0, 'kilometers')
        converter.value.insert(0, '1000')
        converter.convert_units()
        # Check conversion result

    def test_matrix_operations(self):
        matrix_ops = MatrixOperations()
        matrix_ops.matrix_a.insert(0, '[[1, 2], [3, 4]]')
        matrix_ops.matrix_b.insert(0, '[[5, 6], [7, 8]]')
        matrix_ops.add_matrices()
        matrix_ops.multiply_matrices()
        # Check results for matrix addition and multiplication

    def test_equation_solver(self):
        solver = EquationSolver()
        solver.equation.insert(0, 'x**2 - 4')
        solver.solve_equation()
        # Check for expected result

    def test_plot_graph(self):
        plotter = PlotGraph()
        plotter.equation_entry.insert(0, 'x**2 - 4')
        plotter.plot_graph()
        # Ensure the graph plotting function executes without error

    def tearDown(self):
        self.root.destroy()

if __name__ == "__main__":
    unittest.main()
