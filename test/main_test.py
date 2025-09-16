# test/test_main.py
from src.main import odd_even

def test_odd_even():
    result = odd_even(4)
    assert result == "Even", "This should be even"

def test_odd_even_2():
    result = odd_even(5)
    assert result == "odd", "This should be Odd"