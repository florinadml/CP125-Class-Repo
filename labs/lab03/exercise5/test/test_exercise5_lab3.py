import pytest
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from exercise5 import get_position, has_overtaken

def test_overtake_success():
    before = [5, 3, 7, 2, 9]
    after = [5, 7, 3, 2, 9]
    assert has_overtaken(before, after, 7, 3) == True

def test_overtake_fail_fell_behind():
    before = [5, 3, 7, 2, 9]
    after = [5, 7, 3, 2, 9]
    assert has_overtaken(before, after, 3, 7) == False

def test_no_overtake_already_ahead():
    before = [5, 3, 7, 2, 9]
    after = [5, 7, 3, 2, 9]
    assert has_overtaken(before, after, 5, 3) == False

def test_no_overtake_same_position():
    before = [5, 3, 7, 2, 9]
    after = [5, 3, 7, 2, 9]
    assert has_overtaken(before, after, 7, 3) == False

def test_overtake_first_to_second():
    before = [1, 2, 3]
    after = [2, 1, 3]
    assert has_overtaken(before, after, 2, 1) == True

def test_overtake_last_to_first():
    before = [1, 2, 3]
    after = [3, 2, 1]
    assert has_overtaken(before, after, 3, 1) == True

def test_get_position_first():
    cars = [5, 3, 7, 2, 9]
    assert get_position(cars, 5) == 0

def test_get_position_last():
    cars = [5, 3, 7, 2, 9]
    assert get_position(cars, 9) == 4

def test_get_position_middle():
    cars = [5, 3, 7, 2, 9]
    assert get_position(cars, 7) == 2
