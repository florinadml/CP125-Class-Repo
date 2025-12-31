import pytest
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from exercise1 import count_bright_spots

def test_two_bright_spots():
    assert count_bright_spots([100, 120, 200, 150, 180, 160, 140]) == 2

def test_one_bright_spot():
    assert count_bright_spots([50, 100, 50]) == 1

def test_no_bright_spots_increasing():
    assert count_bright_spots([10, 20, 30]) == 0

def test_no_bright_spots_decreasing():
    assert count_bright_spots([30, 20, 10]) == 0

def test_all_same_values():
    assert count_bright_spots([50, 50, 50, 50]) == 0

def test_single_element():
    assert count_bright_spots([100]) == 0

def test_two_elements():
    assert count_bright_spots([100, 200]) == 0

def test_empty_list():
    assert count_bright_spots([]) == 0

def test_multiple_bright_spots():
    assert count_bright_spots([10, 50, 20, 80, 30, 90, 40]) == 3
