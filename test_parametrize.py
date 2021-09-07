import pytest
import math

@pytest.mark.parametrize('test_input', [82, 78, 45, 66])
def test_param01(test_input):
    assert test_input != 50



@pytest.mark.parametrize("inp, out", [(2,4), (3,27), (4, 256)])
def test_param02(inp, out):
    assert (inp ** inp)== out


data=[
    ([2,3,4], 'sum', 9),
    ([2,3,4], 'prod', 24),
]
@pytest.mark.para
@pytest.mark.parametrize("a, b, c", data)
def test_param03(a, b, c):
    if b == 'sum':
        assert sum(a) == c
    elif b == 'prod':
        assert math.prod(a) == c


def now(t):
    countP = 0
    countJ = 0
    countT = 0

    for i in t:
        if i.endswith('txt'):
            countT += 1
        elif i.endswith('py'):
            countP += 1
        elif i.endswith('java'):
            countJ += 1
    return countP, countJ, countT

argument = ['python.py', 'java.java', 'text.txt','smart.py', 'learn.py', 'learn.java']
lst1 = ['python.py', 'java.java', 'text.txt','smart.py', 'learn.py', 'learn.java','python.py', 'java.java', 'text.txt','smart.py', 'learn.py', 'learn.java']
lst2 = ['python.py', 'java.java', 'text.txt','smart.py', 'learn.py', 'learn.java','python.py', 'java.java', 'text.txt','smart.py', 'learn.py', 'learn.java', 'learn.java','python.py', 'java.java', 'text.txt','smart.py', 'learn.py', 'learn.java']
print(now(argument))

@pytest.mark.pix
@pytest.mark.parametrize('input, output', [(argument, (3,2,1)), (lst1, (6, 4, 2)), (lst2, (9, 7, 3))])
def test_user(input, output):
    assert now(input) == output



