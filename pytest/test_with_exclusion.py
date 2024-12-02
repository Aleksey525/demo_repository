import pytest


def divide(a, b):
    if b == 0:
        raise ZeroDivisionError('division by zero')
    return a / b


def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError, match=r'division by zero'):
        divide(10, 0)
