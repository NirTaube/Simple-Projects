import math
import cmath
import numpy as np

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Undefined (division by zero)"
    return x / y

def power(x, y):
    return x ** y

def square_root(x):
    return cmath.sqrt(x)

def log_base_10(x):
    return cmath.log10(x)

def natural_log(x):
    return cmath.log(x)

def sine(x):
    return math.sin(x)

def cosine(x):
    return math.cos(x)

def tangent(x):
    return math.tan(x)

def factorial(x):
    if x < 0:
        return "Undefined"
    return math.factorial(x)

def arcsine(x):
    return math.asin(x)

def arccosine(x):
    return math.acos(x)

def arctangent(x):
    return math.atan(x)

def get_matrix():
    rows = int(input("Enter number of rows for the matrix: "))
    cols = int(input("Enter number of columns for the matrix: "))
    matrix = []
    for i in range(rows):
        row = []
        for j in range(cols):
            row.append(float(input(f"Enter element [{i+1},{j+1}]: ")))
        matrix.append(row)
    return np.array(matrix)

def matrix_addition(A, B):
    return np.add(A, B)

def matrix_subtraction(A, B):
    return np.subtract(A, B)

def matrix_multiplication(A, B):
    return np.matmul(A, B)

def evaluate_polynomial():
    coeffs = [float(x) for x in input("Enter the polynomial coefficients separated by spaces (from highest to lowest degree): ").split()]
    x = float(input("Enter the value of x: "))
    return np.polyval(coeffs, x)

def decimal_to_base(num, base):
    if base == 2:
        return bin(num).replace("0b", "")
    elif base == 8:
        return oct(num).replace("0o", "")
    elif base == 16:
        return hex(num).replace("0x", "").upper()
    else:
        return "Base not supported."

def base_to_decimal(num_str, base):
    if base == 2:
        return int(num_str, 2)
    elif base == 8:
        return int(num_str, 8)
    elif base == 16:
        return int(num_str, 16)
    else:
        return "Base not supported."

def main():
    while True:
        # Display menu
        print("\nOptions:")
        print("Enter 'add' for addition")
        print("Enter 'subtract' for subtraction")
        print("Enter 'multiply' for multiplication")
        print("Enter 'divide' for division")
        print("Enter 'power' to raise a number to a power")
        print("Enter 'sqrt' to find the square root")
        print("Enter 'log' for logarithm base 10")
        print("Enter 'ln' for natural logarithm")
        print("Enter 'sin' for sine")
        print("Enter 'cos' for cosine")
        print("Enter 'tan' for tangent")
        print("Enter 'asin' for arcsine")
        print("Enter 'acos' for arccosine")
        print("Enter 'atan' for arctangent")
        print("Enter 'factorial' for factorial")
        print("Enter 'quit' to end the program")

        # User input
        user_input = input(": ")

        if user_input == "quit":
            break
        # Matrix operations
        elif user_input == "matrix_add":
            print("Enter first matrix:")
            A = get_matrix()
            print("Enter second matrix:")
            B = get_matrix()
            print(matrix_addition(A, B))
        elif user_input == "matrix_sub":
            print("Enter first matrix:")
            A = get_matrix()
            print("Enter second matrix:")
            B = get_matrix()
            print(matrix_subtraction(A, B))
        elif user_input == "matrix_mult":
            print("Enter first matrix:")
            A = get_matrix()
            print("Enter second matrix:")
            B = get_matrix()
            print(matrix_multiplication(A, B))
        
        # Polynomial evaluation
        elif user_input == "polynomial":
            print(evaluate_polynomial())
        
        # Base conversions
        elif user_input == "to_bin" or user_input == "to_oct" or user_input == "to_hex":
            num = int(input("Enter the decimal number: "))
            if user_input == "to_bin":
                print(decimal_to_base(num, 2))
            elif user_input == "to_oct":
                print(decimal_to_base(num, 8))
            elif user_input == "to_hex":
                print(decimal_to_base(num, 16))
        elif user_input == "from_bin" or user_input == "from_oct" or user_input == "from_hex":
            num_str = input("Enter the number: ")
            if user_input == "from_bin":
                print(base_to_decimal(num_str, 2))
            elif user_input == "from_oct":
                print(base_to_decimal(num_str, 8))
            elif user_input == "from_hex":
                print(base_to_decimal(num_str, 16))
        else:
            print("Invalid Input")

        # For operations that need two inputs
        if user_input in ("add", "subtract", "multiply", "divide", "power"):
            x = complex(input("Enter first number: "))
            y = complex(input("Enter second number: "))

            if user_input == "add":
                print(add(x, y))
            elif user_input == "subtract":
                print(subtract(x, y))
            elif user_input == "multiply":
                print(multiply(x, y))
            elif user_input == "divide":
                print(divide(x, y))
            elif user_input == "power":
                print(power(x, y))

        # For operations that need one input
        else:
            x = complex(input("Enter the number: "))

            if user_input == "sqrt":
                print(square_root(x))
            elif user_input == "log":
                print(log_base_10(x))
            elif user_input == "ln":
                print(natural_log(x))
            elif user_input == "sin":
                print(sine(x.real))  # Only real part for trigonometric functions
            elif user_input == "cos":
                print(cosine(x.real))
            elif user_input == "tan":
                print(tangent(x.real))
            elif user_input == "asin":
                print(arcsine(x.real))
            elif user_input == "acos":
                print(arccosine(x.real))
            elif user_input == "atan":
                print(arctangent(x.real))
            elif user_input == "factorial":
                if x.imag == 0:  # Factorial is defined for non-negative integers
                    print(factorial(int(x.real)))
                else:
                    print("Factorial is not defined for complex numbers.")

if __name__ == "__main__":
    main()
