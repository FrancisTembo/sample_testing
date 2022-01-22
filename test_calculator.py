import pytest

from calculator import add, multiply


@pytest.mark.parametrize("a, b, c", [(1, 1, 2), (10, 5, 15), (4, 5, 9)])
def test_add(a, b, c):
    assert add(a, b) == c

@pytest.mark.parametrize("a, b, c", [(1, 1, 1), (10, 5, 50), (4, 5, 20)])
def test_multiply(a, b, c):
    assert multiply(a, b) == c
