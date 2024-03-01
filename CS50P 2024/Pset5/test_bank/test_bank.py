from bank import value


# Test greetings STARTING with "hello"
def test_hello():
    assert value("Hello") == 0
    assert value("Hello there!") == 0
    assert value("Hello, John") == 0


# Test greetings starting with "H" but not "hello"
def test_h():
    assert value("Hey there!") == 20
    assert value("How you doing?") == 20
    assert value("How's it going?") == 20


# Test greetings starting  with everything else but "hello" or "H"
def test_else():
    assert value("What's happening?") == 100
    assert value("What's up?") == 100
    assert value("Good morning") == 100


def test_case():
    assert value("HEY, wHAT'S up?") == 20
    assert value("HELlo tHERE") == 0
    assert value("Good morning") == 100
