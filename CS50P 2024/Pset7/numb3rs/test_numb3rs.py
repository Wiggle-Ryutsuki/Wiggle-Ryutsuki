# Maimoona Aziz

from numb3rs import validate


def test_format():
    assert validate(r"127.0.0.1") == True
    assert validate(r"114.1.3.21.0") == False
    assert validate(r"1") == False
    assert validate(r"cat.dog.bird") == False
    assert validate(r"15.130.0.4") == True


def test_numbers():
    assert validate(r"255.255.255.255") == True
    assert validate(r"512.512.512.512") == False
    assert validate(r"1.2.3.1000") == False
    assert validate(r"1.1.512.1") == False
    assert validate(r"300.1.1.1") == False
    assert validate(r"1.1.1.600") == False
