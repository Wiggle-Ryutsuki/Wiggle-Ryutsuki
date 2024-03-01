# Maimoona Aziz

from plates import is_valid


# Test uppercase
def test_max_min():
    assert is_valid("H") == False
    assert is_valid("50") == False
    assert is_valid("CS5") == True
    assert is_valid("CS50") == True
    assert is_valid("FIFT50") == True
    assert is_valid("OUTATIME") == False


# Test lowercase
def test_two_letters():
    assert is_valid("MA123") == True
    assert is_valid("M1C43") == False
    assert is_valid("400MC") == False
    assert is_valid("HI435") == True


# Test mixed words and sentences
def test_numbers():
    assert is_valid("CS50P2") == False
    assert is_valid("CS05") == False
    assert is_valid("ECTO88") == True

def test_punctuation():
    assert is_valid("PI3.14") == False
    assert is_valid("HI,MYNAMEIS9") == False
    assert is_valid("VICTR1") == True
