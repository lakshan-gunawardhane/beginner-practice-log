from bank import value

def test_return_zero():
    assert value("hello") == 0
    assert value("Hello") == 0
    assert value("HeLLo World") == 0

def test_return_twenty():
    assert value("Hi") == 20
    assert value("hey") == 20
    assert value("How are you?") == 20

def test_return_hundred():
    assert value("What's up?") == 100
    assert value("Good morning") == 100
    assert value("123") == 100