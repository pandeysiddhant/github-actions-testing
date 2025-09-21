import pytest

@pytest.fixture()
def main_fixture():
    x = [1, 2, 3, 4, 5, 6]
    return x

def test_func_4(main_fixture):
    print(main_fixture)
    assert main_fixture[0:3] == [1, 2, 3]

z = [1,2,3,4,5,6,7,8]

@pytest.fixture()
def main_ifxture_2():
    zz = z.copy()
    zz = zz[::-1]
    yield zz
    print("\nDone", z)

def test_fix_2(main_ifxture_2):
    assert main_ifxture_2 == [8,7,6,5,4,3,2,1]

def test_random():
    a = "Sid"
    with pytest.raises(IndexError):
        assert a[100] == "a"
