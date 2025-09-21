import pytest

class TestMainParams:

    @pytest.mark.parametrize("test_param",[1,2,3,4,5])
    def test_func_1(self,test_param):
        assert test_param*test_param == test_param**2

    @pytest.mark.parametrize("test_param_2",["siddhant"])
    def test_func_2(self,test_param_2):
        assert test_param_2.upper() == "SIDDHANT"

    @pytest.mark.parametrize("test_param_3",[{3:(3,9)},{4:(5,20)},{6:(3,18)}])
    def test_func_3(self,test_param_3):
        for i,(j,k) in test_param_3.items():
            assert i*j == k

