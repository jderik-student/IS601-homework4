"""
    Entry point for Calculator program
"""
# pylint: disable=unnecessary-dunder-call, invalid-name


import sys
from decimal import Decimal, InvalidOperation
from calculator import Calculator

def calculate_and_print(a: str, b: str, operation_name: str) -> None:
    """
        Takes in 2 operands and an operation, performs the calculation, and prints the result

        @param a: the first operand
        @param b: the second operand
        @param operation_name: the name of the operation function
    """
    operation_mappings = {
        'add': Calculator.add,
        'subtract': Calculator.subtract,
        'multiply': Calculator.multiply,
        'divide': Calculator.divide
    }

    operation_preposition_mappings = {
        'add': "plus",
        'subtract': "minus",
        'multiply': "times",
        'divide': "divided by"
    }

    try:
        a_decimal, b_decimal = map(Decimal, [a, b])
        result = operation_mappings.get(operation_name) # Use get to handle unknown operations
        if result:
            print(f"The result of {a} {operation_preposition_mappings.get(operation_name)} {b} is equal to {result(a_decimal, b_decimal)}")
        else:
            print(f"Unknown operation: {operation_name}")
    except InvalidOperation:
        print(f"Invalid number input: {a} or {b} is not a valid number.")
    except Exception as e: # Catch-all for unexpected errors
        print(f"An error occurred: {e}")

def main():
    """
        Main method, exits if argv does not have 4 elements
    """
    if len(sys.argv) != 4:
        print("Usage: python calculator_main.py <number1> <number2> <operation>")
        sys.exit(1)

    _, a, b, operation = sys.argv
    calculate_and_print(a, b, operation)

if __name__ == '__main__':
    main()
