import pytest
from add import add


def test_add_positive_numbers():
    result = add(2, 3)
    assert result == 5


def test_add_negative_numbers():
    result = add(-2, -3)
    assert result == -5


def test_add_mixed_numbers():
    result = add(5, -3)
    assert result == 2


if __name__ == "__main__":
    import pytest
    pytest.main()
