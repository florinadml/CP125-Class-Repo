import pytest
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from exercise3 import has_adjacent_seats

def test_adjacent_at_start():
    assert has_adjacent_seats([0, 0, 1, 1, 1, 1, 1, 1]) == True

def test_adjacent_at_end():
    assert has_adjacent_seats([1, 1, 1, 1, 1, 1, 0, 0]) == True

def test_adjacent_in_middle():
    assert has_adjacent_seats([1, 0, 0, 1, 0, 1, 0, 0]) == True

def test_no_adjacent():
    assert has_adjacent_seats([1, 0, 1, 0, 1, 0, 1, 0]) == False

def test_all_empty():
    assert has_adjacent_seats([0, 0, 0, 0]) == True

def test_all_taken():
    assert has_adjacent_seats([1, 1, 1, 1]) == False

def test_two_empty_seats():
    assert has_adjacent_seats([0, 0]) == True

def test_two_taken_seats():
    assert has_adjacent_seats([1, 1]) == False

def test_single_seat():
    assert has_adjacent_seats([0]) == False

def test_empty_list():
    assert has_adjacent_seats([]) == False
