import pytest
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from exercise4 import has_warming_trend

def test_warming_at_start():
    assert has_warming_trend([25, 27, 29, 28, 30, 32, 31]) == True

def test_warming_at_end():
    assert has_warming_trend([30, 29, 28, 27, 28, 29, 30]) == True

def test_no_warming_decreasing():
    assert has_warming_trend([30, 29, 28, 27, 26, 25, 24]) == False

def test_no_warming_flat():
    assert has_warming_trend([25, 25, 25, 25, 25]) == False

def test_minimum_warming():
    assert has_warming_trend([1, 2, 3]) == True

def test_too_short():
    assert has_warming_trend([1, 2]) == False

def test_single_element():
    assert has_warming_trend([25]) == False

def test_empty_list():
    assert has_warming_trend([]) == False

def test_warming_with_plateau():
    assert has_warming_trend([20, 21, 21, 22, 23, 24]) == True

def test_no_warming_zigzag():
    assert has_warming_trend([20, 25, 20, 25, 20, 25]) == False
