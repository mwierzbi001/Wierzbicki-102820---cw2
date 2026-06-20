from application.calculator import add, sub


def test_addition():
    assert add(10, 35) == 45


def test_subtract():
    assert sub(35, 10) == 25
