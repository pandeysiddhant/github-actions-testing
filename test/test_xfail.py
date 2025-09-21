import pytest

fail = True

@pytest.mark.xfail()
# the below is the fail function
def test_func_1():
    assert "name" == "str"

@pytest.mark.xfail(fail == True, reason="This should be failed")
def test_func_2():
    assert "name" == "str"

@pytest.mark.xfail(fail,reason="This function is to fail")
def test_func_3():
    assert 4%2 != 0

