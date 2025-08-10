# Complete Calculator in Python

[![Python](https://img.shields.io/badge/Python-3.x-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20Linux%20%7C%20macOS-lightgrey.svg)](https://www.python.org/)

An advanced scientific calculator developed in Python using tkinter with modern graphical interface and complete mathematical functionalities.

## 🚀 Features

### 🔢 Basic Operations
- **Addition (+)**: Adds two numbers
- **Subtraction (-)**: Subtracts two numbers
- **Multiplication (×)**: Multiplies two numbers
- **Division (÷)**: Divides two numbers
- **Exponentiation (^)**: Raises a number to the power of another
- **Modulo (mod)**: Returns the remainder of division

### ⚡ Advanced Operations
- **Square root (√)**: Calculates the square root of a number
- **Square (x²)**: Squares a number
- **Reciprocal (1/x)**: Calculates the inverse of a number
- **Absolute value (|x|)**: Returns the absolute value of a number
- **Factorial (!)**: Calculates the factorial of an integer

### 📐 Trigonometric Functions
- **Sine (sin)**: Calculates the sine of an angle in degrees
- **Cosine (cos)**: Calculates the cosine of an angle in degrees
- **Tangent (tan)**: Calculates the tangent of an angle in degrees

### 📊 Logarithmic Functions
- **Decimal logarithm (log)**: Calculates the logarithm in base 10
- **Natural logarithm (ln)**: Calculates the natural logarithm (base e)

### 🧮 Mathematical Constants
- **π (pi)**: Value of pi (3.14159...)
- **e**: Euler's number (2.71828...)

### 🎛️ Control Functions
- **C**: Clears the calculator
- **⌫**: Deletes the last digit
- **±**: Changes the sign of the number
- **=**: Executes the operation
- **()**: Parentheses for expressions (basic implementation)

## 🚀 How to Run

1. Make sure you have Python installed on your system
2. Tkinter is already included with the standard Python installation
3. Run the file:

```bash
python calculadora.py
```

## 🖥️ Interface

The calculator has an intuitive interface with:
- Large display to show numbers and results
- Buttons organized in a grid for easy access
- Responsive and modern layout
- Error handling for invalid operations

## ⚠️ Error Handling

The calculator includes handling for:
- Division by zero
- Square root of negative numbers
- Logarithm of non-positive numbers
- Factorial of negative or non-integer numbers
- Invalid inputs

## 💡 Usage Examples

1. **Basic operation**: Type `5 + 3 =` to get `8`
2. **Exponentiation**: Type `2 ^ 3 =` to get `8`
3. **Trigonometric function**: Type `30` and click `sin` to get the sine of 30°
4. **Constant**: Click `π` to insert the value of pi
5. **Factorial**: Type `5` and click `!` to get `120`

## 📋 Requirements

- Python 3.x
- tkinter (included with standard Python installation)
- math (standard Python library)

## 🏗️ Code Structure

The code is organized in a `Calculadora` class with methods for:
- `criar_interface()`: Configures the graphical interface
- `clicar_botao()`: Processes button clicks
- `calcular()`: Executes mathematical operations
- `operacao_unaria()`: Processes single-argument functions
- Auxiliary methods for clearing, deleting, etc.

The calculator is ready to use and can be easily expanded with new features!
