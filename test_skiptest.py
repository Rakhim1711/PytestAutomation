import pytest
import sys
pytestmark=pytest.mark.skipif(sys.platform=='win32', reason ='will run only on Linux OS')



const = 9/5
def cent_to_fah(cent=0):
    fah = (cent * const) +32
    return fah

@pytest.mark.skip(reason='Skipping for no reason')
def test_case01():
    assert type(const)==float


@pytest.mark.skipif(sys.version_info > (3,6), reason='dosent work on py version above 3.6')
def test_case02():
    assert cent_to_fah() == 32
@pytest.mark.skipif(pytest.__version__>'5.5.0', reason='python version is less')
def test_case03():
    assert cent_to_fah(38) == 100.4



