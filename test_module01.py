

def test_a1():

    assert 5 + 9 == 14
    assert 5 * 5 == 25
    assert 5 * 3 == 15

# this is a failed test
def test_a2():
    assert 9/5 !=1.5, "Failed test intentioanlly "

#test_no3
def test_a3():
    assert 9//5 ==1 # Integer truncating division