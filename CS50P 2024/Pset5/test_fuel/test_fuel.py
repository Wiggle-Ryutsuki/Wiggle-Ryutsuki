# Maimoona Aziz

from fuel import convert, gauge
import pytest


# Test invalid cases
def test_invalid():
    with pytest.raises(ZeroDivisionError):
        convert("100/0")
    with pytest.raises(ZeroDivisionError):
        convert("4/0")
    with pytest.raises(ValueError):
        convert("10/3")
    with pytest.raises(ValueError):
        convert("three/four")
    with pytest.raises(ValueError):
        convert("1.5/4")
    with pytest.raises(ValueError):
        convert("5-10")


# Test convert outputs
def test_percent():
    assert convert("3/4") == 75
    assert convert("1/3") == 33
    assert convert("2/3") == 67
    assert convert("50/100") == 50


# Test gauge outputs
def test_guage():
    assert gauge(0) == "E"
    assert gauge(100) == "F"
    assert gauge(99) == "F"
    assert gauge(1) == "E"
    assert gauge(75) == "75%"
    assert gauge(50) == "50%"
    assert gauge(33) == "33%"
