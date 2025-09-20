import pytest

def func_1(num):
    return num * num

# pytest.mark.thistest
def test_func_1():
    result = func_1(3)
    assert result == 9
# pytest.mark.thistest2
def test_func_2():
    assert "Name" == "Name"
