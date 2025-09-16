# test/test_main.py
from src.main import odd_even,addition,pallindrome

def test_odd_even():
    result = odd_even(4)
    assert result == "Even", "This should be even"

def test_odd_even_2():
    result = odd_even(5)
    assert result == "odd", "This should be Odd"

def test_add():
    result = addition(4,5)
    assert result == 9

def test_not_pallindrome():
    result = pallindrome("Siddhant")
    assert result == "Not Pallindrome"

def test_pallindrome():
    result = pallindrome("sys")
    assert result == "Pallindrome"