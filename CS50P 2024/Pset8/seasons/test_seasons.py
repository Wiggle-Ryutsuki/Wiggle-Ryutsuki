# Maimoona Aziz

from seasons import validate_format


# Check format
def test_format():
    assert validate_format("1999-01-01") == ("1999", "01", "01")
    assert validate_format("January 1, 1999") == None
    assert validate_format("2023-01-17") == ("2023", "01", "17")
    assert validate_format("1970-1-1") == None
