import pytest


def test_case01():
    with pytest.raises(ZeroDivisionError):
        assert (1/0)
        assert 3 > 3


def func1():
    raise ValueError('Exception func1 raised')

def test_case02():
    with pytest.raises(Exception) as excinfo:
        func1()
    print(str(excinfo))
    assert (str(excinfo.value))== 'Exception func1 raised'
