# Maimoona Aziz

from twttr import shorten


# Test uppercase
def test_uppercase():
    assert shorten("ALGORITHM") == "LGRTHM"
    assert shorten("EXCITING") == "XCTNG"
    assert shorten("BINARY") == "BNRY"
    assert shorten("PYTHON") == "PYTHN"
    assert shorten("UNIQUE") == "NQ"


# Test lowercase
def test_lowercase():
    assert shorten("database") == "dtbs"
    assert shorten("meow") == "mw"
    assert shorten("twitter") == "twttr"
    assert shorten("oranges are great this season") == "rngs r grt ths ssn"
    assert shorten("the universe is your oyster") == "th nvrs s yr ystr"


# Test mixed words and sentences
def test_mixed():
    assert shorten("CS50") == "CS50"
    assert shorten("What's your name?") == "Wht's yr nm?"
    assert shorten("R2d2!") == "R2d2!"
    assert shorten("5 BIG brown foxEs") == "5 BG brwn fxs"
    assert shorten("2 HUndred And 3 pieCes of F1sh") == "2 Hndrd nd 3 pCs f F1sh"
