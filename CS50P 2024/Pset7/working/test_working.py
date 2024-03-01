# Maimoona Aziz

from working import convert
import pytest


def test_format():
    assert convert(r"9:00 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert(r"9 AM to 5 PM") == "09:00 to 17:00"
    assert convert(r"9 AM to 5:30 PM") == "09:00 to 17:30"


def test_range():
    assert convert(r"10 PM to 8 AM") == "22:00 to 08:00"
    assert convert(r"10:30 PM to 8:50 AM") == "22:30 to 08:50"
    assert convert(r"2:30 PM to 5 AM") == "14:30 to 05:00"


def test_invalid():
    with pytest.raises(ValueError):
        convert(r"9:60 AM to 5:60 PM")
    with pytest.raises(ValueError):
        convert(r"9 AM - 5 PM")
    with pytest.raises(ValueError):
        convert(r"09:00 AM - 17:00 PM")
