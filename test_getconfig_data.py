from pytest_topics.utilities.myconfigparser import *
import pytest


@pytest.mark.sbc
def test_getgmailurl():
    print(getGmailUrl(), ' here')
    assert getGmailUrl() == 'qa.gmail.com'


