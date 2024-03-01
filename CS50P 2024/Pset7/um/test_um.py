# Maimoona Aziz

from um import count


def test_format():
    assert count(r"hello, um, world") == 1
    assert count(r"um") == 1
    assert count(r"Um, thanks, um...") == 2


def test_words():
    assert count(r"um, thanks for the album") == 1
    assert count(r"Due to circumstances, the umberellas are out of stock") == 0
    assert count(r"yummy") == 0


def test_case():
    assert count(r"Um, thanks, um") == 2
    assert count(r"UM, I forgot to document the humification") == 1
    assert count(r"She UM, forgot the drums and um...") == 2
