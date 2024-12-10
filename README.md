# Scientic-Calculator-python

This is a Python-based **Scientific Calculator** with an interactive graphical user interface (GUI) built using the `tkinter` library. It supports basic arithmetic operations, advanced scientific calculations, and a programmer's calculator for number system conversions.

## Features

### Basic Arithmetic
- Addition (`+`), Subtraction (`-`), Multiplication (`*`), Division (`/`).
- Parentheses for grouping operations.
- Backspace (`C`) and Clear All (`AC`) buttons.

### Scientific Operations
- Trigonometric Functions:
  - `sin`, `cos`, `tan` with degree (`Deg`) and radian (`Rad`) modes.
  - Hyperbolic functions: `sinh`, `cosh`, `tanh`.
- Logarithmic Operations:
  - Natural logarithm (`log`), Base-10 logarithm (`log10`).
- Power and Roots:
  - Square root (`√`), nth root, exponential powers (`x^`).
- Constants:
  - Pi (`π`), Euler's number (`e`).
- Reciprocal (`1/x`) and Factorial (`!`).

### Programmer's Calculator
- Converts between Decimal, Binary, Octal, and Hexadecimal number systems.
- Dedicated buttons for Hexadecimal digits (`A-F`).
- Input validation and error handling.

### Memory Operations
- Add to memory (`M+`), Recall memory value (`MR`), Clear memory (`MC`).

### GUI Features
- Responsive design with large buttons for easy input.
- Clear text display for calculations and results.
- Dynamic updates for angle unit (`Deg` or `Rad`).

### Keyboard Shortcuts
- Numeric input: `0-9`
- Arithmetic: `+`, `-`, `*`, `/`
- Parentheses: `(`, `)`
- Equals (`=`), Delete (`Delete`), Backspace (`BackSpace`).

## How to Use

### Switching Modes
- **Degree/Radian**: Toggle between angle units using the `Deg`/`Rad` button.
- **Programmer Mode**: Access via the "Mode" menu to perform number conversions.

### Performing Calculations
1. Input numbers and operators using buttons or keyboard.
2. Use the memory buttons (`M+`, `MR`, `MC`) to store, recall, or clear values.
3. Press `=` to evaluate the expression.

### Programmer's Calculator
1. Select the desired number system from the dropdown menu (Decimal, Binary, Octal, Hexadecimal).
2. Enter a number and view conversions in the result display.

## Installation

1. **Prerequisites**:
   - Python 3.x installed on your machine.
   - Tkinter library (included with Python).

2. **Run the Application**:
   - Download or clone this repository.
   - Navigate to the directory containing `Scientific_calculator.py`.
   - Execute the script:
     ```bash
     python Scientific_calculator.py
     ```

## Known Issues
- Trigonometric calculations default to radians if the degree mode is not toggled properly.
- Programmer's calculator handles integers only.

## Future Enhancements
- Add more scientific operations (e.g., matrices, complex numbers).
- Improve the UI for better usability and modern design.
- Add support for floating-point inputs in the programmer's calculator.
