import pytest
from exercise4 import show_science_distribution
import matplotlib
matplotlib.use('Agg')


def test_returns_student_count():
    result = show_science_distribution("../data/students.csv")
    assert result == 25


def test_return_type():
    result = show_science_distribution("../data/students.csv")
    assert isinstance(result, int)


def test_count_positive():
    result = show_science_distribution("../data/students.csv")
    assert result > 0


def test_count_matches_data():
    result = show_science_distribution("../data/students.csv")
    assert result == 25


def test_function_exists():
    assert callable(show_science_distribution)


def test_accepts_string_parameter():
    result = show_science_distribution("../data/students.csv")
    assert result is not None


def test_returns_integer():
    result = show_science_distribution("../data/students.csv")
    assert type(result) == int


def test_count_not_zero():
    result = show_science_distribution("../data/students.csv")
    assert result != 0


def test_count_reasonable_range():
    result = show_science_distribution("../data/students.csv")
    assert 1 <= result <= 100


def test_multiple_calls_consistent():
    result1 = show_science_distribution("../data/students.csv")
    result2 = show_science_distribution("../data/students.csv")
    assert result1 == result2
