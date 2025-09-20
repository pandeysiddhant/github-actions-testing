# test/test_main.py
from src.main import odd_even,addition,pallindrome,check_prime,check_string

def test_odd_even():
    print("Testing odd even")
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

def test_prime():
    result = check_prime(3)
    assert result == "Prime"

def test_not_prime():
    result = check_prime(21)
    assert result == "Not Prime"

def test_longest_string():
    result = check_string("zsdghtafghrtplbvqzzzjertysu")
    assert result == "The longest sub-string is: fghrtplbvqzzzj"