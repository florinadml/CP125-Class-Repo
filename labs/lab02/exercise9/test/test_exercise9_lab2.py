import pytest
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from exercise9 import calculate_xp_required, can_level_up, simulate_leveling

# Tests for calculate_xp_required
def test_xp_required_level_1():
    # Level 1 -> 2 requires 100 XP
    assert calculate_xp_required(1) == 100

def test_xp_required_level_2():
    # Level 2 -> 3 requires 200 XP
    assert calculate_xp_required(2) == 200

def test_xp_required_level_3():
    # Level 3 -> 4 requires 300 XP
    assert calculate_xp_required(3) == 300

def test_xp_required_level_10():
    # Level 10 -> 11 requires 1000 XP
    assert calculate_xp_required(10) == 1000

# Tests for can_level_up
def test_can_level_up_exact():
    assert can_level_up(100, 100) == True

def test_can_level_up_enough():
    assert can_level_up(150, 100) == True

def test_cannot_level_up_insufficient():
    assert can_level_up(99, 100) == False

def test_cannot_level_up_zero():
    assert can_level_up(0, 100) == False

# Tests for simulate_leveling
def test_simulate_level_1_to_2():
    # 100 XP -> Level 2, 0 remaining
    level, remaining = simulate_leveling(100)
    assert level == 2
    assert remaining == 0

def test_simulate_level_1_to_3():
    # 300 XP -> Level 3 (100 + 200), 0 remaining
    level, remaining = simulate_leveling(300)
    assert level == 3
    assert remaining == 0

def test_simulate_level_1_to_4():
    # 600 XP -> Level 4 (100 + 200 + 300), 0 remaining
    level, remaining = simulate_leveling(600)
    assert level == 4
    assert remaining == 0

def test_simulate_with_leftover():
    # 650 XP -> Level 4, 50 remaining
    level, remaining = simulate_leveling(650)
    assert level == 4
    assert remaining == 50

def test_simulate_not_enough_for_level_2():
    # 50 XP -> Level 1, 50 remaining
    level, remaining = simulate_leveling(50)
    assert level == 1
    assert remaining == 50

def test_simulate_zero_xp():
    # 0 XP -> Level 1, 0 remaining
    level, remaining = simulate_leveling(0)
    assert level == 1
    assert remaining == 0

def test_simulate_large_xp():
    # 5500 XP -> 100+200+300+400+500+600+700+800+900+1000 = 5500 -> Level 11, 0 remaining
    level, remaining = simulate_leveling(5500)
    assert level == 11
    assert remaining == 0

def test_simulate_large_xp_with_remainder():
    # 5600 XP -> Level 11, 100 remaining
    level, remaining = simulate_leveling(5600)
    assert level == 11
    assert remaining == 100
