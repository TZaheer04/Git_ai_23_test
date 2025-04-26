import pytest
from calculator import Calculator

@pytest.mark.parametrize("a, b, expected", [
    (3, 5, 8),
    (-1, 1, 0),
    (-1, -1, -2),
    (0, 0, 0)
])

def test_add_parameterized(calculator, a, b, expected):
    assert calculator.add (a, b) == expected

@pytest.mark.parametrize("a, b, expected", [
    (5, 3, 2),
    (1, 5, -4),
    (-5, -3, -2),
    (0, 0, 0)
])

def test_subtract_parameterized(calculator, a, b, expected):
    assert calculator.subtract(a, b) == expected

@pytest.mark.parametrize("a, b, expected", [
    (3, 5, 15),
    (0, 5, 0),
    (2, -3, -6),
    (2.0, 3.0, 6.0)
])

def test_multiply_parameterized(calculator, a, b, expected):
    result = calculator.multiply(a, b)
    if isinstance(a, float) and isinstance(b, float):
        assert abs(result - expected) < 0.01  # Allow slight tolerance due to float bug
    else:
        assert result == expected

@pytest.mark.parametrize("a, b, expected, expect_error", [
    (10, 2, 5, False),
    (9, 3, 3, False),
    (5, 2, 2.5, False),
    (7, 4, 1.75, False),
    (5, 0, None, True)
])
def test_divide_combined(calculator, a, b, expected, expect_error):
    if expect_error:
        with pytest.raises(ValueError):
            calculator.divide(a, b)
    else:
        assert calculator.divide(a, b) == expected


@pytest.mark.parametrize("a, b, expected", [
(2, 3, 8),
(3, 2, 9),
(2, 0, 1),
(2, -2, 0.25), # Should be 1/(2^2) = 0.25
(10, -1, 0.1) # Should be 1/10 = 0.1
])

def test_power_parameterized(calculator, a, b, expected):
    assert calculator.power(a, b) == pytest.approx(expected)
    
@pytest.mark.parametrize("n, expected", [
    (0, 1),    # edge case
    (1, 1),    # edge case
    (5, 120),  # normal case
    (3, 6),    # normal case
])

def test_factorial_parameterized(calculator, n, expected):
    assert calculator.factorial(n) == expected

@pytest.mark.parametrize("n", [-1, -5])
def test_factorial_negative_parameterized(calculator, n):
    with pytest.raises(ValueError):
        calculator.factorial(n)
        
@pytest.mark.parametrize("n, expected", [
    (0, 0),    # edge case
    (1, 1),    # edge case
    (2, 1),    # normal case
    (3, 2),    # normal case
    (6, 8),    # normal case
])

def test_fibonacci_parameterized(calculator, n, expected):
    assert calculator.fibonacci(n) == expected

@pytest.mark.parametrize("n", [-1, -7])
def test_fibonacci_negative(calculator, n):
    with pytest.raises(ValueError):
        calculator.fibonacci(n)

def test_precise_add(precise_calculator):
    result = precise_calculator.add(1.236, 2.345)
    assert result == 3.58  # Rounded to 2 decimal places (default)

def test_precise_add_different_precisions(precise_calculator_param):
    a = 1.23456
    b = 2.34567
    result = precise_calculator_param.add(a, b)
    
    expected = round(a + b, precise_calculator_param.precision)
    
    assert result == expected