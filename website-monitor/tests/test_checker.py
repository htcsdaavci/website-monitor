import pytest
from monitor import checker

def test_check_url_up():
    assert checker.check_url("https://www.google.com") == True
    assert checker.check_url("https://www.wikipedia.com") == True
    assert checker.check_url("https://www.rockstargames.com") == True

def test_check_url_down():
    assert checker.check_url("https://nichtvorhandenseite.tld") == False
