import pytest
import sys


def test_strjoin():
    s1 = 'Python, Pytest and Automation'
    t1 = ['Python, Pytest', 'and', 'Automation']
    l2 = ['Python', 'Pytest and Automation']
    assert  ' '.join(t1) == s1




@pytest.mark.xfail(raises = IndexError, reason='knwown issue')
def test_str04():
    letters = 'abcdefhgijklmnopqrstuvwxyz'
    assert letters[100]

@pytest.mark.xfail(sys.platform!='win32', reason='works only in win32')
def test_str05():
    letters = 'abcd'
    num=1234
    assert letters + num == 'abcd1234'