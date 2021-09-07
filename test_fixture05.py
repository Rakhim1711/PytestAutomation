# Paramitarization with fixtures
import pytest


@pytest.fixture(params=[(3,4), [3,5]], ids=['tuple', 'list'])
def fixture01(request):
    return request.param

@pytest.fixture(params=['access', 'slice', 'assignment', 'len'])
def fixture02(request):
    return request.param

@pytest.mark.thisone
def test_fix_param01(fixture01):
    assert (type(fixture01)) in [tuple, list]

@pytest.mark.yes
def test_fix_param02(fixture01, fixture02):
    if (fixture02 == 'access'):
        assert (fixture01[0])
    elif (fixture02 == 'slice'):
        assert fixture01[::-1]


    elif (fixture02 == 'len'):
        assert len(fixture01)


