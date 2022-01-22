import pytest

from calculator import add, multiply, divide


@pytest.mark.parametrize("a, b, c", [(1, 1, 2), (10, 5, 15), (4, 5, 9)])
def test_add(a, b, c):
    assert add(a, b) == c


@pytest.mark.parametrize("a, b, c", [(1, 1, 1), (10, 5, 50), (4, 5, 20)])
def test_multiply(a, b, c):
    assert multiply(a, b) == c


@pytest.mark.parametrize("a, b, c", [(1, 1, 1), (10, 5, 2), (40, 5, 8)])
def test_divide(a, b, c):
    assert divide(a, b) == c
