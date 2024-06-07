# pylint: disable=unnecessary-dunder-call, invalid-name
'''
    This file contains tests to test the Calculation class
'''

from decimal import Decimal
import pytest
from calculator.calculation import Calculation
from calculator.operations import add, subtract, multiply, divide


@pytest.mark.parametrize(
    "a, b, operation, expected", 
    [
        # Test with Integers
        (Decimal('6'), Decimal('2'), add, Decimal('8')),
        (Decimal('6'), Decimal('2'), subtract, Decimal('4')),
        (Decimal('6'), Decimal('2'), multiply, Decimal('12')),
        (Decimal('6'), Decimal('2'), divide, Decimal('3')),
        # Test with Decimals
        (Decimal('6.6'), Decimal('2.2'), add, Decimal('8.8')),
        (Decimal('6.6'), Decimal('2.2'), subtract, Decimal('4.4')),
        (Decimal('6.6'), Decimal('2.2'), multiply, Decimal('14.52')),
        (Decimal('6.6'), Decimal('2.2'), divide, Decimal('3.0'))
    ]
)

def test_operations(a, b, operation, expected):
    """
        Tests Calculations with all four operations aginst both integers and Decimals.
        This test verifies that the Calculation class and the operation class are working as intended

        @param a: the first operand of the calculation
        @param b: the second operand of the calculation
        @param operation: the operation function to be used in th calculation
        @param expected: the expected result of the calculation
    """
    assert Calculation(a, b, operation).calculate() == expected

def test_repr():
    """
        Tests the string representation of the Calculation class
    """
    calc = Calculation.create(6, 2, add)
    expected = "Calculation(6, 2, add)"
    assert calc.__repr__() == expected

def test_divide_by_zero_test():
    """
        Tests division by zero to verify that it returns a ValueError
    """
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        Calculation(3, 0, divide).calculate()
