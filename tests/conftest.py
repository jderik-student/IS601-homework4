# conftest.py
from decimal import Decimal
import pytest
from faker import Faker
from calculator.operations import add, subtract, multiply, divide

fake = Faker()

def generate_test_data(num_records):

    for _ in range(num_records):
        a = Decimal(fake.random_number(digits=2))
        b = Decimal(fake.random_number(digits=2))
        operation = fake.random_element(elements=[add, subtract, multiply, divide])

        if operation.__name__ == "divide":
            b = Decimal('1') if b == Decimal('0')  else b

        expected = operation(a,b)

        yield a, b, operation, expected

def pytest_addoption(parser):
    parser.addoption("--num_records", action="store", default=10, type=int, help="Number of test records to generate")

def pytest_generate_tests(metafunc):
    if {"a", "b", "expected"}.intersection(set(metafunc.fixturenames)):
        num_records = metafunc.config.getoption("num_records")
        parameters = list(generate_test_data(num_records))
        metafunc.parametrize("a,b,operation,expected", list(parameters))
