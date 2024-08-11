# Advanced Calculator with Graph Plotting

## Overview
This project is an advanced calculator application built with Python using Tkinter for the GUI. It includes various functionalities such as basic arithmetic operations, scientific calculations, unit conversions, financial calculations, matrix operations, equation solving, and graph plotting. The calculator also supports voice input and maintains a history of calculations that can be exported to a CSV file.

## Features
- **Basic Arithmetic Operations**: Addition, subtraction, multiplication, division.
- **Scientific Calculations**: Functions like sin, cos, tan, log, sqrt, and exponentiation.
- **Graph Plotting**: Plot linear and other mathematical functions involving variable `x`.
- **Unit Conversion**: Convert between different units.
- **Financial Calculations**: Perform various financial calculations.
- **Matrix Operations**: Solve matrix operations.
- **Equation Solver**: Solve algebraic equations.
- **Voice Input**: Perform calculations using voice commands.
- **History**: View and export calculation history.

## Installation
1. **Clone the repository**:
    ```bash
    git clone https://github.com/yourusername/advanced-calculator.git
    cd advanced-calculator
    ```

2. **Create a virtual environment**:
    ```bash
    python -m venv venv
    ```

3. **Activate the virtual environment**:
    - On Windows:
      ```bash
      venv\Scripts\activate
      ```
    - On macOS/Linux:
      ```bash
      source venv/bin/activate
      ```

4. **Install the required packages**:
    ```bash
    pip install -r requirements.txt
    ```

## Usage
1. **Run the application**:
    ```bash
    python gui.py
    ```

2. **Interface**:
    - **Basic Mode**: Use buttons to perform basic arithmetic operations.
    - **Scientific Mode**: Switch to scientific mode to access trigonometric functions, logarithms, and square roots.
    - **Graph Plotting**: Enter an expression involving `x` and click "Plot Graph" to see the graph.
    - **History**: Click "History" to view past calculations and "Export History" to save them to a CSV file.
    - **Unit Conversion**: Click "Unit Convert" to convert units.
    - **Financial Calculations**: Click "Financial" to perform financial calculations.
    - **Matrix Operations**: Click "Matrix" to perform matrix operations.
    - **Equation Solver**: Click "Solve" to solve algebraic equations.
    - **Voice Input**: Click "Voice" to use voice commands for calculations.

## Requirements
- Python 3.x
- Tkinter
- Matplotlib
- SymPy
- Required libraries listed in `requirements.txt`

## File Structure
- `gui.py`: Main application file containing the GUI and calculator logic.
- `db_manager.py`: Manages the database operations for storing and fetching history.
- `utils.py`: Contains classes for unit conversion, financial calculations, matrix operations, and equation solving.
- `voice_input.py`: Handles voice input processing.
- `plot_graph.py`: Provides functionalities for plotting graphs.
- `requirements.txt`: Lists the Python packages required for the project.

## Example Usage

To plot a graph of the function `x**2 + 2*x + 1`:

1. Enter `x**2 + 2*x + 1` into the expression field.
2. Click "Plot Graph" to visualize the function.

## Contributing
Feel free to open issues or submit pull requests if you have any suggestions or improvements.

## Acknowledgments
- Thanks to the developers of the Tkinter, Matplotlib, and SymPy libraries.
