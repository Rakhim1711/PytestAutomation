import pytest
from pytest_topics.utilities.util import get_data

@pytest.mark.parametrize("a, b, c, d", get_data())
def test_check_data_from_file(a,b,c,d):
    print(a, b, c, d)
