import pytest


def func(x):
    return x + 1


@pytest.mark.parametrize("input_value", [1, 2, 3, 4, 5])
def test_func(input_value):
    assert func(input_value) == input_value + 1