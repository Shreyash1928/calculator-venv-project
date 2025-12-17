from calculator.main import Calculator

def test_multiple_operations():
    calc = Calculator()
    result = calc.add(2, 3) * calc.subtract(10, 5)
    assert result == 25  # (2+3) * (10-5) = 25
