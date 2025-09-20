import pytest

class TestMyFunc1:
    def test_func_1(self):
        with pytest.raises(Exception):
            assert (1/0) == 1
    def test_func_2(self):
        assert "String" == "String"
skipping = False
class TestMyFunc2:

    # Skipping the test
    @pytest.mark.skipif(skipping == True, reason="Skipping this test because skipping=True")
    def test_func_1(self):
        assert 1 == (1/1)
    def test_func_2(self):
        assert 1//3 == 0
    # Below function tests the Index error
    def test_exception(self):
        a = "hsdhjdbjawhdbaj"
        with pytest.raises(IndexError):
            assert a[100] == "a"