import pytest 

from fizz_buzz import FizzBuzz

@pytest.mark.parametrize("input_number, expected_output", [
    (1, '1'),
    (2, '2'),
    (3, 'Fizz'),
    (5, 'Buzz'),
    (7, '7'),
    (11, '11'),
    (15, 'FizzBuzz'),
    (30, 'FizzBuzz'),

])
def test_print_number(input_number: int, expected_output: str):
    assert FizzBuzz.run(input_number) == expected_output

def test_print_Fizz():
    assert FizzBuzz.run(3) == "Fizz"

def test_print_Buzz():
    assert FizzBuzz.run(5) == "Buzz"
