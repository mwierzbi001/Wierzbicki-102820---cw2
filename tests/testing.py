from application.calculator import add, sub

def testing_addition():
    assert add(10,35) == 45

def testing_subtract():
    assert sub(35, 10) == 25