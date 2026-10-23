import pytest

from fizzbuzz import FizzBuzz


@pytest.mark.parametrize(
    ("number", "expected"),
    [
        (1, 1),
        (2, 2),
        (3, "Fizz"),
        (6, "Fizz"),
        (5, "Buzz"),
        (10, "Buzz"),
        (15, "FizzBuzz"),
        (30, "FizzBuzz"),
    ],
)
def test_convert(number, expected):
    assert FizzBuzz().convert(number) == expected