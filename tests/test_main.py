'''
    This file contains tests to test main.py
'''

import sys
import pytest
from main import main, calculate_and_print  # Ensure this import matches your project structure

@pytest.mark.parametrize("a_string, b_string, operation_string, expected_string", [
    ("5", "3", 'add', "The result of 5 plus 3 is equal to 8"),
    ("10", "2", 'subtract', "The result of 10 minus 2 is equal to 8"),
    ("4", "5", 'multiply', "The result of 4 times 5 is equal to 20"),
    ("20", "4", 'divide', "The result of 20 divided by 4 is equal to 5"),
    ("1", "0", 'divide', "An error occurred: Cannot divide by zero"),
    ("9", "3", 'unknown', "Unknown operation: unknown"),
    ("a", "3", 'add', "Invalid number input: a or 3 is not a valid number."),
    ("5", "b", 'subtract', "Invalid number input: 5 or b is not a valid number.")
])
def test_calculate_and_print(a_string, b_string, operation_string, expected_string, capsys):
    """
        Tests the calculate_and_print method with the above parametrized test set

        @param a_string: the first operand
        @param b_string: the second operand
        @param operation_string: the operation function
        @param expected_string: the expected result of the calculation
        @param capsys: stdout/stderr
    """
    calculate_and_print(a_string, b_string, operation_string)
    captured = capsys.readouterr()
    assert captured.out.strip() == expected_string, f"Expected: {expected_string} But Printed: {captured.out.strip()}"

def test_main(capsys):
    """
        Tests the main method with a valid set of arguments

        @param capsys: stdout/stderr
    """
    sys.argv = ["main.py", "1", "2", "add"]
    main()
    captured = capsys.readouterr()
    assert captured.out.strip() == "The result of 1 plus 2 is equal to 3", "Expected: The result of 1 plus 2 is equal to 3"

def test_main_invalid_num_of_arg():
    """
        Tests the main method with an ivalid set of arguments
    """
    with pytest.raises(SystemExit):
        sys.argv = ["main.py", "1", "2", "add", "add"]
        main()
